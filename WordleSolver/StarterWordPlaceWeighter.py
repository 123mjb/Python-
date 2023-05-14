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
WordValues = []
for i in range(0,len(AllValid)):
    LettersInWord = []
    WordValues.append(0)
    for g in range(0,5):
        if AllValid[i][g] not in LettersInWord:
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
    
# print(WordValues)
for i in range(0,len(WordValues)):
    if WordValues[i]>LargestNumber:
        Largest = i
        LargestNumber = WordValues[i]
print(AllValid[Largest]," which is an answer." if Largest<LengthofAnswers else "which is not an answer.")
print(str(Largest)," : ",str(LargestNumber))
