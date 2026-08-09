class Trienode:
    def __init__(self):
        self.children={}
        self.endofword=False

class WordDictionary:

    def __init__(self):
        self.root=Trienode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=Trienode()
            cur=cur.children[char]
        cur.endofword=True


    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            cur=root

            for i in range(j,len(word)):
                c=word[i]
                if c==".":
                    for child in cur.children:
                        if dfs(i+1,cur.children[child]):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.endofword
        return dfs(0,self.root)
        
