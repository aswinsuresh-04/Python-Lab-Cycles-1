#1. Develop a program to read a four-digit number and find its
# a. Sum of digits
# b. Reverse
# c. Difference between the product of digits at the odd position and the product of digits at the even position

#function to extract digits of the number.

def extractDigits(num):
  #extracting each digits into variables num1 to num2 respectively
  num4=num%10
  num=num//10
  num3=num%10
  num=num//10
  num2=num%10
  num=num//10
  num1=num%10
  num=num//10
  return num1,num2,num3,num4

#function to calculate the sum of digits.

def sumOfDigits(num1,num2,num3,num4):
  sum=0
  #reverse of the number stored to variable reverse
  sum=num1+num2+num3+num4
  print("The sum is  ",sum)

#function to reverse the number.
def reverseNumber(num1,num2,num3,num4):
  #reverse of the number stored to variable reverse
  reverse=(num4*1000)+(num3*100)+(num2*10)+num1
  print("The reverse is ",reverse)

#function to the compute the difference between the products.

def diffOfProductofDigits(num1,num2,num3,num4):
  #product of digits at odd positions are stored to product of odd
  productofodd=num1*num3
  #product of digits at even positions are stored to product of even
  productofeven=num2*num4
  #the difference of product of odd and even is stored to difference
  difference=productofodd-productofeven 
  print("The difference is ",difference)

num=int(input("Enter a four digit number : "))
num1,num2,num3,num4=extractDigits(num)
sumOfDigits(num1,num2,num3,num4)
diffOfProductofDigits(num1,num2,num3,num4)
reverseNumber(num1,num2,num3,num4)

# 2. Develop a program to read the three sides of two triangles and calculate the area of both. 
# Define a function to read the three sides and call it. Also, define a function to calculate the area. 
# Print the total area enclosed by both triangles and each triangle's contribution (%) towards it

#function to get the sides from the user.
def get_sides():
  a=float(input("Enter the side A :"))
  b=float(input("Enter the side B :"))
  c=float(input("Enter the side C :"))
  return a,b,c

#function to calculate the area of the triangle.
def calculate_area(a,b,c):
  s=(a+b+c)/2
  area=(s*(s-a)*(s-b)*(s-c))**(1/2)
  return area

#function to calculate the total area and % contribution of each triangle.
def totalAreaAndContribution(area_1,area_2):
#total area calculation
  total_area = area_1 + area_2
#calculating the contribution of each triangle to area
  contribution_of_triangle1 = (100*area_1)/total_area
  contribution_of_triangle2 = (100*area_2)/total_area
  print("The total area is ",total_area)
  print("The % contribution of triangle 1 to total area is ",round(contribution_of_triangle1,2),"%")
  print("The % contribution of triangle 2 to total area is ",round(contribution_of_triangle2,2),"%")
  
  print("First Triangle")
a1,b1,c1=get_sides()
area1=calculate_area(a1,b1,c1)
print("The area of first triangle is ",area1)

print("Second Triangle")
a2,b2,c2=get_sides()
area2=calculate_area(a2,b2,c2)
print("The area of second triangle is ",area2)
totalAreaAndContribution(area1,area2)

# 3. Develop a program to read the employee's name, code, and basic pay and calculate the gross salary, deduction, and net salary according to the following conditions.
# Define a function to find each of the components. Finally, generate a payslip


#function to calculate gross salary , arguements - Basic Pay , DA ,HRA , MA
def grosssalay(bp,da,hra,ma):
  grosssalary=bp+da+hra+ma
  return grosssalary

#function to calculate deduction , arguements - Pf, Pt,It
def deduction(pf,pt,it):
  deduct=pf+pt+it
  return deduct

#function - to calculate net salary , arguements : Gross Salary and Deduction
def net_salary(GS,D):
  net_sal=GS - D
  return net_sal

#function to generate the payment slip.
def generatePaymentSlip(name,code,basicpay):
#if basic pay is less than 10,000.
  if basicpay<10000:
    DA=(basicpay*5)/100
    HRA=(basicpay*2.5)/100
    MA=500
    PT=20
    PF=(basicpay*8)/100
    IT=0
    GrossSalary=grosssalay(basicpay,DA,HRA,MA)
    Deduction=deduction(PF,PT,IT)
    NetSalary=net_salary(GrossSalary,Deduction)

#if basic pay is greater than 10,000 and less than 30,000.
  elif basicpay>=10000 and basicpay<30000:
    DA=(basicpay*7.5)/100
    HRA=(basicpay*5)/100
    MA=2500
    PT=60
    PF=(basicpay*8)/100
    IT=0
    GrossSalary=grosssalay(basicpay,DA,HRA,MA)
    Deduction=deduction(PF,PT,IT)
    NetSalary=net_salary(GrossSalary,Deduction)

#if basic pay is greater than 30,000 and less than 50,000.
  elif basicpay>=30000 and basicpay<50000:
    DA=(basicpay*11)/100
    HRA=(basicpay*7.5)/100
    MA=5000
    PT=60
    PF=(basicpay*11)/100
    IT=(basicpay*11)/100
    GrossSalary=grosssalay(basicpay,DA,HRA,MA)
    Deduction=deduction(PF,PT,IT)
    NetSalary=net_salary(GrossSalary,Deduction)
 

