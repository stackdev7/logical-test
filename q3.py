
# [START data input]
while True:
    try:
        length = int(input('Length array : '))
        if length > pow(10, 5): raise ValueError

        array = input('Array list: ')        
        if len(array.split()) > length: raise ValueError

    except ValueError:
        print("This is an unaccepted input, enter a valid value")
        continue
    else:
        break

def solve_problem():
    global length, array

    array = array.split()
    middle = int(len(array)/2)
    left = sum(map(int, array[0:middle]))
    right= sum(map(int, array[middle+1:]))
    print('YES') if(left == right) else print('NO')
    print(str(left) + ' - '+ str(right))

solve_problem()