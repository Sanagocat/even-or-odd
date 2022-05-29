#Problem
#Write program to find whether a given number (accept from the user) is even or odd
#print out an appropriate message to the user
#modulo --> %

#num -> even? odd?
#number % 2 --> = 1 odd
#number % 2 --> = 0 even

#if(number%2 == 0):
#  Even
#elif(number%2 == 1):
#  Odd

NUMBER=int(input("NUmber? : "))
if NUMBER%2==1:
  print('Number is odd')
elif NUMBER%2==0:
  print("number is even")
else: 
  print ("NUMBER IS BIGGER THAN 10 OR UNDER 0")







