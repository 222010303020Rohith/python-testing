for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# prime or not
num = int(input("enter a number: "))
for i in range(2,num):
  if num % i ==0:
    print("not prime")
    break
else:
    print("prime")
