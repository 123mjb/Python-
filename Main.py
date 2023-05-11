from Runner import main as run
from SpeedTester import main as test

switcher = {
    "A":True,
    "B""b":False,
}
while True:
    print("What Are You Doing:\n- A - Running a file\n- B - Testing how long a file takes to run")
    inp = input()
    if inp in switcher.keys() and switcher[inp]:
        run()
    elif inp in switcher.keys():
        test()
    else:
        print("Input A or B")
    
    # [switcher[inp] if inp in switcher.keys else print("Input A or B")]