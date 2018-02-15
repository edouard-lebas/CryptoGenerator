import hashlib
class txtToMd5Class:
    
    def __init__(self, text):
        self.text = text

    def processMd5(self):
        return hashlib.md5(self.text).hexdigest()