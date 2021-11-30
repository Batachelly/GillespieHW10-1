# File name "reconstrustSentence.py"
# Created by Joshua Gillepie 11/30/21
# this program takes to command line arguments 
# the two input arguments should be .txt files
# these files are read into the code, and then reversed and alternate words are read
# it will create an output file names "output.txt"


#f3 = open("output.txt", "w")

import sys

#if not given the right amount or arguments. print..
if len(sys.argv) != 3:
    print('Program takes two line arguments both being .txt files.')
    quit()

#reading argument 1    
inp1=sys.argv[1]#inp1=input1 aka argument 1 or text file 1
file1=open(inp1, 'r');
text1=file1.read()

#reading agrument 2
inp2=sys.argv[2]#inp2=input2 aka argument 2 or text file 2
file2=open(inp2, 'r');
text2=file2.read()

#Get the length of each input list
#printing text for file1
w1=text1.split()
length1 = len(w1)
print(' ')#new line
print('list1 is: ' +str(w1))
print(' ')#new line
print('length of list1 is: ' +str(length1))
print(' ')

#printing text for file2
w2=text2.split()
length2 = len(w2)
print('list2 is: ' +str(w2))
print(' ')#new line
print('length of list1 is: ' +str(length2))
print(' ')#new line


#find longer length file
longest1 = 0
if length2 > length1:
    longest1 = length2
else:
    longest1 = length1
    
#print to output.txt file
out = []

for k in range(0,longest1):
    if(w1 != []):
        out.append(w1.pop())
    if(w2 != []):
        out.append(w2.pop())

print "The list out is: ", out

output=open("output.txt","w")
k=0
for k in range(0,length1+length2):
    output.write(out[k])
    output.write(' ')
