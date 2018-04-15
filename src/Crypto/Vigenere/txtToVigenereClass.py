# -*- coding: utf-8 -*-
class txtToVigenereClass:

    def __init__(self, text,key):
        self.text = text.decode("utf-8").upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".decode("utf-8")
        self.key = key.decode("utf-8").upper()

    def processVigenere(self):
        keyIndex = 0
        crypted = ""
        for t in self.text:
            index = self.alphabet.find(t)
            if index != -1:
                index += self.alphabet.find(self.key[keyIndex])
                index %= len(self.alphabet)
                crypted = crypted + self.alphabet[index]
                keyIndex += 1
                if keyIndex == len(self.key):
                    keyIndex = 0
            else:
                crypted += t
        return crypted