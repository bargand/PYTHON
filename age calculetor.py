#age calculetor

print("please enter your date of birth year,month and day")
num1=int(input("enter your DOB of year:  "))
num2=int(input("enter your DOB of month:  "))
num3=int(input("enter your DOB of day:  "))
print("please enter recent date of year,month and day")
num4=int(input("enter your RECENT of year:  "))
num5=int(input("enter your RECENT of month:  "))
num6=int(input("enter your RECENT of day:  "))
if num1<num4:
    print(num4-num1)
else:
    print("i could not understand")

if num2>num5:
    print(num4-num1-1)
else:
    print("i could not understand")

if num5>num2:
    print(num5-num2)
else:
    print("i could not understand")

if num3>num6:
    print(num5-num2-1)
else:
    print("i could not understand")

if num6>num3:
    print(num6-num3)
else:
    print("i could not understand")