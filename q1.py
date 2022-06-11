# [START DEFINE FINE]
FINE_DAY = 15
FINE_MONTH = 500
FINE_YEAR  = 12000

def validated(label):
    data = input(label)
    date = data.split()
    if len(date) != 3:
        raise ValueError()
    else:        
        if int(date[0]) < 1 or int(date[0]) > 31: raise ValueError
        if int(date[1]) < 1 or int(date[1]) > 12: raise ValueError
        if int(date[2]) < 1 or int(date[2]) > 4000: raise ValueError
        return data

print('Input Format dd mm yyyy')
# [START data input]
while True:
    try:
        due = validated('Due date : ')
        actual = validated('Return date: ')
    except ValueError:
        print("This is an unaccepted input, enter a valid value")
        continue
    else:
        break


def fine_calculation():
    global due, actual

    if(due == actual):
        print('Total : 0')
    else:
        due = due.split()
        actual = actual.split()
        
        if due[2] != actual[2]:
            print('Total : '+ str(((int(actual[2]) - int(due[2])) * FINE_YEAR)))
        elif due[1] != actual[1]:
            print('Total : '+ str(((int(actual[1]) - int(due[1])) * FINE_MONTH)))
        else:
            print('Total : '+ str(((int(actual[0]) - int(due[0])) * FINE_DAY)))


fine_calculation()

