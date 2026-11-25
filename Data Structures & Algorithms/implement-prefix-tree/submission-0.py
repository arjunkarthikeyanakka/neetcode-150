from collections import defaultdict as dd
class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.end_of_word=False
    
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        t=self.root
        n=len(word)
        for i in range(n):
            idx=ord(word[i])-97
            if not t.children[idx]:
                t.children[idx]=TrieNode()
            t=t.children[idx]
            if i==n-1:
                t.end_of_word=True

    def search(self, word: str) -> bool:
        t=self.root
        n=len(word)
        for i in range(n):
            idx=ord(word[i])-97
            if not t.children[idx]:
                return False
            t=t.children[idx]
        return t.end_of_word

    def startsWith(self, prefix: str) -> bool:
        t=self.root
        n=len(prefix)
        for i in range(n):
            idx=ord(prefix[i])-97
            if not t.children[idx]:
                return False
            t=t.children[idx]
        return True