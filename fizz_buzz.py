def FizzBuzz(input):
#divisible by 3 and 5
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz_Buzz"

#divisible by 3
    elif input % 3 == 0:
        return "Fizz"

#divisible by 5
    elif input % 5 == 0:
        return "Buzz"
    else:    
        return (f"you entered number {input} which is not divisible by 3 or 5 try again")


print (FizzBuzz(int(input("please select a divisible number by 3 or 5: "))))