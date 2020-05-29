"""
4.Encoding a string the below format to reduce the size of the string.
A string of lowercase characters in range ascii[‘a’..’z’].
We want to reduce the string to its shortest length
by doing a series of operations. In each operation
we select a pair of adjacent lowercase letters that match,
and delete them. For instance, the string aab could be shortened
to b in one operation. Now we have to delete as many characters
as possible using this method and print the resulting string.
If the final string is empty, print Empty String
"""
def remove_dups(str,ind):
    "remove two duplicate letters "
    #print (str, ind)
    print (str)
    # replace Two consecutive letters with null
    str = str.replace(str[ind], "",2)
    find_dups(str)

def find_dups(text):
    " find duplicate letters in string"
    str=text
    ln = len(str)
    ind = 0
    if ln < 4:
        print (str)
        return str
    for i in range(0,ln-1):
        if(str[i]==str[i+1]):
            ind = i
            remove_dups(str,ind)
            break
 
str = "aaabccddd"        
find_dups(str)
 
