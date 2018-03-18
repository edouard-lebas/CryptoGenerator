import urllib

class md5ToTxtClass:
    
    def __init__(self, hash):
        self.hash = hash
        self.type = "md5"
        self.email = ""
        self.code = ""

    def processTxt(self):
        params = urllib.urlencode({'hash': self.hash, 'hash_type': self.type, 'email': self.email, 'code': self.code})
        f = urllib.urlopen("http://md5decrypt.net/Api/api.php?%s" % params)
        resp = f.read()
        return resp.strip()