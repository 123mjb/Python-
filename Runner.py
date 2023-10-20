"""For users to run a python file"""
from os import listdir
from os.path import isfile, join
def main():
    '''Interacts with the user to find what file they want to run.'''
    #print("What / where is your file")
    #file = input("What File Are You Running?")
    #onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    #onlyfolders = [f for f in listdir(".") if not isfile(join(".", f))]
    #print(onlyfiles)
    fsysprnt()
def fsysprnt():
    '''Prints the structure of the file system that the file is run in.'''
    layout = ""
    for i in listdir("."):
        if isfile(join(".",i)):
            layout += i + "\n"
        else:
            layout += i + "/\n"
            layout += further(join(".",i),1)
    print(layout)
def further(a : str,b : int):
    '''
    Create a string of a filesystem.
    
    Parameters
    ----------
    a : str
        Where the function starts.
        
    b : str
        How many layers in it is starting from.
    
    Returns
    -------
    string
        The entire filesystem from a as a string.
          
    '''
    layout = ""
    for i in listdir(a+"/"):
        if isfile(join(a+"/",i)):
            layout += ((b*3)*" ") + i + "\n"
        else:
            layout += ((b*3)*" ") + i + "/\n"
            layout += further(join(a+"/",i),1 + b)
    return layout
main()
