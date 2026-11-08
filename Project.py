lis=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Quiz steps")
print("\n\nLowest: 1\n2. Average: 5\nBiggest: 10")

steps=0
print("\nBig Omega: (1)")
for i in lis:
    if i==1:
        steps+=1
print(steps) 

step=0
print("\nBig Theta: (5)")
for i in lis:
    if i==5:
        print(step)
    else:
        step+=1

ste=0
print("\nBig O: (10)")
for i in lis:
    if i==10:
        print(ste)
    else:
        ste+=1


while True:
    num=int(input("Enter a number from one to 9: "))
    if num in lis:
        for number in lis:
            if number==num:
                steps=steps

            else:
                steps+=1

        break
    else:
        continue

print(steps)