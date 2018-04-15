import argparse

class ParserClass:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Crypto / Hash Translator", usage="\npython CryptoHashTranslator.py --translate --text textToTranslate --md5 \npython CryptoHashTranslator.py --generate --text textToGenerate --md5")
        self.setArguments()
    
    def generateArgs(self):
        args = []
        args.append(["--md5","Use md5",'store_true'])
        args.append(["--sha1","Use sha1",'store_true'])
        args.append(["--sha256","Use sha256",'store_true'])
        args.append(["--sha384","Use sha384",'store_true'])
        args.append(["--sha512","Use sha512",'store_true'])
        args.append(["--cesar","Use Cesar",'store_true'])
        args.append(["--vigenere","Use Vigenere",'store_true'])
        args.append(["--translate","Used to translate text to Hahs/Crypto",'store_true'])
        args.append(["--generate","Used to generate text to Hahs/Crypto",'store_true'])
        args.append(["--text","Pass the text to generate / translate"])
        return args

    def setArguments(self):
        for arg in self.generateArgs():
            if len(arg) == 3:
                self.parser.add_argument(arg[0],help=arg[1],action=arg[2])
            else:
                self.parser.add_argument(arg[0],help=arg[1])
        self.parsed = self.parser.parse_args()

    def getParsed(self):
        return self.parsed
