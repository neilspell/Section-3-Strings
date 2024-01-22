# String Slicing
So far we have used indexing to access individual characters from a string. The technique of indexing can also be used to extract a sub-string from a string. This is known as slicing. 
The part of the string that is extracted is known as the slice (i.e. sub-string). 

Slicing is useful when we want to extract a specific piece of information out of a longer piece of information. For example, we may want to extract a share price from a web page displaying stocks.

In order to extract a slice from a string we need to know the indices of the desired slice’s start and end positions. The slice is taken by specifying these values inside the square brackets. The values are separated by a full colon.

The technique of slicing is demonstrated by the following short program:
````py
# Initialise the string 
pangram = "The quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123  

# Extract from index 1 up to but NOT including index 5
print(pangram[1:5]) # "he q"

# Extract from index 17 up to but NOT including index 19
print(pangram[17:19]) # ox

print(pangram[:19])   # "The quick brown fox"
print(pangram[20:26]) # "jumps"
print(pangram[26:])   # "over the lazy dog!"
````
The colon `:` delimits the start and end positions of the slice we are interested in extracting. 

The resulting slice runs from the starting index **_up to, but not including_** the end. If the start is missing it is taken to be zero i.e. the first character of the string. If end is missing it is taken as the index of the last character in the string. 

👉 What do you think the statement `print(pangram[:])` would display?

