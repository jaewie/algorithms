from operator import itemgetter 
from math import sqrt


def closest_pair(pts):
  px = sorted(pts, key=itemgetter(0))
  py = sorted(pts, key=itemgetter(1))
  return _closest_pair(px, py)

def _closest_pair(px, py):
  if len(px) < 2:
    return (None, None)
  if len(px) == 2:
    return px

  mid = len(px) / 2
  mid_line = px[mid][0]
  L = _closest_pair(px[:mid], py[:mid])
  R = _closest_pair(px[:mid + 1], py[:mid + 1])
  delta = min(distance(L), distance(R))
  
  sx = [pt for pt in py if abs(mid_line - pt[0]) <= delta]
  S = closest_split_pair(sx)

  return min(L, R, S, key=distance)

def closest_split_pair(sx):
  closest_pair = (None, None)
  pts_consider = 6

  for i, pt0 in enumerate(sx):
    for pt1 in sx[i + 1 : (i + 1) + pts_consider]:
      closest_pair = min(closest_pair, (pt0, pt1), key=distance)
  return closest_pair
     
def distance(pts):
  if pts == (None, None):
    return float("inf")
  pt0, pt1 = pts
  return sqrt((pt0[0] - pt1[0]) ** 2 + (pt0[1] - pt1[1]) ** 2)
