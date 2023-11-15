class Generate:
    def __init__(self) -> None:
        self.values = {
            1 : {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
            2 : {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
            3 : {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
            4 : {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
            5 : {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
        }
        self.letters = {"a":1,"b":2,"c":3,"d":4,"e":4,"f":4,"g":4,"h":4,"i":4,"j":4,"k":4,"l":4,"m":4,"n":4,"o":4,"p":4,"q":4,"r":4,"s":4,"t":4,"u":4,"v":4}
        self.allwords = [""]
    def values_create(self):
        with open("NewWordleSolver/Answers.txt","r",encoding="utf-8") as f:
            self.allwords = f.readlines()
        for i in self.allwords:
            self.individual_values(i)
    def individual_values(self,word):
        for i in range(0,len(word)):
            self.values[i][self.letters[word[i]]] += 1