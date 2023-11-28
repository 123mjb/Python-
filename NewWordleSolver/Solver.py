import json
class Solve:
    def __init__(self) -> None:
        with open("NewWordleSolver/Values.txt","w",encoding="utf-8") as f:
            self.values = json.load(f.readlines())
        with open("NewWordleSolver/Answers.txt","w",encoding="utf-8") as f:
            self.words = json.load(f.readlines())
        self.gvalues = {}
        self.it = 0
        self.invalidwords=[]
        self.invalidletters=[]
        self.eachvalue=[]
    def buildguess(self):
        inpguess = input("What was the guess")
        inpcolours = input("What was the colours? form - cwyyw (c-correct,w-wrong,y-yellow)")
        self.gvalues += {inpguess,inpcolours}
    def guessmaker(self):
        self.eachvalue=[]
        for i in range(0,len(self.words)):
            if not self.words[i] in self.invalidwords:
                for j in range(0,5):
                    if self.words[i][j] in self.invalidletters:
                        self.eachvalue.append(0)
                        break
                    elif self.it>0 and self.words[i][j] in self.gvalues[self.it-1][0]:
                        self.invalidletters.append(self.words[i][j])
                        self.eachvalue.append(0)
                        break
                    else:
                        self.eachvalue.append()
            else:
                self.eachvalue.append(0)
    def main(self):
        if self.it > 0:
            self.buildguess()
        self.it+=1
        self.guessmaker()
