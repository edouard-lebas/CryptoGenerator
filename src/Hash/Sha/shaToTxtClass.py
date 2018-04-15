import urllib
class shaToTxtClass:
    
    def __init__(self, hash):
        self.hash = hash
        self.type = "sha1"
        self.email = "lebas.edouard@elebas.fr"
        self.code = "7baef180cfe77097"

    def processSha1(self):
        self.type = "sha1"
        params = urllib.urlencode({'hash': self.hash, 'hash_type': self.type, 'email': self.email, 'code': self.code})
        f = urllib.urlopen("http://md5decrypt.net/Api/api.php?%s" % params)
        resp = f.read()
        return resp.strip()

    # def processSha224(self):
    #     self.type = "sha224"
    #     params = urllib.urlencode({'hash': self.hash, 'hash_type': self.type, 'email': self.email, 'code': self.code})
    #     f = urllib.urlopen("http://md5decrypt.net/Api/api.php?%s" % params)
    #     resp = f.read()
    #     return resp.strip()

    def processSha256(self):
        self.type = "sha256"
        params = urllib.urlencode({'hash': self.hash, 'hash_type': self.type, 'email': self.email, 'code': self.code})
        f = urllib.urlopen("http://md5decrypt.net/Api/api.php?%s" % params)
        resp = f.read()
        return resp.strip()


    def processSha384(self):
        self.type = "sha384"
        params = urllib.urlencode({'hash': self.hash, 'hash_type': self.type, 'email': self.email, 'code': self.code})
        f = urllib.urlopen("http://md5decrypt.net/Api/api.php?%s" % params)
        resp = f.read()
        return resp.strip()


    def processSha512(self):
        self.type = "sha512"
        params = urllib.urlencode({'hash': self.hash, 'hash_type': self.type, 'email': self.email, 'code': self.code})
        f = urllib.urlopen("http://md5decrypt.net/Api/api.php?%s" % params)
        resp = f.read()
        return resp.strip()
