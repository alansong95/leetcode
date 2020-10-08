# if constraint "in place" is not there
# time: O(n)
# space: O(n)
# class Solution(object):
#     def duplicateZeros(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: None Do not return anything, modify arr in-place instead.
#         """
#         dest = []
#         for e in arr:
#             dest.append(e)
#             if e == 0:
#                 dest.append(e)
#         arr = dest[:len(arr)]
#         print(arr)


# if constraint "in place" is there
# brute force
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr): 
            if arr[i] == 0:
                temp_prev = 0
                for j in range(i+1, len(arr)):
                    if j < len(arr):
                        temp = arr[j]
                        arr[j] = temp_prev
                        temp_prev = temp
                i+=1
            i+=1
        print(arr)

            
            




solution = Solution()
solution.duplicateZeros([1,0,2,3,0,4,5,0])
solution.duplicateZeros([1,2,3])