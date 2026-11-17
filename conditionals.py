# age = 30 
# if age >= 18:
#     print("you are got a man")
# else:
#     print("you are a child")    



# num = int(input("enter the n :"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("zero")



# num = int(input("enter the n :"))
# if num%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by")

# age = 25
# has_id= True

# if age >=18 and has_id:
#     print("you are eligible to vote")
# else: 
#     print("you are denied")


# num =int(input("write the input"))

# if num%3==0  and num%5==0:
#     print("divisible by 3 and 2")
# else:
#     print("not divisible by 3 and 5")

# year =int(input("enter the year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")


# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# # print(max(a,b))

# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# c= int(input("enter the third number:"))

# if a>=b and a>=c:
#     print("a is greater than b and c")
# elif b>=a and b>=c:
#     print("b is greater than a and c")
# else:
#     print("c is greater than a and b")


# temperature = int(input("enter the temperature:"))
# if temperature<=15:
#     print("it is cold")
# elif temperature>15 and temperature<=30:
#     print("it is warm")
# else:
#     print("it is hot")


# print ("a" in "abstaction")


# ch=input("enter the input:")
# if ch=="a" in ch=="e" in ch=="i" in ch=="o" in ch=="u":
# # if ch in "aiuoe":    
#     print("it is vowel")
# else :
#     print("consenent")    



# ch = input("Enter a character: ").lower()

# if ch in "aeiou":
#     print("Vowel")
# elif "a" <= ch <= "z":
#     print("Consonant")
# else:
#     print("Not a letter")


# ch = input("Enter a character: ").lower()
# if ch in "aeiou":
#     print("vovel")
# elif ch in "&%#$@":
#     print("special character")    
# elif "a" <=ch <="z":
#     print("consenet")
# else:
#     print("not a latterh")        


# ch=input("enter the input:")
# if any (ch in "aeiou" for ch in ch):

#     print("vovel")
# else:
#     print("not a consenent")    

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))

# if a+b>c and a+c>b and b+c>a:
#     print("it is a triangle")
# elif a+b<c or a+c<b or b+c<a:
#     print("it is not a triangle")
# else:
#     print("it is not a triangle")
  
  
# ch=input("enter the first number:").lower()       


# if "a"<=ch <="m":
#      print("the letter is in the first half of the alphabet")
# elif "n"<=ch <="z":
#     print("the letter is in the second half of the alphabet")      
# else:
#     print("it is not a letter")  
# 
#   
# n=int(input("enter the rowa:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# age =20 
# has_id = True
# if age >=18:
#     if has_id:
#         print("entry allowed")
#     else:
#         print("show id")    
# else:    
#     print("you are not eligible to vote")

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print("it is an equilateral triangle")
#     elif a==b or b==c or a==c:
#         print("it is an isosceles triangle")
#     else:
#         print("it is a scalene triangle")
# else:
#     print("it is not a triangle")        


# num=int(input("enter the number:"))
# if num<0 or num>23:
#     print("invalid input")
# if num>=0 and 12>=num:
#     print("good morning")

# elif num>12 and 16>=num:
#     print("good afternoon")
# elif num>16 and 23>=num:
#     print("good evening")
# else:
#     print("invalid input")



# age=int(input("enter the age:"))
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")    

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a == 0 or b == 0:
#     print("Zero can't be checked this way")
# elif a % b == 0 or b % a == 0:
#     print("One number is a multiple of the other")
# else:
#     print("Neither is a multiple of the other")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a%2==0 and b%2==0:
    print("Both numbers are even")
elif a%2==0 or b%2==0:
    print("At least one number is  even")
else:
    print("Both numbers are odd")    