string = input("Enter your own word:")
character=input("Enter your own character:")
i=0
count=0

while(i<len(string)):
    if(string[i] == character):
        count=count+1
    i=i+1

print("The Total Amount of Times", character,"Has Occured =", count)