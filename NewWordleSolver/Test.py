# from LetterAndPlaceWeighter import Generate as a
# a("NewWordleSolver/Answers.txt","NewWordleSolver/Values.txt").main()
with open("NewWordleSolver/Answers.txt","r",encoding="utf-8") as f:
    words = f.read().split("\n")
print(words)