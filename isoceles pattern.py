
#using while function
def while_func(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end="")
            j = j + 1
        s = 1
        while s <= n - i:
            print(" ", end="")
            s = s + 1
        s = 1
        while s <= n - i:
            print(" ", end="")
            s = s + 1
        j = 1
        while j <= i:
            print(i - j + 1, end="")
            j = j + 1
        print()
        i = i + 1
n=int(input())
while_func(n)

