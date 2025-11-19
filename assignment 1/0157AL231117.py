'''       



Name: Lakshya Mansharamani 
Enrollment NO.- 0157AL231117
Batch : MTF
Batch Time : 10:30




'''


                         # # Basic If–Else Problems:--

# Q1. Write a program to check whether a number is positive, negative, or zero. 

num=int(input("Enter the number you want to check: "))
if (num>0):
    print("Given Number is Positive.")
elif(num==0):
    print("The Given Number is zero.")    
elif(num<0):
    print("Given Number is Negative. ")
else:
    print("invalid input, Please Re-enter")


# Q2. Write a program to check whether a number is even or odd.

num=int(input("enter the number: "))
if(num%2==0):
    print('number is even')
else:
    print('number is odd')


# Q3. Write a program to check if a given year is a leap year or not. 

year=int(input("enter any year: "))
if(year%4==0 and year%100 !=0):
    print('year is leap')
elif(year%400==0):
    print('year is leap')
else:
    print('Not a leap year')



# Q4. Write a program to find the greatest of two numbers. 

num1= int(input("enter 1st number: "))
num2 =int(input("enter 2nd number: "))
if(num1>num2):
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")


# Q5. Write a program to check whether a person is eligible to vote (age >= 18).

age=int(input("enter your age: "))
if (age>=18):
    print('eligible to vote')
else:
    print('not eligible to vote')


# Q6. Write a program to check whether a given character is a vowel or consonant.

char=input('enter the character: ')
vow=['a','e','i','o','u','A','E','I','O','U']
if(char in vow):
    print('it is a vowel')
else:
    print('it is a consonant')


# Q7. Write a program to check if a number is divisible by 5.

num=int(input('enter the number: '))
if(num%5==0):
    print('divisible by 5')
else:
    print('NOT divisible by 5')


# Q8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit 
# number.

num = int(input("Enter a number: "))
if (0<=num<10 or -9<=num<=-1):
    print("It is a Single-digit number.")
elif (10<=num<100 or -99<=num<=-10):
    print("It is a Two-digit number.")
else:
    print("Number with more than two digits.")


# Q9. Write a program to check whether a student has passed or failed (passing marks = 40)

marks=int(input("enter your marks: "))
if (marks>=40):
    print('you are pass')
else:
    print('you are fail ')


# Q10. Write a program to find whether the entered number is a multiple of both 3 and 7

num=int(input("enter the number: "))
if(num%3==0 and num%7==0):
    print('given number is multiple of 3 and 7')
else:
    print('NOT a multiple of 3 and 7')


                          # # Ladder If & Nested If:--

#Q1. Write a program to find the greatest among three numbers


num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2nd number: "))
num3=int(input("enter the 3rd number: "))
if(num1>=num2  and num1>=num3):
    print(f"{num1} is greatest ")
elif(num2>=num1  and num2>=num3):
    print(f"{num2} is greatest ")
else:
    print(f"{num3} is greatest ")


# Q2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).

age=int(input('enter your age: '))
if(age<13):
    print('child')
elif(13<= age<=19):
    print('teenager')
elif(20<= age<=59):
    print('adult')
else:
    print('senior')


# Q3. Write a program to assign grades based on marks: 
# 90-100: A,  
# 75-89: B,  
# 50-74: C,  
# 35-49: D,  
# <35: Fail. 

marks=int(input('enter your marks: '))
if(marks<35):
    print('fail')
elif(35<= marks<=49):
    print('D')
elif(50<= marks<=74):
    print('C')
elif(75<= marks<=89):
    print('B')
elif(90<= marks<=100):
    print('A')
else:
    print('ENTER MARKS AGAIN (VALID)')


# Q4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
# checking whether triangle exist or not
if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b == c):
        print("Equilateral Triangle")
    elif (a == b or b == c or a == c):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("The given sides do not form a valid triangle")


# Q5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol. 

ch = input("Enter a character: ")
if len(ch) != 1:
    print("Please enter only one character!")
else:
    if ch.isupper():
        print("Uppercase Letter")
    elif ch.islower():
        print("Lowercase Letter")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special Symbol")




