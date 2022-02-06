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
format
for i,value in dicter.items():
    if format==i and value>1:
        for s in range(value):
            os.rename(file,f'{s}.{format}')
Soldier(path, 'main.py', 'py')
