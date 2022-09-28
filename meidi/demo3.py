class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word: str) -> None:
        for w in word:
            ch = ord(w) - ord('a')
            if not self.children[ch]:
                self.children[ch] = Trie()
            self = self.children[ch]
        self.isEnd = True

    def search(self, word: str) -> bool:
        for w in word:
            ch = ord(w) - ord('a')
            if not self.children[ch]:
                return False
            self = self.children[ch]
        return self.isEnd

    def startsWith(self, prefix: str) -> bool:
        for w in prefix:
            ch = ord(w) - ord('a')
            if not self.children[ch]:
                return False
            self = self.children[ch]
        return True


if __name__ == '__main__':
    opt = eval(input().strip())
    words = eval(input().strip())
    tree = Trie()
    res = []
    for i in range(len(opt)):
        if opt[i] == 'insert':
            tree.insert(words[i])
            res.append("null")
        elif opt[i] == 'search':
            t = tree.search(words[i])
            if t:
                res.append("true")
            else:
                res.append("false")
        else:
            t = tree.startsWith(words[i])
            if t:
                res.append("true")
            else:
                res.append("false")
    s = '['
    for i in res:

        s += '"' + i + '"' + ','
    s = s[:-1]
    s += ']'
    print(s)

