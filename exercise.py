import random
# IMPRIMIR NUMEROS PARES

# for i in range(1,101):
#     if i%2 == 0:
#         print(i)
# i = 1

# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i+=1 

#ADDITION 

# sum = 0
# for i in range (1,11):
#     while True:
#         try:
#             sumSav = int(input(f"please, write your {i} number: "))
#             break
#         except ValueError:
#             print("Invalid input. Please, enter an number")
#     sum+=sumSav
# print(f"The final total is: {sum}")    

# PALINDROME

# word = input("Please, enter a palindrome: ")
# word = word.replace(" ","").lower()
# if word == word[::-1]:
#     print(f"{word} it's a palindrome")
# else:
#     print(f"{word} it's not a palindrome")

#PRIMe

# while True:
#     try:
#         num = int(input("Please, enter a number: "))
#         if num < 2:
#             print(f"{num} is not a prime number")
#             continue
        
#         pri = True  
#         for i in range(2, num):
#             if num%i == 0:
#                 print(f"{num} is not a prime number")
#                 pri = False 
#                 break
#         if pri:
#             print(f"{num} is a prime number")
#         break
#     except ValueError:
#             print("please, enter a integer")

# # CALCULADORA SIMPLE

# while True:
#     try: 
#         num1 = int(input("please, enter a number: "))
#         num2 = int(input("please, enter a number: "))
        
#         ope = int(input("which operation do you want to do? (1 to add, 2 to substract, 3 to multiply and 4 to divide):  "))
        
#         if ope == 1:
#             tot = num1+num2
#         elif ope == 2:
#             tot = num1-num2
#         elif ope == 3:
#             tot = num1 * num2
#         elif ope == 4:
#             tot = num1/num2
#         else:
#             print("the operation is not valid. Please enter a number between 1 and 4.")
#             continue
        
#         print(f"The result is: {tot}")
        
#     except ValueError:
#         print("please, enter an intenger")
        
#     except ZeroDivisionError:
#         print("Division by zero is not allowed. Please try again.")

# NUMBER 1 TO 100

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# FIBONACCI
    # this is the correct one, it follows the fibonacci sequence 
# i, f = 1, 0 
# while f < 50:
#     print(f)
#     f, i = i, f+i 

    #este da el resultado de la secuencia, pero no sigue la lógica de fibonacci 
# i, f =1, 1 
# while f < 50:
#     print(f, i)
#     f = i+1
#     i = f+i

# factorial

# n = int(input("Please, enter a number: "))
# t = n
# while n > 1:
#     n -= 1
#     t *= n
# print(t)

# GUESS GAME 

# ranNum = random.randint(1, 100)
# n = 0
# while n != ranNum:
#     n = int(input("Please, enter a number: "))
#     if n > ranNum:
#         print("Your number is too big.")
#     elif n < ranNum:
#         print("Your number is too small.")
# print(f"your number is right: {ranNum}")

# ORDERING NUMBERS

# listNumber = []
# while True:
#     try:
#         n = int(input("how many numbers do you want to order: "))
#         for i in range(0, n):
#             number = int(input("Please enter the number: "))
#             listNumber.append(number)
#         break
#     except ValueError:
#         print("Please enter a integer.")
# listNumber.sort()
# print(listNumber)

def hola(nom):
    print(f"hola {nom}")
    return
hola("Lara Croft")


def factorial(num):
    t = num
    while num > 1:
        num -= 1
        t *= num
    return t
print(factorial(4))

def iva(total,per=21):
    facIva = (total*(per/100))+total
    return facIva
print(iva(1000))

def areCir(rad):
    pi = 3.1415
    return pi*rad**2
def areCil(rad, hig):
    return areCir(rad)*hig
print(areCil(3,5))

def mediaLista(sample):
    return sum(sample)/len(sample)
print(mediaLista([10,5,25, 40]))

def exponent(numbers):
    lastList = []
    for i in numbers:
        lastList.append(i**2)
    return lastList
print(exponent([2,4,5,6]))