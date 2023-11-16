class Generate:
    def __init__(self,words,valueprint) -> None:
        self.words = words
        self.valueprint = valueprint
        self.values = {
            1 : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            2 : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            3 : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            4 : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            5 : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        }
        self.letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
        self.allwords = [""]
    def values_create(self):
        with open(self.words,"r",encoding="utf-8") as f:
            self.allwords = f.read().split()
            print(len(self.allwords))
        for i in self.allwords:
            self.individual_values(i)
    def individual_values(self,word : str):
        for i in range(0,len(word)):
            self.values[i+1][self.letters[word[i]]-1] += 1
    def printtofile(self):
        with open(self.valueprint,"w",encoding="utf-8") as f:
            f.write(str(self.values))
    def main(self):
        self.values_create()
        self.printtofile()
