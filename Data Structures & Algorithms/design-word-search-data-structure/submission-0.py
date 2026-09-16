class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        # Helper function to handle character branching and wildcards via DFS
        def dfs(j: int, root: TrieNode) -> bool:
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    # Wildcard check: explore all possible paths at the current node
                    for child_node in cur.child.values():
                        if dfs(i + 1, child_node):
                            return True
                    return False
                else:
                    # Standard exact match check
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
                    
            return cur.endOfWord

        return dfs(0, self.root)
