class UglyCipher:
    def july(self, word, key):
        chars = []
        for line in word:
            chars.extend(line)

        for i in range(len(chars)):
            chars[i] = chr(ord(chars[i]) + key)

        return ''.join(chars)

    def reverse(self, word):
        return word[::-1]

    def rnd_split(self, word, c):
        return word.split(c)

    def mod_sort(self, words, a):
        stack = []
        for i in range(len(words)):
            stack.append(words[(i+a) % len(words)])
            
        return stack

    def buildCipher(self, source='', key=3, c='', a=1):
        return self.mod_sort(self.rnd_split(self.reverse(self.july(source, key)), c), a)

