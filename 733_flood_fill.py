class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        original_num = image[sr][sc]
        nr = len(image)
        nc = len(image[0])
        seen = set()

        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop(0)
            image[r][c] = newColor
            seen.add((r, c))
            
            if r-1 >= 0 and image[r-1][c] == original_num and (r-1, c) not in seen:
                queue.append((r-1, c))
            if r+1 < nr and image[r+1][c] == original_num and (r+1, c) not in seen:
                queue.append((r+1, c))
            if c-1 >= 0 and image[r][c-1] == original_num and (r, c-1) not in seen:
                queue.append((r, c-1))
            if c+1 < nc and image[r][c+1] == original_num and (r, c+1) not in seen:
                queue.append((r, c+1))
         
        return image