# import collections
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         return len(collections.Counter(ransomNote) - collections.Counter(magazine))== 0

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         for c in set(ransomNote):
#             if ransomNote.count(c) > magazine.count(c):
#                 return False
#         return True

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return all([ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote)])