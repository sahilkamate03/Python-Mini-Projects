import datetime, time
from pygame import mixer

def play(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

print("for how much hour do u want to work")
try:
    while True:
        working_hour=int(input("enter here hour: "))
        working_min=int(input("enter here min: "))
        if working_min>60 or working_min<0 :
            print("minute is out of range.")     
        else:
            break
except:
    print("Wrong Input!!")

extension_eye=0
if working_min>=30:
    extension_eye=1

extension_ex=0
if working_min>=45:
    extension_ex=1

# reminder time set
reminder_water= working_hour
reminder_eye= (working_hour*2)+extension_eye
reminder_ex= int((working_hour*4)/3)+extension_ex

# print(reminder_eye, reminder_water, remainder_ex)
current_now=datetime.datetime.now()
current_hour=current_now.hour
current_min=current_now.minute
print(current_min)

x=y=z=0

while True:
    now=datetime.datetime.now()
    hour,min=now.hour,now.minute
    end_min=working_min+current_min
    extra=0
    if end_min>60:
        extra=1
        end_min-=60 
    end_hour=(current_hour+working_hour+extra)
    if end_hour>24:
        end_hour-=24
    # print(extra)
    # print(hour)
    # print(end_hour,end_min)

    while x<reminder_eye:
        reminder_time_eye_min=current_min+30
        extra_eye=0
        if reminder_time_eye_min>60:
            extra_eye=1
            reminder_time_eye_min-=60
        reminder_time_eye_hour=current_hour+extra_eye
        if reminder_time_eye_min==min and reminder_time_eye_hour==hour:
            reminder_time_eye_min+=30
            gain=0
            if reminder_time_eye_min>60:
                reminder_time_eye_min-=60
                gain=1
            reminder_time_eye_hour+=gain
            print("Do your eye exercise")
            play('drink.wma')
            feed=input("type yes or no:")
            if feed=="yes":
                x+=1
                mixer.music.stop()
                break
        else:
            # print("breaking eye")
            break
    
    while y<reminder_water:
        reminder_time_ex_min=current_min+45
        extra_ex=0
        if reminder_time_ex_min>60:
            extra_ex=1
            reminder_time_ex_min-=60
        reminder_time_ex_hour=current_hour+extra_ex
        if reminder_time_ex_min==min and reminder_time_ex_hour==hour:
            reminder_time_ex_min+=30
            gain=0
            if reminder_time_ex_min>60:
                reminder_time_ex_min-=60
                gain=1
            reminder_time_ex_hour+=gain
            print("Do your workout")
            play('drink.wma')
            feed=input("type yes or no:")
            if feed=="yes":
                y+=1
                mixer.music.stop()
                break
        else:
            # print("breaking ex")
            break
    
    
    while z<reminder_water:
        reminder_time_water_hour= current_hour+1
        if reminder_time_water_hour==hour:
            reminder_time_ex_hour+=1
            print("Drink water.")
            play('drink.wma')
            feed=input("type yes or no:")
            if feed=="yes":
                z+=1
                mixer.music.stop()
                break
        else:
            # print("breaking water")
            break
    
    # condition1=reminder_time_ex_hour == reminder_time_eye_hour
    # condition2=reminder_time_eye_hour == reminder_time_water_hour
    # condition3=reminder_time_ex_hour == reminder_time_water_hour
    # if reminder_time_ex_hour == reminder_time_eye_hour == reminder_time_water_hour):
