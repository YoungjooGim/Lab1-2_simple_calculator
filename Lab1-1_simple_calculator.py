# 간단한 계산기 코드의 일부 

# ******** 함수 선언 ***************
def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

# ******** 몸체 ***************

print("Select operation.")
print("1.Add")
print("2.Subtract")

# Take input from the user  
choice = input("Enter choice(1/2): ")  ##문자형으로 반환 되므로

num1 = float(input("첫번째 숫자를 입력하시오: "))  ##float 형으로 바꿔 줘야지!
num2 = float(input("두번째 숫자를 입력하시오: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1, num2))  ## 프린트 문안에 함수를...!

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

else:
    print("틀린 입력을 하였습니다")

