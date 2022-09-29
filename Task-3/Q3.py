import re
from statistics import multimode
with open("about.txt","r") as f:
    s = f.read()#Reads the entire content of the file and stores it in s
    l = s.split()#Splits the string s into individual words
    l = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in l]#Removes punctuations from each string in the list and creates a new list
    l_unique = list(set(l[:]))
    print("Words with atleast 6 letters : ")
    for i in l_unique:
        if len(i) >= 6:
            print(i)
    print("The most frequently used word : ")
    for j in multimode(l):#multimode function from statistics library returns a list of most frequent elements in a list.
        print(j," --> Frequency : ",l.count(j))
    
    
