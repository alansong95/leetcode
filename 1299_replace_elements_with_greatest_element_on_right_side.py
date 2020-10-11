# brute force
# Time: O(n^2)
# Space: O(1)
# class Solution:
#     def replaceElements(self, arr):
#         for i in range(len(arr)):
#             largest = 0
#             for j in range(i+1, len(arr)):
#                 if arr[j] > largest:
#                     largest = arr[j]
#             arr[i] = largest
#         arr[-1] = -1
#         return arr

# optimized solution iterate from back
# Time: O(n)
# Space: O(1)
class Solution:
    def replaceElements(self, arr):
        largest = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = largest
            if temp > largest:
                largest = temp
        return arr


solution = Solution()
print(solution.replaceElements([17,18,5,4,6,1]))
