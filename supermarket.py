name=input("Enter your name: ")
address=input("Address: ")
list1='''    
            oil       95/kg
            sugar     46/kg
            maida     24/kg
            salt      12/kg
            tea       65/kg
            soap      32/piece
            onions    15/kg
            coffee    10/pack
            rice      50/kg
'''
print(list1) #prints list of items
stock={"oil":95,"sugar":46,"maida":24,"salt":12,"tea":65,"soap":32,"onions":15,"coffee":10,"rice":50}
items1=[]
quantity=[]
fprice=0
for i in range(len(stock)):
    n=input("continue shopping? press y or n: ")
    if n=="n":
        break
    elif n=="y":
        a=input("Enter item: ")
        if a in stock: #checking of given item in stock
            l=[]  #creating empty list to add quantity,price per item,final price of item
            b=int(input("Enter quantity: ")) #if stock available ask for quantity
            l.append(b)
            price=stock[a]
            l.append(price)
            rate=stock[a]*b
            l.append(rate)
            items1.append(a) #adding items to list
            quantity.append(l) #appending list to quantity(list within list)
        else:print("Out of stock")    
    else:print("Invalid input")   
         
abc=dict(zip(items1,quantity) )#lists are converted into dictionary to update duplications 

items2=list(abc.keys()) #dictionart again convereted to list for looping
quantity2=list(abc.values())

for i in range (len(quantity2)):
    fprice+=quantity2[i][2] #calculating total bill by adding last elements of list within list  
print(100*"-")
print(40*" ","WELCOME TO SUPERMARKET") 
print("Name: ",name)
print("Address: ",address)
print(100*"-")
print("sno",10*" ","Item",10*" ","Quantity",10*" ","rate",10*" ","final")
for i in range(1,len(items2)+1):
    print(i,12*" ",items2[i-1],13*" ",quantity2[i-1][0],15*" ",quantity2[i-1][1],13*" ",quantity2[i-1][2])
print()
print()
print(55*" ","Final price: ",fprice)
print()
amount=(int(input("enter the amount paid: ")))
print(55*" ","Amount paid:",amount)
if amount < fprice:
    print(55*" ","Need to pay",fprice-amount)
else:    
    print(55*" ","Balance:",amount-fprice)
print(100*"-")
print(40*" ","Thanks For Visiting")





