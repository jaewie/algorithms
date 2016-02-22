from tree_node import TreeNode


class QuadTreeNode(TreeNode):
    def __init__(self, top_left, top_right):
        super(IntervalNode, self).__init__((top_left, top_right))

    def update_max_endpoints(self):
        left = self.left.max_ep if self.left else None
        right = self.right.max_ep if self.right else None
        cur = self.max_ep

        self._max_endpoint = max(left, right, cur)
        if self.parent:
            self.parent.update_max_endpoints()

    def intersects(self, query_interval):
        lo, hi = self.val
        q_lo, q_hi = query_interval
        is_between = lambda c, lo, hi: lo <= c <= hi

        return (is_between(q_lo, lo, hi) or
                is_between(q_hi, lo, hi) or
                is_between(lo, q_lo, q_hi) or
                is_between(hi, q_lo, q_hi))

    def query(self, query_interval):
        result = []

        if self.intersects(query_interval):
            result.append(self.val)

        left, right = self.left, self.right
        lo, hi = query_interval

        if left and left.max_ep >= lo:
            result.extend(left.query(query_interval))
        if right and right.max_ep >= lo and right.lo <= hi:
            result.extend(right.query(query_interval))
        return result
