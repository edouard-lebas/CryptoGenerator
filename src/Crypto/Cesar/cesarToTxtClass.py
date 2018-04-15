class cesarToTxtClass:

    def __init__(self, cesar, offset=None):
        self.cesar = cesar.decode("utf-8").upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".decode("utf-8")
        if offset != None:
            self.offset = offset

    def processCesarWithOffset(self):
        decrypted = ""
        for c in self.cesar:
            if c in self.alphabet:
                index = self.alphabet.find(c)
                index = index - self.offset
                if index < 0:
                    index = index + len(self.alphabet)
                decrypted += self.alphabet[index]
            else:
                decrypted += self.alphabet[index]
        return decrypted

    def processCesarWithoutOffset(self):
        decrypted = []
        for a in range(1,len(self.alphabet)+1):
            print a
            word = ""
            for c in self.cesar:
                if c in self.alphabet:
                    index = self.alphabet.find(c)
                    index = index - a
                    if index < 0:
                        index = index + len(self.alphabet)
                    word += self.alphabet[index]
                else:
                    word += self.alphabet[index]
            decrypted.append(word)
        return decrypted
