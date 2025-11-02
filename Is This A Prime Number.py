lower=int(input("Enter an upper range:"))
upper=int(input("Enter an lower range:"))

print("Prime Number beween",lower, "and",upper, "are:")
for num in range(lower, upper+1):

    if num>1:
        for i in range(2, num):
            if(num % 1) == 0:
                break
        else:
            print(num)
    