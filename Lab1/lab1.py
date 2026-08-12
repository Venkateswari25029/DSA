#program1:
num = int(input("Enter the number: "))
def launch():
    i = 10
    while(num <= i):
        print(i)
        i = i - 1
    print("Rocket launched")
launch()
#program2:
p = float(input("Enter principal growth factor: "))
n = int(input("Enter number of years: "))
def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)
result = power(p, n)
print("Power =", result)
#program3:
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter the number: "))
print(fib(n))
#program4:
def search_employee(emp_list, emp_id, index=0):
    if index == len(emp_list):
        return False
    if emp_list[index] == emp_id:
        return True
    return search_employee(emp_list, emp_id, index + 1)

employees = [101, 102, 103, 104, 105]

emp_id = int(input("Enter Employee ID to search: "))

if search_employee(employees, emp_id):
    print("Employee ID found.")
else:
    print("Employee ID not found.")

#program5:
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter the number:"))
print(fact(n))









































    
