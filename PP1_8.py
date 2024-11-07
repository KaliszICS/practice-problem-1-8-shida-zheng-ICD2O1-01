
def q1():  
  #Write Assignment code here
  bool1 = "True"
  bool2 = "False"
  print(bool1 and bool2)
  print(bool1 or bool2)
def q2():
  #Write Assignment code here
  num = int(input("Enter an integer: "))
  if num == 0:
    print("False")
  
  else:
    print("True")
def q3():
  #Write Assignment code here
  num = float(input("Enter a number: "))
  if 0 <= num <= 10:
    print("True")
  else:
    print("False")
def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink: ")
  if food == "pizza" and drink == "pop":
    print("False")
  else:
    print("True")
def q5():
  #Write Assignment code here
  num = int(input("Enter an integer: "))
  if num % 2 == 0: 
    print(f"The integer {num} is True.")
  else:
    print(f"The integer {num} is False.")
#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()



