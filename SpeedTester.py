import time
from os import system
from os.path import isfile
from runner import fsysprnt, further
def main():
    '''Interacts with the user to find what file they want to run.'''
    fsysprnt()
    path = ''
    while True:
        print("Where do you want to go / run python file.")
        inp = input()
        if isfile(('.' if path == '' else path)+inp):
            break
        path+=inp+"/"
        print(further(path,0))