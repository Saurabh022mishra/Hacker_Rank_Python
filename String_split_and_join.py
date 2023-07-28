"""Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words."""


def split_and_join(line):
    w=[]
    a=0
    for i in line:
        w.append(i)
    for i in w:
        a=a+1
        if(i==" "):
            w[a-1]="-"
    return ''.join(w)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)