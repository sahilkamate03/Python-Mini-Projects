def date():
     import datetime
     return datetime.datetime.now()
try:
    while True:
        ready=input("Type (y/n): ")
        if ready=="y":
            print("1.Log \t\t\t 2. Retrieve")
            type=int(input("Enter what u want to do (1/2) : "))
            print()
            print("1. s \t\t 2. a \t\t 3. h")
            name=int(input("Select the person (1/2/3): "))

            if type==2:
                print("1.Health \t\t\t 2. Diet")
                k=int(input("Enter the number: "))
                if k==1:
                    data=open(f'D:\project\Text\{name}h.txt')
                    print(data.read())
                    data.close()
                if k==2:
                    data=open(f'D:\project\Text\{name}d.txt')
                    print(data.read())
                    data.close()

            if type==1:
                print("1.Health \t\t\t 2.Diet")
                todo=int(input("Enter command(1/2) : "))
                if todo==1:
                    h=input("Enter the exercise which hv been done: ")
                    r=open(f'D:\project\Text\{name}h.txt','a')
                    r.write(str(date()))
                    r.write('\n')
                    r.write(h)
                    r.write('\n\n')
                    r.close()
                if todo==2:
                    h=input("Enter the diet : ")
                    r=open(f'D:\project\Text\{name}d.txt','a')
                    r.write(str(date()))
                    r.write('\n')
                    r.write(h)
                    r.write('\n\n')
                    r.write
                    r.close()
        if ready=="n":
            break

except:
    print('wrong input!!!!')