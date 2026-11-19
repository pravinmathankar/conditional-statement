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

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a%2==0 and b%2==0:
#     print("Both numbers are even")
# elif a%2==0 or b%2==0:
#     print("At least one number is  even")
# else:
#     print("Both numbers are odd")    


# a= int(input("enter the first number:"))
# b= int(input("enter the second number:"))
# c= int(input("enter the third number:"))

# # if a+b>c and a+c>b and b+c>a:
#     # print("it is a triangle")
# if a==b==c:
#         print("it is an equilateral triangle")
# elif a==b or b==c or a==c:
#         print("it is an isosceles triangle")
# else:
#         print("it is a scalene triangle")

# marks = int(input("Enter your marks: "))

# if marks>=90:
#     print("Grade: A")
# elif marks>=80:
#     print("Grade: B")
# elif marks>=70:
#     print("Grade: C")
# elif


# number = int(input("Enter a number: "))
# a= number //100
# b = (number // 10)%10
# c= number % 10

# if number>100 and number<999:
#     if b>a and b>c:
#         print("the middle digit is the largest")
#     elif b<a and b<c:
#         print("the first digit is the smallest")
#     else:
#         print("meither the first or last digit is the largest")
# else:
#     print("invalid input")


# num = int(input("Enter a number: "))

# if num//10==0:
#     print("it is a single digit number")
# elif num//100==0:
#     print("it is a two digit number")
# else:
#     print("it is a three digit number")



# num=int(input("Enter a number: "))

# if num%7==0:
#     if num%10==7:
#         print("that number is multiple of 7 and ends with 7")
#     else:
#         print("number is multiple of 7")    
# else:
#     print("that number is not multiple of 7 and does not end with 7")        


# a= int(input("Enter first number: "))
# b= int(input("Enter second number: "))

# c= 180 - (a+b)

# if c < 180 and c >0 :
#     print("compute",c)
# else:
#     print("Invalid angle")

# num=int(input("entert the value:"))

# i=1
# if i<0:
#     print("thats not a number")
# else :
#     while i*i<=num:
#         if i*i==num:
#             print("perfect sqare value")
#             break
#         i+=1    
#     else:
#      print("not a perfect")            

# num=input("enter the input:")
# if "a"<=num<="z":
#     print("letter")
# elif  1 <=num <=9:
#     print("digit",int(num))
# else:
#     print("neigther")        

# num=input("enter the input:")
# # if len(num)==1:
# if num.isalpha():
#      print("aplphabet")
# elif num.isdigit():
#      print("digit")
# else:
#       print("special charactor")


# num=int(input("enter the input:"))

# if num%3==0:
#     print("fizz")
# elif num%5==0:
#     print("buzz")
# elif num%3==0 and num%5==0:
#     print("fizzbuzz")        
# else:
#    print("not devisable")    

# name=input("enter the input:")
# age=int(input("enter the age:"))

# print(F"my name is {name} and i am {age} year old")


# a=input ("enter the input:")

# b=float(input ("enter the input:"))
# c=input ("enter the input:")

# print(type(int(a)))
# print(type(b))
# print(type(c))

# te and print the result of the following expression:Q5
# x = 10 + 3 * 2 ** 2

# print(x)  # Output: 22

# a=input("enter the input:")
# b=float(a) * (9/5) +32
# print(b)

# a=4
# b=6
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# a=int(input("enter the first number:"))
# b=float(3.14)*(a**2)
# print(b)


# p=input("enter the input:")
# r=input("enter the input:")
# t=input("enter the input:")
# si=float(p)*float(r)*float(t)/100
# # print(si)

# a=float(input("enter the first number:"))
# integer=int(a)
# fact=float(a)-integer
# print(integer)
# print(fact)

# def fuction(a,b):
#     sum=a+b
#     return sum
# ans=fuction(3,5)
# print(ans)

#  Write a program that takes as input. Using conditional statements,
# calculate the based on these rules:
# Q1 salary
# final tax rate
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%


# salary=int(input("enter your salary:"))
# if salary<30000:
    # tax=(30000*5)/100
#     print("your salry have a tax",(30000*5)/100)
# elif 30000<=salary<70000:
#     print("you have tac of",(salary*15)/100)
# elif salary>70000:
#     print("your tax",(salary*25)/100)        
# else:
#     print("mothing")    

# def fuction(a,b):
#     for i in range (a,b):
      
    
#         if i%2==0 :
#          print(i)

# print(fuction(10,30))

# def function(a,b):

#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
# print(function(10,20))            
# def function(n):
#     while n>0:
#         digit=n%10
#         print(digit)
#         n=n//10
# n=int(input("enter the numvber:"))
# function(n)        

# def function(n):
#     count=0
#     while n>0:
#         n=n//10
#         count +=1
#         # print(count)
#     print(count)
# n=int(input("enter the input:"))
# function(n)      


# def function(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum +=digit
#         n=n//10
#     print(sum)
# n=int(input("enter the input:"))
# function(n)        

# def myfunc():
#  for i in range(100):
#     if i %3==0 and i%5==0:
#         print(i)
# myfunc()        
# while True:
#     n=input("enter the input:")
#     if n.lower()=="Quit":
#        break
#     n=int(n)
#     if n==0:
#        print("zero")
#     elif n>0:
#        print("positive")
#     else:
#        print("negative")   
# while True:
#   a=float(input("enter the input:"))
#   b=float(input("enter the input:"))
  
#   x=input("enter the input:+,-,,*,/")
  
#   if x=="+":
#       print(a+b)
#   elif x=="-":
#       print(a-b)
#   elif x=="*":
#       print(a*b)
#   elif x=="/":
#       print(a/b)
#   else:
#       print("invaid")                


# def it_prime(n):
#     if n<=1:
#         return False
#     for i in range (2,n):
#         if n%i==0:
#              print("thats not a prime number")
#     else :
#         print("it is a prime number:",i)
# n=int(input("enter the input:"))
# it_prime(n)                

# guss=10
# count=0
# for i  in range():
#  n=int(input("enter the input 1 to 100 :"))
# # for i  in range():
  
#  count +=1

#  if n>guss:
#         print("your number is a large")
#  elif n<guss:
#         print("your number is small") 
#  elif n==guss:
#         print("congratulation you find the number")
#         print("your total attempt",count)
#  else:
#         print("invalid")           

