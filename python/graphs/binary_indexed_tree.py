class BinaryIndexedTree(object):
  def __init__(self, nums=tuple()):
    self.bit = [0] * (len(nums) + 1)
    for index, val in enumerate(nums):
      self.update(index, val)

  def update(self, index, val):
    index += 1
    while index < len(self.bit):
      self.bit[index] += val
      index = index + (index & -index)

  def sum(self, start, end):
    if start > end:
      raise IllegalArgumentException('Start %d is greater than end %d' % start, end)
    elif start < 0 or start >= len(self.bit) - 1:
      raise IndexError('Start %d is out of bound' % start)
    elif end < 0 or end >= len(self.bit) - 1:
      raise IndexError('End %d is out of bound' % end)

    return self._sum(end) - self._sum(start - 1)

  def _sum(self, end):
    end += 1
    total = 0
    while end > 0:
      total += self.bit[end]
      end = end & (end - 1)
    return total


if __name__ == '__main__':
  nums = [1, 2, 3, 4, 5]
  bit = BinaryIndexedTree(nums)

  for i in range(len(nums)):
    for j in range(i, len(nums)):
      print (i, j), bit.sum(i, j) == sum(nums[i: j + 1])
