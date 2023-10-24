import runner as run
import SpeedTester as ST

switcher = {
    "A""a": True,
    "B""b": False,
}
while True:
    print("What Are You Doing:\n- A - Running a file\n- B - Testing how long a file takes to run")
    inp = input()
    if switcher[inp]:
        run.main()
    elif not switcher[inp]:
        ST.main()
    else:
        print("Input A or B")

    # [switcher[inp] if inp in switcher.keys else print("Input A or B")]
