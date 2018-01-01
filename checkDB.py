# -*- coding: utf-8 -*-

def verifyID(id,array):
     name="Unknown"
     for x in range(0,len(array)):
         if(array[x]==id):
                 name=array[x+1]
     return name

def copyToTextFile(id):
    with open("db/students.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return verifyID(id,content)