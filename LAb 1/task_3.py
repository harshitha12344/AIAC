def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start: "))
end = int(input("Enter end: "))

primes = [i for i in range(start+1, end) if is_prime(i)]
print("Prime numbers between", start, "and", end, "are:", ','.join(map(str, primes)))
