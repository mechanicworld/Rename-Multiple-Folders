import os
import time
import sys
import random

os.system("cls")
# Rename multiple folders with match value
print("This is a mini program to rename multiple folder names that has same character".upper())
print("""Main purpose of this program is cut the '-min.' part of compressed image folders downloaded
from imagecompressor.com .""")

replaceTag = input("Enter replacement value (exp: -min.): ")
replaceValue = input("Enter replce (exp: . ): ")
print("All '{}' chars will replace with '{}'".format(replaceTag,replaceValue))

def renameFolder():
    ''' This program works for renaming folder'''

    #Get directory path
    while 1:
        pathLocation = input("'I want to give the path': enter 1  /  'The program is in my image folder': enter 0\nEnter Value (1/0): ")
        # You can try the imageTest folder for giving path version
        if pathLocation == "1":
            dirPath = input("""Enter the image folder path (ex: C:\\Users\\Oguz\\Desktop\\Rename-Multiple-Folders\\imageTest\\)\n!!Do not forget the add slash "//" end of the path name !!!\n Folder Path :""")
            break
        # You can run the program directly inside of the folder, this works for files at the same level of python file
        elif pathLocation == "0":
            dirPath = os.getcwd()
            break
        else:
            os.system("cls")
            print("Oops something went wrong please enter the acceptable value (1/0)".upper())
            continue

    #os.walk(path) gives us a generator object as a tuple has 3 list inside
    # lists has  (0)dirpath, (1)dirnames,(2)filenames we need filenames    
    _folderList = list(os.walk(dirPath))[0][2]
    doneMessage = "Renaming File Operation Is Done".center(80,".").upper()
    counter = 1
    print(_folderList)
    os.system("cls")

    #Folder Names
    for each in _folderList:
        # Except .py folders 
        if each[-2:] != "py":
            eachNew = each.replace(replaceTag, replaceValue)
            source = dirPath+"\\"+each
            dist = dirPath+"\\"+eachNew
            os.rename(source, dist)
            message = "{} is converted to {}".format(each,eachNew)
            
            ##This for loop works show the folder number
            message ="No {} was renamed\r".format(counter).upper()
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            counter += 1
        else:
            continue
    sys.stdout.write("\n")
    for char in doneMessage:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    return 


if __name__ == "__main__":
    renameFolder()





