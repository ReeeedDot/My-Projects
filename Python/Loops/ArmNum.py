num= int(input("Enter a nnumber: "))
sum_of_power=0
temp=num
digits = len(str(num))

while temp> 0:
    digit = temp% 10
    sum_of_power += digit ** digits
    temp //=10

if sum_of_power ==num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is NOT an armstrong number")