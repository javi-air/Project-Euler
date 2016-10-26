def fibonacci_sum(n):
    previous = 1
    current = 2
    total = 0

    def next_fibo(p,c):
        return (c,p+c)

    while current < 4000000:
        total += (current if not current%2 else 0)
        (previous,current) = next_fibo(previous,current)

    print(total)
