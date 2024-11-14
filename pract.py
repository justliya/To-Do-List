#
# Convert it to uppercase.
#Remove any leading or trailing whitespace.
#Replace a word with another word of your choice.
#Split it into a list of words.

# Outputs should be:
#1. -->  'CODING TEMPLE IS THE BEST BOOTCAMP EVER!'
#2. --> 'Coding temple is the best bootcamp ever!'
#3. 'Coding temple is the greatest bootcamp ever!'
#4. ['Coding', 'temple', 'is', 'the', 'best', 'bootcamp', 'ever!']

my_string = '            Coding temple is the best bootcamp ever!      '

print(my_string.upper())
print(my_string.strip())
print(my_string.replace("ever","platform"))
print(my_string.split())