from collections import defaultdict as dd
class TrieNode:
    '''
    A TrieNode doesnt have current node value, it is taken from its parent node's children value.
    ex: root(*)->children{'d'}, and d has o in its children and o has g, and g has end of word as true, 
    which makes dog a stored word. 
    '''
    def __init__(self):
        self.children=dd(TrieNode) #this will have info about children of current node
        self.end_of_word=False  #this will confirm if a word ends at current node

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        t=self.root
        n=len(word)
        for i in range(n):
            if not t.children[word[i]]:
                t.children[word[i]]=TrieNode()
            t=t.children[word[i]]
            if i==n-1:
                t.end_of_word=True

    def search(self, word: str) -> bool:
        def dfs(idx,curr):
            if len(word)==idx:
                return curr.end_of_word
            char=word[idx]
            if char=='.':
                for ch in curr.children.values():
                    if (dfs(idx+1,ch)):
                        return True
                return False
            return char in curr.children and dfs(idx+1,curr.children[char])
        return dfs(0,self.root)


