# Strings in more detail _(textbook tasks)_ 
The following tasks are from pages 21 - 23 of your book.


## Converting from one case to another
### 1. From lower to upper case:
👉 To convert a string of lowercase letters to uppercase, type
the following lines:
````py
string1 = "hello"
string1 = string1.upper()
print(string1)
````


### 2.  From upper to lower case:
👉 To convert a string of upper case letters to lower case, type the following lines:
````py
string1 = "HELLO"
string1 = string1.lower()
print(string1)
````

### 3. Changing the first letter of a string to uppercase and the rest of the string to lowercase:

👉 Type these lines to capitalise the first letter of “hELLo”:

````py
string1 = "hELLo"
string1 = string1.capitalize()
print(string1)
````

What happens if the first letter of the string is already a 
capital letter? 

Note that the code uses the US English spelling _“capitalize”_
rather than the UK English spelling.

### 4. To find out the length of a string:
The `len()` function, counts the number of characters in a 
string. It returns the total number, which will always be an 
integer so the answer is of variable type `int`.

👉 Type these lines to see how it works:
````py
string1 = "Hello"
length = len(string1)
print(length)
print(type(length))
````


👉 Practise using `len()` to calculate and display the lengths of the following strings: 
````
"Never ever again!"
"Mr. McCarthy"
"5 or 6? "
"Jane-Z"
````
  