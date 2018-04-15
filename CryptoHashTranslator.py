# -*- coding: utf-8 -*-
from src.Miscellaneous.Parser import ParserClass
from src.Crypto.Cesar.cesarToTxtClass import cesarToTxtClass
from src.Crypto.Cesar.txtToCesarClass import txtToCesarClass
from src.Hash.Md5.md5ToTxtClass import md5ToTxtClass
from src.Hash.Md5.txtToMd5Class import txtToMd5Class
from src.Hash.Sha.shaToTxtClass import shaToTxtClass
from src.Hash.Sha.txtToShaClass import txtToShaClass
from src.Crypto.Vigenere.txtToVigenereClass import txtToVigenereClass


p = ParserClass.ParserClass()
parsed = p.getParsed()

if parsed.text:
    if parsed.generate:
        tmd5 = txtToMd5Class(parsed.text)
        tsha = txtToShaClass(parsed.text)
        if parsed.md5:            
            print "TEXT > "+parsed.text
            print "MD5 > "+tmd5.processMd5()
        elif parsed.sha1:            
            print "TEXT > "+parsed.text
            print "SHA1 > "+tsha.processSha1()
        elif parsed.sha256:
            print "TEXT > "+parsed.text
            print "SHA256 > "+tsha.processSha256()
        elif parsed.sha384:
            print "TEXT > "+parsed.text
            print "SHA384 > "+tsha.processSha384()
        elif parsed.sha512:
            print "TEXT > "+parsed.text
            print "SHA512 > "+tsha.processSha512()
        elif parsed.cesar:
            tces = txtToCesarClass(parsed.text,int(raw_input("Offset : ")))
            print "TEXT > "+parsed.text
            print "CESAR > "+tces.processCesar()
        elif parsed.vigenere:
            tvig = txtToVigenereClass(parsed.text,raw_input("Key : "))
            print "TEXT > "+parsed.text
            print "VIGENERE > "+tvig.processVigenere()
    elif parsed.translate:
        md5t = md5ToTxtClass(parsed.text)
        shat = shaToTxtClass(parsed.text)
        if parsed.md5:            
            print "MD5 > "+parsed.text
            print "TEXT > "+md5t.processMd5()
        elif parsed.sha1:            
            print "SHA1 > "+parsed.text
            print "TEXT > "+shat.processSha1()
        elif parsed.sha256:
            print "SHA256 > "+parsed.text
            print "TEXT > "+shat.processSha256()
        elif parsed.sha384:
            print "SHA384 > "+parsed.text
            print "TEXT > "+shat.processSha384()
        elif parsed.sha512:
            print "SHA512 > "+parsed.text
            print "TEXT > "+shat.processSha512()
        elif parsed.cesar:
            off = int(raw_input("Offset [= -1 for all] : "))
            if off == -1:
                cest = cesarToTxtClass(parsed.text)
                allces = cest.processCesarWithoutOffset()
                print "CESAR > "+parsed.text
                index = 1
                for a in allces:
                    print "TEXT "+str(index)+" > "+str(a)
                    index += 1
            else:
                cest = cesarToTxtClass(parsed.text,off)
                print "CESAR > "+parsed.text
                print "TEXT > "+cest.processCesarWithOffset()
        elif parsed.vigenere:
            print "vigenere"
    else:
        print "Error ARGS"