def main():
    g = 0
    for a in range(99,10,-1):
        if a % 10 == 0:
            continue
        for b in range(99,10,-1):
            if b % 10 == 0:
                continue
            s = sum([int(d) for d in str(a**b)])
            if s > g:
                g = s
                
    return g

    
if __name__ == '__main__':
    print(main())
