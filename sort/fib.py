def fib(index):
    a = 1
    b = 1 
    yield a
    yield b 
    for _ in range(index - 2):
        a, b = b, b + a
        yield b

def main():
    for i in fib(5):
        print(i)


if __name__ == "__main__":
    main()
