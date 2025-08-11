import time
import string

# Includes lowercase, uppercase, digits, space and punctuation
letters = list(string.ascii_letters + string.digits + " " + string.punctuation)

# Enter the text you want to be printed
target = "Hello my name is vague"  
current_str = ""

while current_str != target:
    for letter in letters:
        print(current_str + letter)
        time.sleep(0.001) # Choose how fast you want it to go through each letter.
        if current_str + letter == target[:len(current_str) + 1]:
            current_str += letter
            break
