import random
import datetime
month=[]
day=[]
months = [0,'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# nd=int(input('Enter the no of random dates:'))
c=0
def get_dates():
    while len(month)<23:
        try:
            a=datetime.date(2022, random.randint(1,12),random.randint(1,31))
            month.append(a.month)
            day.append(a.day)
        except:
            pass
    return day
    

while c<10:
    day=get_dates()
    print(day)
    data=[]
    print(c)
    c+=1
    
    # for i in month:
    #     d=months[i]+' '+str(day[i])
    #     data.append(d)
    # # print(data)

    # dictre={i:data.count(i) for i in data}
    # # print(dictre)
    # sum=0
    # for x, y in dictre.items():
    #     if dictre[x]!=1:
    #         sum+=dictre[x]
    # print()
    # # print(s)
    # print(dictre)
    # print('sum: ',sum)
    # final=[]
    # final.append(sum)
    # print(final)
    # print('appended')
    # c+=1
# print(final)


# # number=int(input('Enter the number of '))
# standard_input = '23'

# count=0