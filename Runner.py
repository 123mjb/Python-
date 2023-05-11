from os import listdir
from os.path import isfile, join
def main():
    file = input("What File Are You Running?")
    onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    print(onlyfiles)