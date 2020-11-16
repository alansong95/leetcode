class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        try:
            x = coordinates[1][0] - coordinates[0][0]
            y = coordinates[1][1] - coordinates[0][1]
            
            if x == 0:
                for i in range(2, len(coordinates)):
                    _x = coordinates[i][0] - coordinates[i-1][0]
                    if _x != 0:
                        return False
                return True
            
            slope = y / float(x)

            for i in range(2, len(coordinates)):
                x = coordinates[i][0] - coordinates[i-1][0]
                y = coordinates[i][1] - coordinates[i-1][1]

                tempSlope = y / float(x)

                if tempSlope != slope:
                    return False
            return True
        except:
            print('except')
            return False