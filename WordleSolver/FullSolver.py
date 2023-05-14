import json
Largest = 0
LargestNumber = 0
prevlet = 0
multlet = []
Answers = open("WordleSolver\Answers.txt","r")
ValidAnswers = Answers.read().split()
Answers.close()
Guesses = open("WordleSolver\Guesses.txt","r")
ValidGuesses = Guesses.read().split()
Guesses.close()
LetterValues : dict[str,int]
LetterValues = json.loads(open("WordleSolver\LetterPlaceValues.txt","r").read())
open("WordleSolver\LetterPlaceValues.txt","r").close()
# print(LetterValues)
LengthofAnswers = len(ValidAnswers)
AllValid = ValidAnswers + ValidGuesses
cont = True
InWord = []
correct = []
Previous = []
j = []
while cont:
    correct = list(input("Input Correct letters in format h_l_o. Leave empty if first turn.\n"))
    print(correct)
    if correct == []:
        correct = ["_","_","_","_","_"]
    InWord = list(input("Input all other letters in word.\n"))
    NotInWord = list(input("Input What Letters Are not in the word.\n"))
    WordValues = []
    for i in range(0,len(AllValid)):
        WordValues.append(0)
        if AllValid[i] not in Previous:
            LettersInWord = []
            for g in range(0,5):
                for l in Previous:
                    j.append(l[g]) 
                if AllValid[i][g] in NotInWord:
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] / 4
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif (AllValid[i][g] in j) and not AllValid[i][g] == correct[g]:
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] / 4
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif AllValid[i][g] == correct[g]:
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] * 2
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif AllValid[i][g] in InWord and correct[g] == "_":
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] * 1.5
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif AllValid[i][g] not in LettersInWord:
                    LettersInWord.append(AllValid[i][g])
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"]
                else:
                    # WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] /2
                    while True:
                        if AllValid[i][prevlet] == AllValid[i][g] and LetterValues[str(prevlet)][AllValid[i][prevlet]] < LetterValues[str(g)][AllValid[i][g]] and not prevlet == g:
                            multlet.append(prevlet)
                            if prevlet < g:
                                prevlet+=1 
                            # WordValues[i] += (LetterValues[str(prevlet)][AllValid[i][prevlet]] / LetterValues["totalvalue"] / -2) + LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"]
                        elif g == prevlet:
                            for k in multlet:
                                WordValues[i] += -(LetterValues[str(k)][AllValid[i][k]] / LetterValues["totalvalue"] / 2)
                            WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"]
                            break 
                        else:
                            WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] /2 
                            break
                    prevlet = 0
                    multlet = []
                j = []
        else:
            WordValues[i] = 0
        if i < LengthofAnswers:
            WordValues[i] = WordValues[i] * 1.25
        
    # print(WordValues)
    for i in range(0,len(WordValues)):
        if WordValues[i]>LargestNumber:
            Largest = i
            LargestNumber = WordValues[i]
    Previous.append(AllValid[Largest])
    print(AllValid[Largest]," which is an answer." if Largest<LengthofAnswers else "which is not an answer.")
    print(str(Largest)," : ",str(LargestNumber))
    Largest = 0
    LargestNumber = 0
    if input("X to exit") == "X":
        cont = False
        
    

