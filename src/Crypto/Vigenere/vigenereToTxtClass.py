# -*- coding: utf-8 -*-
class vigenereToTxtClass:

    def __init__(self, text,key=None):
        self.text = text.decode("utf-8").upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".decode("utf-8")
        if key != None:
            self.key = key.decode("utf-8").upper()

    def processVigenereWithKey(self):
        keyIndex = 0
        decrypted = ""
        for t in self.text:
            index = self.alphabet.find(t)
            if index != -1:
                index -= self.alphabet.find(self.key[keyIndex])
                index %= len(self.alphabet)
                decrypted = decrypted + self.alphabet[index]
                keyIndex += 1
                if keyIndex == len(self.key):
                    keyIndex = 0
            else:
                decrypted += t
        return decrypted

    