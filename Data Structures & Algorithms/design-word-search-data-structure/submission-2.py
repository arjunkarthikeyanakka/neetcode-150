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
        found=False
        def dfs(idx,curr):
            nonlocal word,found
            if idx<len(word) and curr:
                if word[idx] in curr.children:
                    curr=curr.children[word[idx]]
                    # print(word[idx],'...',word,curr.end_of_word)
                    if idx==len(word)-1:
                        found|=curr.end_of_word
                        return curr.end_of_word
                    if dfs(idx+1,curr):
                        found|=dfs(idx+1,curr)
                else:
                    if word[idx]=='.':
                        for c in curr.children:
                            if dfs(idx+1,curr.children[c]):
                                found|=dfs(idx+1,curr.children[c])
                    else:
                        return False
            if idx==len(word):
                return curr.end_of_word
        t=self.root
        dfs(0,t)
        return found
