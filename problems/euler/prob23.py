from itertools import combinations_with_replacement
from Divisors import find_divisors
from Factorize import factorize

def main():
    abundant_numbers = []

    for i in range(1, 28124):
        if sum([n for n in find_divisors(i)]) - i > i:
            abundant_numbers.append(i)

    seive = []
    for i in combinations_with_replacement(abundant_numbers, 2):
        s = sum(i)
        if s > 28123:
            continue
        seive.append(s)

    print(sum(range(28124)) - sum(set(seive)))


if __name__ == '__main__':
    main()
