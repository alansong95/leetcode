class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        intersection = collections.Counter(nums1) & collections.Counter(nums2)
        for item in intersection.items():
            for _ in range(item[1]):
                output.append(item[0])
        return output