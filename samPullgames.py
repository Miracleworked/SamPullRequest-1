#qustion 8
import  random
name = input('Hello, what is your name?')
print('Well',name,'the integer in the range 1 to 10. You have three guesses')
number = random.randint(1,10)
guess = 0
while guess < 4:
    guess_number = int(input('Enter a number:')
    guess += 1
    if guess_number < number:
        print('Your guess is to low')
    if guess_number > number:
        print('Your guess is to high')
    if guess_number == number:
        print('Your guess is correct the number is',number)
        break
    if guess == 4:
        break
#Qustion 9

print("+----+")
for symbol in range (1,6):
    print('\   /')
    print('/   \\')
print("+----+")

#Qustion 10 
for n in range(1,6):
    print(n, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10)
#My method for getting the output:

#1 2 3 4 5 6 7 8 9 10
#2 4 6 8 10 12 14 16 18 20
#3 6 9 12 15 18 21 24 27 30
#4 8 12 16 20 24 28 32 36 40
#5 10 15 20 25 30 35 40 45 50

#Qustion 11
age = int(input("What is your age?"))

if age < (18):
    print("You are not old enough to vote")
else :
    print("You are old enough to vote")


#Qustion part 2

age = input(What is your age?")
age = int(age)
if age <= 4 
    print("Your Admission is Free")
elif age in range(5,19) :
    print("Your Admission Fee is $7.00")
else :
    print("Your Admission Fee is $12.00")

