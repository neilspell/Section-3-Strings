# -----------------------
# Caesar Shift - Solution
# Date:
# -----------------------


### Caesar Shift - Without special characters!

import time

shift = int(input("Enter key: ")) # defining the shift count
encryption = ""
message = input("Enter message: ")

for i in range(len(message)):
  unicode = ord(message[i])                  # get decimal Unicode for each letter
  letter_index = ord(message[i]) - ord("a")  # finds the index position in alphabet (i.e. 0-25)
  new_index = (letter_index + shift) % 26    # perform the shift within range of letters
  new_unicode = new_index + ord("a")         # adds new index value onto "a" (i.e 3 + 97 = 100)
  new_message = chr(new_unicode)             # convert to new character (i.e. 100 = "d")
       
  encryption = encryption + new_message      # append to encryption string

print("Encoding... ")
time.sleep(2)
print("Encoded message: ", encryption)            # print encoded message