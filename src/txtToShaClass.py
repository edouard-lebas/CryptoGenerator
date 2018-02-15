import hashlib
class txtToShaClass:
    
    def __init__(self, text):
        self.text = text

    def processSha1(self):
        return hashlib.sha1(self.text).hexdigest()

    def processSha224(self):
        return hashlib.sha224(self.text).hexdigest()

    def processSha256(self):
        return hashlib.sha256(self.text).hexdigest()

    def processSha384(self):
        return hashlib.sha384(self.text).hexdigest()

    def processSha512(self):
        return hashlib.sha512(self.text).hexdigest()

toto = txtToShaClass("bonjour")
print toto.processSha1()

toto = txtToShaClass("bonjour")
print toto.processSha224()

toto = txtToShaClass("bonjour")
print toto.processSha256()

toto = txtToShaClass("bonjour")
print toto.processSha384()

toto = txtToShaClass("bonjour")
print toto.processSha512()
