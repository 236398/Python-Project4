def fibonacci_sequence():
    MAX_VALUE = 10000
    a, b = 0, 1
    print(a, end=' ')
    while b < MAX_VALUE:
        print(b, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    fibonacci_sequence()
