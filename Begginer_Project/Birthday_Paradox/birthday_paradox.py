import datetime
from os import times
import random
start_date=datetime.date(2022,1,1)

def getBD(numberofBD):
    date_list=[]
    for i in range(numberofBD):
        add_date = datetime.timedelta(random.randint(0,364))
        date_list.append(str(start_date+add_date))
    return date_list

# print(getBD(20))
def getMatchBD(listBD):
    match_date={i:listBD.count(i) for i in listBD}
    for t in match_date.values():    
        if t>1:
            return True
        
# print(datetime.datetime.month(1))
# def main(noOfSim,user_input):
"Percentage: {t/noOfSim*100}"
print("How many birthday should I generate?")
user_input=int(input("> "))

date_list=[]
for i in range(user_input):
    add_date = datetime.timedelta(random.randint(0,364))
    s_date=add_date+start_date
    date_list.append(s_date)


noOfSim=int(input("Number of time simulator to run: "))
s="sahil is my name"
print(s.split("",1))
# print(getMatchBD(getBD()))
# print(main(noOfSim,user_input))
# print(getBD(getMatchBD(5)))
if user_input<366:
    t=0
    for i in range(noOfSim):
        print(f"Running Simulator: {i+1}")
        if getMatchBD(getBD(user_input))==True:
            t+=1
    print(f"Percentage: {t/noOfSim*100}")
elif user_input>365:
    print("Percentage: 100.0")

# listBD=[1,1,3,4,3]
# print({i:listBD.count(i) for i in listBD})