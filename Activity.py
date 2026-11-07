n=4
print("====================Running points====================")

print("\nFirst place: 5 points\nSecond place: 3 points\nThird place: 2 point\nCalculatin the total")

print("1. Formula")
result=n*(n+1)//2
print("Big o -> O(1)")
print("step=1, total=",result)

total=0
print("\n2. Loop")
print("Big o -> O(n)")
steps=0
for i in range(1, n+1):
    total+=i
    steps+=1

print(f"step={steps}, total=",total)

print("\n3. Double loop")
print("Big o -> O(n**2)")
step=0
count=0
for i in range(1, n+1):
    for num in range(i, i+1):
        step+=1
        count+=num

print("steps=",step," total=",count)

print("\n\n")

lis=[1, 2, 3, 4, 5, 6, 7, 8, 9]

steps=0
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


print("\n\n")

ste=0
for i in range(1, 10):
    ste+=1
print(ste,"\n")

step=0
for x in[100, 1000, 10000]:
    for i in range(1, x+1):
        for num in range(i, i+1):
            step+=1
    print(step)


        