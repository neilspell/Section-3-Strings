# Predict & Run
_Pangram_ - A pangram is a sentence that uses every letter of the alphabet at least once. 

👉Study the program below and see if you can predict what it does? 

✍Record your prediction in your copy.

👉 Copy the code into `main.py` and run it to test your predictions.

````py
# Initialise the string 
pangram = "The quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123  position of character in string (0 - 43)

# INDEXING
print(pangram[0])
print(pangram[1])
print(pangram[2+4])    # What is this line of code doing??
print(pangram[14])
print(pangram[8])
print(pangram[43])

# The index can be any valid Python expression
pos = 17
print(pangram[pos])    # What is this line of code doing??
print(pangram[pos+1])  # What is this line of code doing??

# A general pattern used to find the last character

print( pangram[len(pangram)-1] )  # What is this line of code doing??
````

## 💡 Common Mistakes
It is worth pointing out a couple of very common pitfalls relating to strings and index numbers.

The first thing to note is that strings are **_immutable._** 

This means that once a string has been initialised it cannot be changed. For this reason, it is not permitted to use the index operator `[ ]` on the left hand side of an assignment statement. 

For example, the string `"Cavan"` could not be changed to `"Navan"` as follows:
````py
town = "Cavan"
town[0] = "N"
````
👉 Try for yourself and see what happens!

To ‘change’ the value of town to Navan the program needs to make a new assignment `town = "Navan"` but be warned that the reference to the original string "Cavan" is now lost.

Secondly, if a program attempted to access a character in a string using an index that is too big (i.e. beyond the last character) for that string; Python returns a runtime error telling you that the index is out of range. 

For example, running the following code snippet would result in a runtime error being displayed because the index 5 is beyond the range of the string.

````py
s = "Hello"
print(s[5])
````
👉 Try for yourself and see what happens!