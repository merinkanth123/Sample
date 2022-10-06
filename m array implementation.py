try:
    class array ():
        def _init_(self):
            self= []
        def insert_at_last (self, lst, val):
            l=lst
            l.append(val)
            return l
        def insert_at_start (self, lst, val):
            l=lst
            l.insert (0, val)
            return l
        def insert_at_mid (self,lst,val, index):
            l=lst
            l.insert(index, val)
            return l
        def to_pop(self, lst):
            l=lst
            l1=l.pop()
            return l1
        def to_get_min(self,lst):
            l=lst
            l1=min(l)
            return l1
        def to_get_max(self,lst):
            l=lst
            l1=max(l)
            return l1
        def to_get_length(self,lst):
            l=lst
            l1=len(l)
            return l1
        def to_reverse(self,lst):
            l=lst
            l.reverse()
            return l
    obj= array()
    lst=[]
    length=int(input("Enter the Length Of the List:"))
    print("Enter The List Elements:")
    for i in range(length):
        values=int(input())
        lst.append(values)
    x='y'
    while(x=='y'):
        print("Enter '1' for insert a value in a list at start")
        print("Enter '2' for insert a value in a list at end")
        print("Enter '3' for insert a value in a list at Your Position")
        print("Enter '4' for pop a list")
        print("Enter '6' to get a min in a list")
        print("Enter '7' to get a max in a list")
        print("Enter '8' to get a length of the list")
        print("Enter '9' to reverse a list")
        print("***********")
        choice=int(input("Enter The Choice From the Above Function:"))
        if choice==1:
            val=int(input("Enter The Value To Add:"))
            res=obj.insert_at_start(lst,val)
            print(res)
        elif choice==2:
            val=int(input("Enter The Value To Add:"))
            res=obj.insert_at_last(lst,val)
            print(res)
        elif choice==3:
            val=int(input("Enter The Value To Add:"))
            pos=int(input("Enter The Position For Adding value:"))
            res=obj.insert_at_mid(lst,val,pos)
            print(res)
        elif choice==4:
            res=obj.to_pop(lst)
            print(res)
        elif choice==5:
            res=obj.to_get_min(lst)
            print(res)
        elif choice==6:
            res=obj.to_get_max(lst)
            print(res)
        elif choice==7:
            res=obj.to_get_length(lst)
            print(res)
        elif choice==8:
            res=obj.to_reverse(lst)
            print(res)
            print("------------------------------------------------------------------------------------------")
        x=input("To Continue The Above Function Press 'y' If not press 'n':")
        print("Program Exit")
except:
    print("check your code")
