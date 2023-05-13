import json
Largest = 0
LargestNumber = 0
Answers = open("WordleSolver\Answers.txt","r")
ValidAnswers = Answers.read().split()
Answers.close()
Guesses = open("WordleSolver\Guesses.txt","r")
ValidGuesses = Guesses.read().split()
Guesses.close()
LetterValues : dict[str,int]
LetterValues = json.loads(open("WordleSolver\LetterValues.txt","r").read())
open("WordleSolver\LetterValues.txt","r").close()
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
            WordValues[i] += LetterValues[AllValid[i][g]] / LetterValues["totalvalue"]
        else:
            WordValues[i] += LetterValues[AllValid[i][g]] / LetterValues["totalvalue"] / 2
# print(WordValues)
for i in range(0,len(WordValues)):
    if WordValues[i]>LargestNumber:
        Largest = i
        LargestNumber = WordValues[i]
print(AllValid[Largest]," which is an answer." if Largest<LengthofAnswers else "which is not an answer.")
print(str(Largest)," : ",str(LargestNumber))
