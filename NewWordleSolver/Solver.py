import json
class Solve:
    def __init__(self) -> None:
        with open("NewWordleSolver/Values.txt","w",encoding="utf-8") as f:
            self.values = json.load(f.readlines())
        self.gvalues = {}
        self.it = 0
    def buildguess(self):
        inpguess = input("What was the guess")
        inpcolours = input("What was the colours? form - cwyyw (c-correct,w-wrong,y-yellow)")
        self.gvalues += {inpguess,inpcolours}
    def main(self):
        if self.it > 0:
            self.buildguess()
        self.it+=1
