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
# class Solution(object):
#     def duplicateZeros(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: None Do not return anything, modify arr in-place instead.
#         """
#         i = 0
#         while i < len(arr): 
#             if arr[i] == 0:
#                 temp_prev = 0
#                 for j in range(i+1, len(arr)):
#                     if j < len(arr):
#                         temp = arr[j]
#                         arr[j] = temp_prev
#                         temp_prev = temp
#                 i+=1
#             i+=1


# if constraint "in place" is there
# more elegant & better solution
# Time: O(n)
# Space: O(1)
class Solution(object):
    def duplicateZeros(self, arr):
        arr_len = len(arr)-1
        zero_count = 0
        i = 0
        while i + zero_count <= arr_len:
            if arr[i] == 0:
                if i == arr_len - zero_count:
                    arr[arr_len] = 0
                    arr_len -= 1
                    break
                zero_count += 1
            i += 1

        j = arr_len
        for i in range(arr_len-zero_count, -1, -1):
            arr[j] = arr[i]
            if arr[i] == 0:
                arr[j-1] = arr[i]
                j -= 1
            j -= 1
        print(arr)


solution = Solution()
solution.duplicateZeros([1,0,2,3,0,4,5,0])
solution.duplicateZeros([1,2,3])
solution.duplicateZeros([8,4,5,0,0,0,0,7])
solution.duplicateZeros([8,4,5,0,0,5,0,7])
solution.duplicateZeros([8,4,5,2,3,0,0,7])
solution.duplicateZeros([])
solution.duplicateZeros([0])
solution.duplicateZeros([1])
solution.duplicateZeros([1,0])
