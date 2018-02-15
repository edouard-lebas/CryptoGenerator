from src.txtToMd5Class import txtToMd5Class
from src.txtToShaClass import txtToShaClass

def menu():
    print "1 > MD5"
    print "2 > SHA"
    print "3 > EXIT"
    return raw_input("Choice :")

def menuSha():
    print "1 > SHA1"
    print "2 > SHA224"
    print "3 > SHA256"
    print "4 > SHA512"
    print "5 > SHA512"
    print "6 > RETURN"
    return raw_input("Choice :")

while exit != '1':
    choice = menu()
    if choice == '1':
        md5 = raw_input("Text To Md5 : ")
        m = txtToMd5Class(md5)
        print m.processMd5()
    elif choice == '2':
        choiceSha = menuSha()
        if choiceSha == '1':
            sha1 = raw_input("Text To SHA1 : ")
            s = txtToShaClass(sha1)
            print s.processSha1()
        elif choiceSha == '2':
            sha224 = raw_input("Text To SHA224 : ")
            s = txtToShaClass(sha224)
            print s.processSha224()
        elif choiceSha == '3':
            SHA256 = raw_input("Text To SHA256 : ")
            s = txtToShaClass(sha256)
            print s.processSha256()
        elif choiceSha == '4':
            SHA384 = raw_input("Text To SHA384 : ")
            s = txtToShaClass(sha384)
            print s.processSha384()
        elif choiceSha == '5':
            SHA512 = raw_input("Text To SHA512 : ")
            s = txtToShaClass(sha512)
            print s.processSha512()
        elif choiceSha == '6':
            print "Return"
        else:
            print "Choice Error"
    elif choice == '3':
        exit = '1'
        print "Exit ..."
    else:
        print "Choice Error"