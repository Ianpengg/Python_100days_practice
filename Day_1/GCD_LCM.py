def main():

    def gcd(m, n):
        (m, n) = (n, m) if n > m else (m, n)
        for factor in range (m, 0, -1):
            #print(factor)
            if m % factor == 0 and n % factor == 0:
                return factor
    def lcm(m, n):
        output = int(m * n / gcd(m, n))
        return output
    m = int(input('m = '))
    n = int(input('n = '))

    print(gcd(m, n))
    print(lcm(m, n))




if __name__ == '__main__':
    main()