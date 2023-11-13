import time
import importlib
from os.path import isfile
from runner import fsysprnt, further
def main():
    '''Interacts with the user to find what file they want to run.'''
    fsysprnt()
    path = ''
    while True:
        print("Where do you want to go / run python file.")
        inp = input()
        if isfile((path)+inp):
            break
        path+=inp+"/"
        print(further(path,0))
    start = time.time_ns()
    n = importlib.__import__(path.replace("/",".") + inp.replace(".py",""))
    print("It took " + (start- time.time_ns()) + " Nanoseconds")
main()
    