class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        ht = {}
        for path in paths:
            ht[path[0]] = path[1]
        
        city = paths[0][0]
        while city in ht:
            city = ht[city]
        return city