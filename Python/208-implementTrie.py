# Chris:TODO::read this one more time!!!!

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = {}
        self.isWord = False
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
               child = TrieNode()
               node.childs[letter] = child
            node = child
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            node = node.childs.get(letter)
            if node is None:
               return False
        return node.isWord
        
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.childs.get(letter)
            if node is None:
               return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")