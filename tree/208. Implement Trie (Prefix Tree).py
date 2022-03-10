from collections import defaultdict


class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.isword = False


class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)