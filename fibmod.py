def fib(nterms):
    n1 = 0
    n2 = 1
    count = 0
    while count < nterms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
