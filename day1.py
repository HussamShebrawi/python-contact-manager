contacts = {}
def add_contact(x, y):
    contacts[x]= y
def delete_contact(x):
    if x in contacts :
        del contacts[x]
def search_contact(x):
    if x in contacts :
        print(contacts[x])
def display_all():
    print(contacts)
while True:
    user=int(input("1. Add, 2. Delete, 3. Search, 4. View All, 5. Exit : "))
    if user==1:
        q = input("Enter name")
        w = int(input("Enter number"))
        add_contact(q, w)
    elif user==2:
        s=input("Enter name")
        delete_contact(s)
    elif user==3:
        u=input("Enter name")
        search_contact(u)
    elif user==4:
        display_all()
    elif user==5 :
        break