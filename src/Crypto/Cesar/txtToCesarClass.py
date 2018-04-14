class txtToCesar:

    def __init__(self,txt,offset):
        self.txt = txt.decode("utf-8").upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".decode("utf-8")
        self.offset = offset

    def processCesar(self):
        crypted = ""
        for t in self.txt:
            if t in self.alphabet:
                index = self.alphabet.find(t)
                index += self.offset
                if index >= len(self.alphabet):
                    index = index - len(self.alphabet)
                crypted += self.alphabet[index]
            else:
                crypted += t
        return crypted
