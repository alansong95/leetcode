class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = defaultdict(list)
        max_freq = None
        ans = 50001
        
        for i, num in enumerate(nums):
            hashmap[num].append(i)
            if num == max_freq:
                ans = hashmap[num][-1] - hashmap[num][0]
            elif not max_freq or len(hashmap[num]) > len(hashmap[max_freq]):
                max_freq = num
                ans = hashmap[num][-1] - hashmap[num][0]
            elif len(hashmap[num]) == len(hashmap[max_freq]):
                if hashmap[num][-1] - hashmap[num][0] < ans:
                    max_freq = num
                    ans = hashmap[num][-1] - hashmap[num][0]
        
        return ans + 1