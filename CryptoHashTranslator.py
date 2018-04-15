# -*- coding: utf-8 -*-
from src.Crypto.Cesar import cesarToTxtClass, txtToCesarClass
from src.Hash.Md5 import md5ToTxtClass, txtToMd5Class
from src.Hash.Sha import shaToTxtClass, txtToShaClass
from src.Miscellaneous.Parser import ParserClass

p = ParserClass.ParserClass()
parsed = p.getParsed()

if parsed.text:   
    print "TEXT"
    if parsed.translate:
        print "Translate"
        if parsed.md5:
            print "MD5"
        elif parsed.sha1:
            print "SHA1"
        elif parsed.sha256:
            print "SHA256"
        elif parsed.sha384:
            print "SHA384"
        elif parsed.sha512:
            print "SHA512"
        elif parsed.cesar:
            print "cesar"
        elif parsed.vigenere:
            print "vigenere"
    elif parsed.generate:
        print "Generate"
        if parsed.md5:
            print "MD5"
        elif parsed.sha1:
            print "SHA1"
        elif parsed.sha256:
            print "SHA256"
        elif parsed.sha384:
            print "SHA384"
        elif parsed.sha512:
            print "SHA512"
        elif parsed.cesar:
            print "cesar"
        elif parsed.vigenere:
            print "vigenere"
    else:
        print "Error ARGS"