# Q6. Write a program to calculate electricity bill based on units: 
# Up to 100 units: ₹5 per unit, 
# 101–200 units: ₹7 per unit, 
# Above 200 units: ₹10 per unit. 

units=int(input("enter units consumed: "))
if(units<=100):
    bill=units*5
elif(101<= units<= 200):
    bill= 100*5 + (units-100)*7
else:
    bill= 100*5 + 100*7 + (units-200)*10
print(bill)



# Q7. Write a program to determine the largest of four numbers using nested if.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
if a>b:
    if a>c:
        if a>d:
            l=a
        else:
            l=d
    else:
        if c>d:
            l=c
        else:
            l=d
else:
    if b>c:
        if b>d:
            l=b
        else:
            l=d
    else:
        if c>d:
            l=c
        else:
            l=d
print("largest number is ", l)



# Q8. Write a program to check if a given year is a century year and also a leap year

year = int(input("Enter a year: "))
if year % 100 == 0:
    print(year, "is a Century Year")
else:
    print(year, "is NOT a Century Year")
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")



# Q9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), 
# Obese (30+).

wg=float(input('enter your weight: '))
if(wg<18.5):
    cat=('Underweight')
elif(18.5<= wg<=24.9):
    cat=('Normal')
elif(25<= wg<=29.9):
    cat=('Overweight')
else:
    cat=('Obese')
print('BMI IS: ', cat)



# Q10. Write a program to display the smallest number among three using nested if. 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a<b:
    if a<c:
        s=a
    else:
        s=c
else:
    if b<c:
        s=b
    else:
        s=c
print("smallest no. is :", s )






                              # # FOR LOOPS:--


# Q1. Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: 

print("Armstrong numbers between 100-999 are: ")

