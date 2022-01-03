dic = {'a':123,'b':4454}
# for i in range(2):
#         keys = input('Enter the name of Employee:')
#         values = int(input('Enter the Phone number of Employee:'))
#         dic[keys] = values
# print(dic)
# search = input('Enter the  Name of Employee you want to be search phone number: ')

def funtion(search):
    if search in dic:
        return dic[search]
    else:
        return 'Does not exist!!'

a = funtion(input('Enter the  Name of Employee you want to be search phone number: '))
print(a)
