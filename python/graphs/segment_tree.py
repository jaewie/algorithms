from segment_node import SegmentNode


def make_segment_tree(lst):
    return _make_segment_tree(lst, 0, len(lst) - 1)


def _make_segment_tree(lst, start_ind, end_ind, combine_func=min):
    if start_ind == end_ind:
        assert(len(lst) == 1)
        val = lst[0]
        return SegmentNode(val, start_ind, end_ind)

    mid = len(lst) // 2

    left = _make_segment_tree(lst[:mid], start_ind, start_ind + mid - 1)
    right = _make_segment_tree(lst[mid:], start_ind + mid, end_ind)

    root_val = combine_func(left.val, right.val)

    return SegmentNode(root_val, start_ind, end_ind, left, right)


def _query_min(node, start_ind, end_ind):
    if node.start_ind == start_ind and node.end_ind == end_ind:
        return node.val

    result = float('inf')
    left = node.left
    right = node.right

    if left.start_ind <= start_ind <= left.end_ind:
        result = min(result, query_min(left, start_ind, min(end_ind, left.end_ind)))

    if right.start_ind <= end_ind <= right.end_ind:
        result = min(result, query_min(right, max(start_ind, right.start_ind), end_ind))

    return result
