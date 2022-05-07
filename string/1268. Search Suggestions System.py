from typing import List


class Node:
    def __init__(self, val):
        self.word_list = set({})
        self.val = val
        self.son_list = {i: None for i in 'abcdefghijklmnopqrstuvwxyz'}

    def add_word(self, word):
        self.word_list.add(word)


class Tier:
    def __init__(self, word_list):
        self.root = Node(None)
        for word in word_list:
            root = self.root
            for char in word:
                if root.son_list.get(char) is None:
                    son = Node(char)
                    root.son_list[char] = son
                    son.word_list.add(word)
                else:
                    son = root.son_list.get(char)
                    son.word_list.add(word)
                root = son

    def get_suggestion(self, word):
        suggestion = []
        root = self.root
        for char in word:
            if root.son_list.get(char) is not None:
                suggestion.append(sorted(list(root.son_list.get(char).word_list))[:3])
                root = root.son_list.get(char)
            else:
                suggestion.append([])
        return suggestion


class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Tier(products)
        return t.get_suggestion(searchWord)






if __name__ == '__main__':
    Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], searchWord='mouse')