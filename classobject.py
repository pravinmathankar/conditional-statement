# class dog:
#     sound="bark"
# dog1=dog()
# print(dog1.sound)

# class dog:
#     species="chanie"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# dog1=dog("muku",3)
# print(dog1.name)
# print(dog1.species)



# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name} is {self.age} year old"
# dog1=dog("bobby",3)
# dog2=dog("tommy",2)
# print(dog1)
# print(dog2)



# class car:
#     def __init__(self,name,age,sername):
#         self.name=name
#         self.sername=sername
#         self.age=age
#     def names(self):
#         return f"my {self.name} and i am {self.age} and my sername {self.sername}"
     
# car1=car("pravin",22,"mathankar")
# car2=car("pravin",22,"sharma")
# print(car1.names())
# print(car2.names())

# class gfg:
#     def __init__(self, topic):
#         self._topic = topic  # Store parameter value in instance variable

#     def topic(self):
#         print("Topic:", self._topic)  # Access the renamed variable

# # Creating an instance of gfg
# ins = gfg("Python")

# # Calling the topic method
# ins.topic()

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")


# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.sound()

# class animal:
#     def __init__(self,name):
#         self.name=name
#     def info(self):
#         print("animal name:",self.name)

# class dog (animal):
#     def sound(self):
#         print(self.name,"barks")

# d=dog("bobby")

# d.info()
# d.sound()]


# class animal:
#     def __init__(self,name):
#         self.name=name

#     def info(self):
#         print( f"animal name:{self.name}")

# class dog(animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed

#     def details(self):
#         print(self.name, "is a ",self.breed)

# d=dog("bobby","golden retriever")

# d.info()
# d.details()


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

#     def move(self):
#         return "Moving"

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# dog = Dog()
# print(dog.move())
# x=501
# number=0
# for i in range (x):
#     if i%5==0 and i%7==0:
#         number=x
#         print("print that number is divided for both" ,number)
#     else:
#         print("not")
# count=0
# for i in range(501):
   
#     if i %5==0 and i%7==0:
#         count+=1
#         print(i)
#         print(count)

# for i in range(1, 101):
#     num = i
#     total = 0

#     while num > 0:
#         digit = num % 10
#         total += digit
#         num //= 10

#     if total % 2 == 0:
#         print(i)


# class student:

#     name="pravin"
#     roll=88
#     subject="python"

# a1=student()
# print(a1.name,a1.roll,a1.subject)


# class studnet:
#     def __init__(self,name):
#         self.name=name
        

# a1=studnet("pravin")
# a2=studnet("mahendra")
# a3=studnet("akshy")

# print(a1.name)
# print(a2.name)
# print(a3.name)



# class student:
#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
#     def cg_pa(self):
#         return self.cgpa


# stu1=student("rahul",99)
# stu2=student("pravi",91)
# stu3=student("mahima",96)

# print(stu1.cg_pa(),stu1.name)


# class student:
#     collage_name="apc apna collage"
#     pi=3.444

#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         self.pi=3.2

# stu1=student("rahul",9.2)
# print(stu1.name ,stu1.gpa)
# print(student.collage_name)
# print(stu1.collage_name)
# print(stu1.pi)

# class laptop:
#     storage_type="ssd"
#     def __init__(self,ram,storage):
#         self.ram=ram
#         self.storage=storage
#     @classmethod
#     def get_storage(cls):
#         print(f"storage type={cls.storage_type}")

#     def get_info(self):
#         print(f"laptop has a {self.ram} ram {self.storage}{self.storage_type}")


# l1=laptop("16gb","512")
# # l2=laptop("8gb","256gb")

# # l1.get_info()
# # l2.get_info()

# l1.get_storage()

class product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count+=1
    def get_info(self):
        print(f"price of{ self.name} is rs {self.price}")

    @classmethod

    def get_count(cls):
        print(f"total product in store={cls.count}")


@staticmethod
def cal_discount(price,discount):
    print(f"dicount={price-(price*discount)/100}")

    
p1=product("phone",20_000)
p2=product("laptop",50_000)
p3=product("pen",10)


product.get_count()
# print(p1.get_info())

s1=cal_discount(10000,10)
# print(s1.cal_discount())