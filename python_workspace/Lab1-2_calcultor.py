# Program makes a simple calculator

# ******** Function Declaration ***************
def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# ******** Body *******************
while True:                          ## 같은 코드를 반복해서 실행하려면 기본적으로 while True는 고려해볼것!
    print("==================")
    print("Select operation.")
    print("0.Exit")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

# Take input from the user  
    choice = input("Enter choice(0/1/2/3/4): ")
    if choice == '0':
        break
    if (choice < '0') or (choice > '4'): ##??이게 모든 예외를 포함함...? 어뜨케....?
        print("Invalid input")     ##오류 를 범했을 경우 루프 맨위로 올라 갈 수 있는 방법
        continue
                                    ## 고로 num1, num2를 입력하고 오류가 발생하는 일이 없다!
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
       print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
         print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
         print(num1,"*",num2,"=", multiply(num1,num2))

    else:
         print(num1,"/",num2,"=", divide(num1,num2))

