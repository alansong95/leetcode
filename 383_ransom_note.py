<<<<<<< HEAD
# import collections
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         return len(collections.Counter(ransomNote) - collections.Counter(magazine))== 0

=======
>>>>>>> 9977ba8f050923a20a7f82c65c87ff0e1d6ad68e
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
<<<<<<< HEAD
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True
=======
        return len(collections.Counter(ransomNote) - collections.Counter(magazine))== 0
>>>>>>> 9977ba8f050923a20a7f82c65c87ff0e1d6ad68e