#if the basic pay is above 50,000.
  else:
    DA=(basicpay*25)/100
    HRA=(basicpay*11)/100
    MA=7000
    PT=80
    PF=(basicpay*12)/100
    IT=(basicpay*20)/100
    GrossSalary=grosssalay(basicpay,DA,HRA,MA)
    Deduction=deduction(PF,PT,IT)
    NetSalary=net_salary(GrossSalary,Deduction)

#printing the payment slip
  print("\nPayment Slip")
  print("Employee Name : "+name)
  print("Employee Code :",code)
  print("Employee Basic Pay : Rs.",basicpay)
  print("Employee DA : Rs.",DA)
  print("Employee HRA : Rs.",HRA)
  print("Employee MA : Rs.",MA)
  print("Employee PT : Rs.",PT)
  print("Employee PF : Rs.",PF)
  print("Employee IT : Rs.",IT)
  print("Employee GrossSalary : Rs.",GrossSalary)
  print("Employee Deduction : Rs.",Deduction)
  print("Employee NetSalary : Rs.",NetSalary)

EmployeeName = input("Enter your name ")
EmployeeCode = int(input("Enter your code "))
basic_pay = int(input("Enter your basic pay "))
generatePaymentSlip(EmployeeName,EmployeeCode,basic_pay)

# 4. Develop a program to perform the following task:
#a.Define a function to check whether a number is happy or not.
#b.Define a function to print all happy numbers within a range.
#c.Define a function to print first N happy numbers.Ahappy numberis a number defined by the following process:
#•Starting with any positive integer, replace the number withthe sum of the squares of its digits.
#•Repeat the process until the number equals 1 (where it will stay), or itloops endlessly in a cyclewhich does not include 1.
#•Those numbers for which this processends in 1are happy.
# Note: if a number is not being happy after 100 iterations, consider it sad.

#function to check whether happy or sad
def happy(n):
  for i in range(1,101):
    sum=0
    while n!=0:
        digit=n%10
        square=digit**2                         
        n=n//10                         
        sum=sum+square                         
    n=sum                         
  return (sum)

#function to print the happy number within range
def happynumber(l,u):
  count=0
  for i in range(l+1,u):
    s=happy(i)
    if s==1:
      print(i,end=" ")
      count=1
  print()
  if count==0:                      
    print("There is no happy numbers between this range.")

#Function to print 'n' number of happy numbers
def printnumbers(n):
   count=1
   i=1
   while count<=n:
     total=happy(i)
     if total==1:
        print(i,end=" ")
        count+=1
     i=i+1
   print('') 

#function to invoke all above mentioned functions 
def main():
  print("\t HAPPY NUMBER FUNCTIONS")
  print("\tA number is Happy or Sad")
  num=int(input("Enter the number to check:"))
  if happy(num)==1:
    print("Its a Happy number.")
  else:
    print("Its a Sad number.")
  print("\tHappy numbers within a range.")
  lowerlimit=int(input("Enter the Lower limit:"))
  upperlimit=int(input("Enter the Upper limit:"))
  happynumber(lowerlimit,upperlimit)   
  print("\tFirst N happy numbers") 
  N=int(input("Enter the number of terms:"))
  printnumbers(N)
main()

# 5. Develop a program to read a string and perform the following operations:
#•Print all possible substrings.
#•Print all possible substrings of length K.
#•Print all possible substrings of length K with N distinct characters.
#•Print substring(s)of length maximum length with N distinct characters.
#•Print all palindrome substrings.Define function for each of the task

#function - to print all possible substrings
def sub_strings(name):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      print(s, end="\n")

#function - to print all possible substrings with length specified
def sub_strings_with_length(name,size):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      if len(s)==size:
        print(s,end=" , ")

#function - to print all possible substrings with length and no of distinct characters specified
def sub_strings_with_length_with_N_characters(name,size,N):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      if len(s)==size:
        distinct = set(s)
        if len(distinct) == N:
          print(s,end=" , ")

#function - to print all possible substrings with max length and N no of distinct characters
def sub_strings_with_max_length_with_N_characters(name,N):
  string_list = []
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      distinct = set(s)
      if len(distinct) == N:
        string_list.append(s)

  length = len(max(string_list,key = len)) 
  for i in string_list:
    if len(i)==length:
      print(i,end=" , ")

#function - to print all the paliandrome substrings
def print_paliandrome(name):
  for i in range(0,len(name)+1):
    for j in range(i+1,len(name)+1):
      s = name[i:j]
      reverse = s[::-1]
      if reverse == s:
        print(s , end = " , ")


name = input("Enter the string ")
print("All the Possible Sub Strings are")
sub_strings(name) #prints all possible sub-strings

length = int(input("\nEnter the length of the substrings you want to print "))
#prints all possible sub-strings with length specified
print("\nAll the Possible Sub Strings with length ",length," are")
sub_strings_with_length(name,length) 

num_of_distinct = int(input("\nEnter the no of distinct characters you want to print "))
#prints all possible sub-strings with length and no of distinct characters
print("\nAll the Possible Sub Strings with length ",length,"and ",num_of_distinct," distinct characters are")
sub_strings_with_length_with_N_characters(name,length,num_of_distinct)

#prints all sub-strings with max-length and no of distinct characters given
print("\nSub Strings with Max - Length and ",num_of_distinct," characters")
sub_strings_with_max_length_with_N_characters(name,num_of_distinct)

#prints all the paliandrome sub-strings
print("\nThe Paliandrome Strings are ")
print_paliandrome(name)
