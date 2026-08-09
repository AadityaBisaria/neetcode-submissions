from collections import Counter
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        words=wordList+[beginWord]
        adj={word:[] for word in words}
        
        def differ_by_one_char(word1, word2):
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_count += 1
                if diff_count > 1:
                    return False
            return True
        
        for word in words:
            for oword in words:
                if word!=oword and differ_by_one_char(word,oword):
                    adj[word].append(oword)
                    adj[oword].append(word)
        
        visit=set()
        visiting=set([beginWord])

        def dfs(word):
            if word in visit:
                return float("inf")
            visit.add(word)
            if word==endWord:
                return 1
            res=float("inf")
            for words in adj[word]:
                res=min(res, 1+dfs(words))
            return res
        
        q=deque([beginWord])
        res=1       
        while(q):
            
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                
                for oword in adj[word]:
                    if oword not in visiting:
                        visiting.add(oword)
                        q.append(oword)
            res+=1
        return 0
                
                


