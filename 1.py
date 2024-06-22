# prime_checker.py

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    number = int(input("请输入一个正整数: "))
    if is_prime(number):
        print(f"{number} 是素数")
    else:
        print(f"{number} 不是素数")

if __name__ == "__main__":
    main()