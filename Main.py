import runner as run
import SpeedTester as ST


while True:
    print("What Are You Doing:\n- A - Running a file\n- B - Testing how long a file takes to run")
    inp = input()
    if inp in ["a","A"]:
        run.main()
    elif inp in ["b","B"]:
        ST.main()
    else:
        print("Input A or B")

    # [switcher[inp] if inp in switcher.keys else print("Input A or B")]
