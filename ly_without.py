#Catherine Hu
#CS362 HW3 Question 3
#Without error handling

#To run, type:
#   python3 ly_without.py

def main():
    yearInput = int(input("Enter a year: "))

    if yearInput % 4 == 0:
        #Divisible by 4
        if yearInput % 100 == 0:
            #Divisible by 100
            if yearInput % 400 == 0:
                #Divisible by 400
                print(yearInput, " is a leap year")
            else:
                #Not divisible by 400
                print(yearInput, " is not a leap year")
        else:
            #Not divisible by 100 = YES leap year
            print(yearInput, " is a leap year")
    else:
        #Not divisible by 4
        print(yearInput, " is not a leap year")

#Call main function
main()
