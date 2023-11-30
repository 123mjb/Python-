import json
class Solve:
    def __init__(self) -> None:
        with open("NewWordleSolver/Values.txt","r",encoding="utf-8") as f:
            self.values = json.loads(f.read())
        with open("NewWordleSolver/Answers.txt","r",encoding="utf-8") as f:
            self.words = f.read().split("\n")
        self.letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
        self.gvalues = []
        self.it = 0
        self.invalidwords=[]
        self.invalidletters=[]
        self.eachvalue=[]
    def buildguess(self):
        inpguess = input("What was the guess: ")
        inpcolours = input("What was the colours? form - cwyyw (c-correct,w-wrong,y-yellow): ")
        self.gvalues.append([inpguess,inpcolours])
    def guessmaker(self):
        self.eachvalue=[]
        for i in range(0,len(self.words)):
            value = 0
            if not self.words[i] in self.invalidwords:
                for j in range(0,5):
                    if self.words[i][j] in self.invalidletters:
                        self.eachvalue.append(0)
                        break
                    elif self.it>0 and len(self.gvalues) > 0 and self.words[i][j] in "".join([self.gvalues[p][0]for p in range(0,len(self.gvalues))]): # FIX THIS PART MICAH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        a = "".join([self.gvalues[p][0]for p in range(0,len(self.gvalues))])
                        h=""
                        for l in range(1,len(a)+1):
                            if self.words[i][j] == a[l-1]:
                                if (self.gvalues[int((l-(l%5))/5)-1][1][j] == "w" or self.gvalues[int((l-(l%5))/5)-1][1][j] == "y") and j == l % 5:
                                    h="w"
                                    break
                                elif self.gvalues[int((l-(l%5))/5)-1][1][j] == "y":
                                    h="c"
                                elif self.gvalues[int((l-(l%5))/5)-1][1][j] == "c" and j == l % 5:
                                    h = "c"
                                    break
                        if h == "w":
                            self.invalidletters.append(self.words[i][j])
                            self.invalidwords.append(self.words[i])
                            self.eachvalue.append(0)
                            break
                        elif h == "c":
                            value += self.values[str(j+1)][self.letters[self.words[i][j]] - 1]*1.1
                            if j == 4 : self.eachvalue.append(value)
                        value += self.values[str(j+1)][self.letters[self.words[i][j]] - 1]
                        if j == 4 : self.eachvalue.append(value)
                    else:
                        value += self.values[str(j+1)][self.letters[self.words[i][j]] - 1]
                        if j == 4 : self.eachvalue.append(value)
            else:
                self.eachvalue.append(0)
        maximum = 0
        for i in range(0,len(self.eachvalue)):
            if self.eachvalue[i] > self.eachvalue[maximum]: maximum = i
        print("Best guess is "+self.words[maximum]+" with a value of "+str(self.eachvalue[maximum]))
    def main(self):
        if self.it > 0:
            self.buildguess()
        self.it+=1
        self.guessmaker()
