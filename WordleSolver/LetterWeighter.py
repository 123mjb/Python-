import json
Answers = open("WordleSolver\Answers.txt","r")
ValidAnswers = Answers.read().split()
Answers.close()
TotalValue = len(ValidAnswers) * 5
lettervalues = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,"totalvalue":TotalValue}
for i in range(0,len(ValidAnswers)):
    for g in range(0,5):
        lettervalues[ValidAnswers[i][g]] += 1
txtlv = open("WordleSolver\Lettervalues.txt","w")
txtlv.write(str(json.dumps(lettervalues)))
txtlv.close()