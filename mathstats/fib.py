from math import sqrt, pow, floor

def fib(index):
    a = 1
    b = 1 
    yield a
    yield b 
    for _ in range(index - 2):
        a, b = b, b + a
        yield b

def fibonacci(index):
    for _ in range(index):
        yield floor((pow((1+sqrt(5))/2, _)-pow((1-sqrt(5))/2, _))/sqrt(5))

def main():
    pass


if __name__ == "__main__":
    main()
