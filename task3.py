def fact(n):
    if n < 2:
        return 1
    else:
        return fact (n-1) * n

def Fib(n):
    if n <=1:
        return n
    else:
        return Fib(n-1)+Fib(n-2)

print('Enter what you whant to do: \nTo calculate the factorial of a number -- Fact \n Find the fibonacci number -- Fib')
move = input()
if move == "Fib":
    print('Enter your number')
    n = int(input())
    print(Fib(n))
elif move == 'Fact':
    print('Enter your number')
    n = int(input())
    print(fact(n))
else:
    print('Invalid command')