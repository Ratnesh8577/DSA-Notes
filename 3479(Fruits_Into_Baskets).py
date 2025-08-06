class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = nums[lo]
            return
        mid = (lo + hi) // 2
        self.build(nums, 2 * tree_index + 1, lo, mid)
        self.build(nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = max(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, tree_index, lo, hi, i, val):
        if lo == hi:
            self.tree[tree_index] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * tree_index + 1, lo, mid, i, val)
        else:
            self._update(2 * tree_index + 2, mid + 1, hi, i, val)
        self.tree[tree_index] = max(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def query_first(self, target):
        return self._query_first(0, 0, self.n - 1, target)

    def _query_first(self, tree_index, lo, hi, target):
        if self.tree[tree_index] < target:
            return -1
        if lo == hi:
            self.update(lo, -1)  # Mark the basket as used
            return lo
        mid = (lo + hi) // 2
        if self.tree[2 * tree_index + 1] >= target:
            return self._query_first(2 * tree_index + 1, lo, mid, target)
        else:
            return self._query_first(2 * tree_index + 2, mid + 1, hi, target)


class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        tree = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            if tree.query_first(fruit) == -1:
                unplaced += 1

        return unplaced
# Copy in Google
    