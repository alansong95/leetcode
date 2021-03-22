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


class Solution2(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        
        return ans