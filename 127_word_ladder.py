class Solution(object):
    def preprocess(self, wordList):
        d = {}
        for word in wordList:
            for c in range(len(word)):
                wildcard = word[:c] + '*' + word[c+1:]
                if wildcard not in d:
                    d[wildcard] = []
                d[wildcard].append(word)
                
        
        return d
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # error checking
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        # preprocessing
        processedWords = self.preprocess(wordList)
        
        # BFS
        queue = deque()
        queue.append([beginWord, 1])
        visited = set()
        
        while queue:
            curr, level = queue.popleft()
            for c in range(len(curr)):
                wildcard = curr[:c] + '*' + curr[c+1:]
                if wildcard in processedWords:
                    for word in processedWords[wildcard]:
                        if word == endWord:
                            return level + 1
                        
                        if word not in visited:
                            visited.add(word)
                            queue.append([word, level + 1])
                            
                        
        
        
        return 0