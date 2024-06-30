# star = "*"
# space = " "
# spaces = 5
# for number in range(1, 10, 2) :
#     print((space * spaces) + (star * number))
#     spaces -= 1

row = int(input("enter a number of rows :"))
star = 1

while row > 0:
    row -= 1
    print(" " * row, end="" )
    print("*" * star)
    star += 2