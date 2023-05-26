import json


def valuer(nonvalidletters):
    Answers_value = open("WordleSolver\Answers.txt","r")
    ValidAnswers_value = Answers_value.read().split()
    Answers_value.close()
    nonvalid = []
    for i in range(0,len(ValidAnswers_value)):
        for l in ValidAnswers_value[i]:
            if l in nonvalidletters:
                nonvalid.append(i)
                break
    TotalValue_value = len(ValidAnswers_value)
    lettervalues_value = {0:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0},
                    1:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0},
                    2:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0},
                    3:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0},
                    4:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0},
                    "totalvalue":TotalValue_value}
    for i in range(0,len(ValidAnswers_value)):
        if i not in nonvalid:
            for g in range(0,5):
                lettervalues_value[g][ValidAnswers_value[i][g]] += 1
    txtlv = open("WordleSolver\LetterPlaceValuesDuring.txt","w")
    txtlv.write(str(json.dumps(lettervalues_value)))
    txtlv.close()
    


LARGEST = 0
LARGESTNUMBER = 0
PREVLET = 0
multlet = []
Answers = open("WordleSolver/Answers.txt", "r")
ValidAnswers = Answers.read().split()
Answers.close()
Guesses = open("WordleSolver/Guesses.txt", "r")
ValidGuesses = Guesses.read().split()
Guesses.close()
LetterValues: dict[str, int]
LetterValues = json.loads(
    open("WordleSolver/LetterPlaceValues.txt", "r").read())
open("WordleSolver/LetterPlaceValues.txt", "r").close()
# print(LetterValues)
LengthofAnswers = len(ValidAnswers)
AllValid = ValidAnswers + ValidGuesses
CONT = True
InWord = []
correct = []
Previous = []
j = []
ITE = 0
while CONT:
    if ITE > 0:
        correct = list(
            input("Input Correct letters in format h_l_o. Leave empty if first turn.\n"))
        # print(correct)
        if not correct:
            correct = ["_", "_", "_", "_", "_"]
        InWord = list(input("Input all other letters in word.\n"))
        NotInWord = list(input("Input What Letters Are not in the word.\n"))
    else:
        correct = ["_", "_", "_", "_", "_"]
        InWord = []
        NotInWord = []
    if ITE > 1:
        LetterValues = json.loads(
            open("WordleSolver/LetterPlaceValuesDuring.txt", "r").read())
        open("WordleSolver/LetterPlaceValuesDuring.txt", "r").close()
    WordValues = []
    for i in range(0, len(AllValid)):
        WordValues.append(0)
        if AllValid[i] not in Previous:
            LettersInWord = []
            for g in range(0, 5):
                for l in Previous:
                    j.append(l[g])
                if AllValid[i][g] in NotInWord:
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / \
                        LetterValues["totalvalue"] / 5
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif (AllValid[i][g] in j) and not AllValid[i][g] == correct[g]:
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / \
                        LetterValues["totalvalue"] / 4
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif AllValid[i][g] == correct[g]:
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / \
                        LetterValues["totalvalue"] * (2 + .2 * ITE)
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif AllValid[i][g] in InWord and correct[g] == "_":
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / \
                        LetterValues["totalvalue"] * (1.5  + .2 * ITE)
                    if AllValid[i][g] not in LettersInWord:
                        LettersInWord.append(AllValid[i][g])
                elif AllValid[i][g] not in LettersInWord:
                    LettersInWord.append(AllValid[i][g])
                    WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / \
                        LetterValues["totalvalue"]
                else:
                    # WordValues[i] += LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"] /2
                    while True:
                        if AllValid[i][PREVLET] == AllValid[i][g] and LetterValues[str(PREVLET)][AllValid[i][PREVLET]] < LetterValues[str(g)][AllValid[i][g]] and not PREVLET == g:
                            multlet.append(PREVLET)
                            if PREVLET < g:
                                PREVLET += 1
                            # WordValues[i] += (LetterValues[str(PREVLET)][AllValid[i][PREVLET]] / LetterValues["totalvalue"] / -2) + LetterValues[str(g)][AllValid[i][g]] / LetterValues["totalvalue"]
                        elif g == PREVLET:
                            for k in multlet:
                                WordValues[i] += -(LetterValues[str(k)]
                                                   [AllValid[i][k]] / LetterValues["totalvalue"] / 2)
                            WordValues[i] += LetterValues[str(
                                g)][AllValid[i][g]] / LetterValues["totalvalue"]
                            break
                        else:
                            WordValues[i] += LetterValues[str(
                                g)][AllValid[i][g]] / LetterValues["totalvalue"] / 2
                            break
                    PREVLET = 0
                    multlet = []
                j = []
        else:
            WordValues[i] = 0
        if i < LengthofAnswers:
            WordValues[i] = WordValues[i] * 1.1
    # print(WordValues)
    for i in range(0, len(WordValues)):
        if WordValues[i] > LARGESTNUMBER:
            LARGEST = i
            LARGESTNUMBER = WordValues[i]
    Previous.append(AllValid[LARGEST])
    print(AllValid[LARGEST], " which is an answer." if LARGEST <
          LengthofAnswers else "which is not an answer.")
    print(str(LARGEST), " : ", str(LARGESTNUMBER))
    LARGEST = 0
    LARGESTNUMBER = 0
    if input("x to exit").lower() == "x":
        CONT = False
    ITE += 1
    valuer(NotInWord)
