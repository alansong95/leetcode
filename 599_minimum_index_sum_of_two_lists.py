class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ht = {}
        ht2 = {}
        
        for ind, item in enumerate(list1):
            ht[item] = ind
        
        for ind, item in enumerate(list2):
            if item in ht:
                ht2[item] = ind + ht[item]
        
        min_value = min(ht2.values())
        return [key for key, value in ht2.iteritems() if value == min_value]
            
        