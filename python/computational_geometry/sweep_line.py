from operator import itemgetter
from collections import defaultdict


def max_intersecting_intervals(intervals):
  # sweep line algorithm
  points = [(x[0], x) for x in intervals] + [(x[1], x) for x in intervals]
  points.sort(key=itemgetter(0))

  lines = set()
  intersections = {interval: 0 for interval in intervals}

  for point, interval in points:
    if is_starting_interval(point, interval):
      lines.add(interval)
      if lines:
        for line in lines:
          intersections[line] += 1
    else:
      lines.remove(interval)
  return max(intersections, key=lambda x: intersections[x])
    
def is_ending_interval(point, interval):
  return point == interval[1]

def is_starting_interval(point, interval):
  return point == interval[0]
