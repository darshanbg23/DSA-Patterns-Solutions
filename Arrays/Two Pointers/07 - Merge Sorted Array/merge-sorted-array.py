class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        left = m-1
        right = n-1
        indx = (m+n)-1

        while right >= 0:

            if left >= 0 and nums1[left] > nums2[right]:
                nums1[indx] = nums1[left]
                left -= 1
                indx -= 1
            else:
                nums1[indx] = nums2[right]
                right -= 1
                indx -= 1