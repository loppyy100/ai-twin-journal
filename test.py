nums = (1,2,3,4,5,6,7,8,9,10,11,12,12,14,15)


for n in range(1, 16):
    if n % 3== 0 and n % 5 == 0:
       print("fizzbuzz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizz")
    else:
        print(n)
                    