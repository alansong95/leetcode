class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_not_under_attack(row, col):
            return not rows[col] and not hills[row + col] and not dales[row - col]
        
        def place_queen(row, col):
            rows[col] = 1
            hills[row + col] = 1
            dales[row - col] = 1
        
        def remove_queen(row, col):
            rows[col] = 0
            hills[row + col] = 0
            dales[row - col] = 0
        
        def backtrack(row, count):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count
        
        rows = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n + 1)
        return backtrack(0, 0)