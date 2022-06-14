import hashlib
import json
import datetime
from venv import create

class Blockchain():
    
    chainLenght = 0

    def __init__(self):
        self.start = self.current = {
            "index" : self.chainLenght,
            "time"  : str(datetime.datetime.now()),
            "data"  : "Text Start : "+ input("Heading :"),
            "proof" : 1,
            "chain" : None
        }

    def createLedger(self,text):
        ledger = {
            "index" : self.chainLenght,
            "time"  : str(datetime.datetime.now()),
            "data"  : text,
            "proof" : self.createProof(),
            "chain" : None
        }
        self.current["chain"] = ledger
        self.chainLenght += 1
        self.current = ledger
        print("--Ledger Created--")
        
    
    def createProof(self):
        checkProof = True
        newProof = 1
        print("--Started Mining--")
        while checkProof:
            createHash = hashlib.sha256(
                str(newProof**2 - self.current.get("proof")**2).encode()).hexdigest()
            if createHash[:5] == "00000":
                checkProof = False
            else:
                newProof += 1
        print("--Created Proof--")
        return createHash

    def printText(self):
        readChain = self.start
        chain = True
        while chain:
            print(readChain["data"])
            if readChain["chain"] == None:
                chain = False
            else:
                readChain = readChain["chain"]
        
    def printChain(self):
        readChain = self.start
        chain = True
        while chain:
            print(readChain)
            if readChain["chain"] == None:
                chain = False
            else:
                readChain = readChain["chain"]

    def checkLedger(self):
        checker = False
        start = self.start
        while checker == False :
            if start["proof"][:5] != "00000" or start["index"] != 0:
                checker = True
        if checker:
            print("Not Valid")
        else:
            print("Valid")
            
              