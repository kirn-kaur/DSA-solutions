class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  # binary search on the shorter array
        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2   # elements taken from A into the left half
            j = half - i         # elements taken from B into the left half

            a_left = A[i - 1] if i > 0 else float("-inf")
            a_right = A[i] if i < m else float("inf")
            b_left = B[j - 1] if j > 0 else float("-inf")
            b_right = B[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
            elif a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1