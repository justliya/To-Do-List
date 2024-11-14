#rint all numbers from 1 to 30.
#Skip the numbers that are divisible by 3 using the continue statement.#
# 3Stop the loop if the number is greater than 25 using the break statement.

for t in range(30):
    if t %3 == 0:
        continue
    elif t > 25:
        break
    else:
     print(t)
  

