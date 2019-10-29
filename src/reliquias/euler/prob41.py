from isprime import isprime
from itertools import permutations


def main():
    for n in permutations('7654321',7):
        if isprime(int(''.join(n))):
            return ''.join(n)


if __name__ == '__main__':
    print(main())
