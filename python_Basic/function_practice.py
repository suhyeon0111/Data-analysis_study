# 재귀함수
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

    
print(factorial(int(input("Input Number for Factorial Caculation!"))))


# 함수의 인수
'''
키워드 인수: 함수의 인터페이스에 지정된 변수명을 사용하여 함수의 인수를 지정하는 방법
디폴트 인수: 별도의 인수값이 입력되지 않을 때, 인터페이스 선언에서 지정한 초깃값을 사용하는 방법
가변 인수: 함수의 인터페이스에 지정도니 변수 이외의 추가변수를 함수에 입력할 수 있게 지원하는 방법
키워드 가변 인수: 매개변수의 이름을 따로 지정하지 않고 입력하는 방법
'''

def keyword_argument(myname, yourname):
    print("hello {0}, my name is {1}".format(yourname, myname))


keyword_argument("suhyeon", "su")
keyword_argument(yourname="suhyeon", myname="su")
# hello su, my name is suhyeon
# hello suhyeon, my name is su


def default_argument(myname, yourname = "suhyeon"):
    print("hello {0}, my name is {1}".format(yourname, myname))


default_argument("su", "coffie")
default_argument("su")
# hello coffie, my name is su
# hello suhyeon, my name is su


def varibale_length_argument(a, b, *args):
    return a + b + sum(args)


print(varibale_length_argument(1,2,3,4,5))
# 15


def varibale_length_argument2(*args):
    x, y, *z = args
    return x, y, z


print(varibale_length_argument2(3,4,5,6,7,8))
# (3, 4, [5, 6, 7, 8])

def ketword_varibale_length_argument(**kwargs):
    print(kwargs)
    print("frist value is {first}".format(**kwargs))
    print("secod value is {second}".format(**kwargs))
    print("third value is {third}".format(**kwargs))


ketword_varibale_length_argument(first = 3, second = 4, third = 5)
