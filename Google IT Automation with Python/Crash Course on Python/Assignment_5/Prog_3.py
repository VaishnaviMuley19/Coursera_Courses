#Write a script that prints the multiples of 7 between 0 and 100.
#Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
#Remember that 0 is also a multiple of 7.
for x in range(100):
    if x % 7==0:
      print(x)