for num in range(100,1000):
    d1=(num//100)
    d2=(num//10)%10
    d3=(num%10)
    if((d1**3+ d2**3 + d3**3)==num):
        print(num)



# Q2. Write a program to generate and display the first n prime numbers using a for loop.

n = int(input("Enter how many prime numbers you want: "))

count = 0   
num = 2     
for num in range(2, 1000):  
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        count += 1
    
    if count == n:   
        break



# Q3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits 
# should not exceed 10. 

for num in range(1, 501):
    if num % 3 == 0:
        sum = 0
        for d in str(num):
            sum += int(d)
            
        if sum <= 10:
            print(num)



# Q4. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:

n = int(input("Enter height of pyramid: "))
for i in range(1, n+1):
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)



# Q5. Write a program to accept a string and check whether it is a pangram

s = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
pangram = True
for ch in alphabet:
    if ch not in s:
        pangram = False
        break
if pangram:
    print("String is a pangram")
else:
    print("String is not a pangram")



# Q6. Write a program using a for loop to print all twin primes between 1 and 100.

for i in range(2, 100):
    prime1 = True
    for j in range(2, i):
        if i % j == 0:
            prime1 = False
            break
    prime2 = True
    for j in range(2, i+2):
        if (i+2) % j == 0:
            prime2 = False
            break
    if prime1 and prime2 and i+2 <= 100:
        print(i,i+2)



# Q7. write a program that accepts a number from the user and prints whether it is a Harshad number

num = int(input("Enter a number : "))
s_num = str(num)

s=0
for i in s_num:
    digit = int(i)
    s+=digit

if num%s==0:
    print("Harshad number")
else:
    print("Not harshad")



#Q8. Write a program to generate Pascal’s Triangle up to n rows

num = int(input("Enter the number : "))
l=[]
for i in range(num):
    temp = []
    for j in range(i+1):
        if j==0 or j==i:
            temp.append(1)
        else:
            temp.append(l[i-1][j-1] + l[i-1][j])
    l.append(temp)

for i in range(num):
    for j in range(num-i+1):
        print(" ",end="")
    for k in range(i+1):
        print(l[i][k],end=" ")
    print()



    
#Q9. display the sum of the series: 1² + 2² + 3² + ... + n²

n = int(input("Enter number : "))
s = 0
for i in range(1,n+1):
    s+=i**2
    print(i**2," + ",end="")
print("\nTotal sum = ",s)




#Q10. WAP to check for a strong number

num = int(input("Enter number : "))
s = 0
fact=1
s_num = str(num)
for i in s_num:
    for j in range(1,int(i)+1):
        fact*=j
    s+=fact
    fact=1
print(s)
if s==num:
    print("Strong number")
else:
    print("Not strong number")
    

                              
                                                       
                    
                              
                                 # # While loop


#Q11. WAP to reverse a number and check if it is a prime

num = int(input("Enter number : "))
new_num = 0
while(num>0):
    digit = num%10
    new_num = new_num*10 + digit
    num//=10

print(f"Reverse number : {new_num}")

if new_num<2:
    print("Not prime")

else:
    flag = True
    for j in range(2, int(new_num**0.5) + 1):
        if new_num % j == 0:
            flag = False
            break
        
    if flag:
        print("Prime")
    else:
        print("Not prime")



#Q12. continously take input number until all digits's sum is : sum>100

s=0
while s<=100:
    num = int(input("Enter number : "))
    while num>0:
        digit = num%10
        s+=digit
        num//=10

print("Sum crossed 100 , sum : ",s)



#Q13. WAP to check a number is a Duck number

num = int(input("Enter a number : "))
s_num = str(num)
if s_num[0]==0:
    print("Non Duck number")
else:
    i=0
    while i < len(s_num):
        if s_num[i]=='0':
            print("Duck number")
            break
        else:
            i+=1
    else:
        print("Not a Duck number")


#Q14. WAP to check happy number

num = int(input("Enter a number : "))
visited = set()

while num!=1 and num not in visited:
    visited.add(num)
    s=0
    while num>0:
        digit = num%10
        s+=digit**2
        num//=10
    num = s

if num==1:
    print("Happy number")
else:
    print("Not a happy number")
    



#Q15. WAP to find largest prime factor of given number

num = int(input("Enter number : "))
largest = 1
i=2
while i<=num:
    if num%i==0:
        flag= True
        for j in range(2,i):
            if i%j==0:
                flag = False
                break
        if flag:
            largest = i
        
    i+=1
print(largest," is the largest prime factor")
            
            
            

#Q16. WAP to repeatedly take input a string till we get palindrome string

s = input("Enter a string : ")
rev = s[::-1]
while s!=rev:
    s = input("Enter a string : ")
    rev = s[::-1]

print("Palindrome string found : ",s)




#Q17. WAP to find sum of digits till we get a single digit

num = int(input("Enter a number : "))
while num>=10:
        s=0
        while num>0:
            digit = num%10
            s+=digit
            num//=10
        num=s
print("Single value : ",num)



#Q18. WAP to generate collartz sequence

num = int(input("Enter a number : "))
while num!=1:
    if num%2==0:
        num=int(num/2)
        print(num,end=" ")
    else:
        num=int((3*num)+1)
        print(num,end=" ")




#Q19. WAP to check keprekar number

num = int(input("Enter a number : "))
if num==1:
     print("Kaprekar number")
     
else:    
    sq=num**2
    str_sq = str(sq)
    mid = len(str_sq)//2

    l = str_sq[:mid]
    r = str_sq[mid:len(str_sq)]

    if int(l)+int(r)==num:
        print("Kaprekar number")
    else:
        print("Not a Kaprekar number")




#Q20. Write a program to simulate an ATM machine

print("1. Check balance")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Exit")

balance = int(input("Enter balance : "))

choice = input("Enter choice :")
while choice!='4':
    if choice=='1':
        print("Your balance : ",balance)
    
    elif choice=='2':
        depo = int(input("Enter amount to deposit : "))
        balance+=depo
        print("Your balance : ",balance)
    
    elif choice=='3':
        amt = int(input("Enter amount to withdraw : "))
        if amt>balance:
            print("Not enough amount")
        else:
            balance-=amt
            print("Your balance : ",balance)
    else:
        print("Enter from 1 to 4 only")
    choice = input("Enter choice :")
else:
    print("Thank you !! ")

        
        


        












































