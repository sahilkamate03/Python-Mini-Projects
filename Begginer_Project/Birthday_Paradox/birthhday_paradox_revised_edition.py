import datetime, random
import enum

# Date generator function
def getBirthdays(numberOfBirthday):

    birthdays=[]
    for i in range(numberOfBirthday):
        startOfYear=datetime.date(2022,1,1)
        randomNumberofDays=datetime.timedelta(random.randint(0,364))
        birthday=startOfYear+randomNumberofDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA==birthdayB:
                return birthdayA
print(getMatch(getBirthdays(100)))
exit()
MONTHS=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# print(MONTHS)
print("sahil".isdecimal())
# while True:
#     print("How many Bdays you want to generate?")
#     response=int(input('> '))
#     if response.isdecimal()