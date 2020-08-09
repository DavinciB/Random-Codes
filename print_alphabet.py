import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   i+=1
   print('{} {}'.format(letter,i), end =" ")
print("\nAlphabet from A-Z:")
i = 0
for letter in string.ascii_uppercase:
   i+=1
   print('{} {}'.format(letter,i), end =" ")
