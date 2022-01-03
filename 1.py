dic = dict()
def funtion():
    for i in range(2):
        keys = input('Enter the name of Employee:')
        values = int(input('Enter the Phone number of Employee:'))
        dic[keys] = values
    print(dic)
    search = input('Enter the  Name of Employee you want to be search phone number: ')
    if search in dic:
        print('Employee phone number:',dic[search])
    else:
        print('Does not exist!!')

funtion()
