import os


def Soldier(path, file, format):
    os.chdir(path)
    if file in os.listdir():
        os.rename(file, file.capitalize())

    else:
        return 'file not found'


path = 'd:\code\git_code\project\python_project\pretifyer'
print(os.listdir())
file = 'main.py'

f = os.listdir('d:\code\git_code\project\python_project\pretifyer')
lis = [i.split('.')[1] for i in f]
dicter = {a: lis.count(a) for a in lis}
format='py'

# for i,value in dicter.items():
#     if format==i and value>1 and file!='main.py':
#         for s in range(value):
#             os.rename(,f'{s}.{format}')
n=0
for i in f:
    print(i)
    os.rename(i,f'{n')
    n+=1
Soldier(path, 'main.py', 'py')

