num = int(input("Enter a number: "))
s = 0
n = num
while n > 0:
   k = n % 10
   s += k ** 3
   n //= 10
print(s)
if s==num:
    print("it is amstrong number")
else:
    print("not an amstrong")