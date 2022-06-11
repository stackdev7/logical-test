
# [START data input]
while True:
    try:
        student = int(input('Student : '))
        if student < 1 or student > pow(10, 9): raise ValueError

        candies = int(input('Candies: '))
        if candies < 1 or candies > pow(10, 9): raise ValueError

        first   = int(input('First Student: '))
        if first < 1 or first > student: raise ValueError
    except ValueError:
        print("This is an unaccepted input, enter a valid value")
        continue
    else:
        break

def find():
    global student, candies, first

    modulus = candies % student 
    if (modulus == 0): modulus = first 
    isSourCandies = first - 1   
    for x in range(modulus):
        if isSourCandies < student:
            isSourCandies = isSourCandies + 1
        else:
            isSourCandies = 1

    print('The sour candy is student ' +str(isSourCandies))


find()