'''
class library
display book donw
 lend book done
 return book done
 add book
 dict (lender name) return who has taken the book key=books value=name_of_person
 constructor ('list of book','name of library')
 addd a while loop take input from user
'''
class Lib:
    def __init__(self,books,name) -> None:
        self.books=books
        self.lname=name

    def display(self):
        print(f'Books in lib are: {self.books}')

    def book_return(self,bname):
        if bname in lb.keys():
            self.books.append(bname)
            del lb[bname]
        else:
            print('This book is not lended or doesnot belong to the lib. Plz contact admins')

    def lend (self,bname, person):
        lb[bname]=person

    def donate(self,bname):
        self.books.append(bname)

    # def return_book (self):
        

b=['s','a','h','i','l']
lb={}
Sahil=Lib(b,'Sahil Library')

while True:
    print(lb)
    print('1.Display \t 2.Return \t 3.Lend \t 4.Donate')
    feed = int(input("Enter the choice: "))

    if feed==1:
        Sahil.display()

    elif feed==2:
        bname= input('Enter the book name.')
        Sahil.book_return(bname)

    
    elif feed==3:
        bname=input('Enter book name: ')
        
        if bname in Sahil.books:
            person=input('Lender Name: ')
            Sahil.books.remove(bname)
            Sahil.lend(bname,person)

        elif bname in lb.keys():
            print(f'The book is with {lb[bname]}. It will be available soon.')

        else:
            print('Book not found!!')

    elif feed==4:
        bname=input('Enter the book u want to donate: ')
        Sahil.donate(bname)  
        print('Thanks for Donating')

    else:
        print('not valid input')


        