if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("weird")
    elif n in range(2,6):
        print("not weird")
    elif n in range(6,21):
        print("weird")
    elif n > 20:
        print("not weird")