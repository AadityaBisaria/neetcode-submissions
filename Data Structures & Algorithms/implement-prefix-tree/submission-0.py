class TrienNode:
    def __init__(self):
        self.children={}
        self.endofword=False

class PrefixTree:

    def __init__(self):
        
        self.root=TrienNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for w in word:
            if w not in cur.children:
                cur.children[w]=TrienNode()
            cur=cur.children[w]
        cur.endofword=True
    

    def search(self, word: str) -> bool:
        cur=self.root
        for w in word:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        return cur.endofword
             

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        
        return True
        
        