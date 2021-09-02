import datetime

#Lists continued

best_friends = ['Mary','Jonny','Cindy','Jonny']

#to add something to the end of a list, we use append()

best_friends.append('Mike')

print(best_friends)

#what if i wanted to add a name to the middle? we use insert()

best_friends.insert(1,'Candice')

print(best_friends)

#to remove an item, we can use remove() this removes the first instance of item

best_friends.remove('Jonny')

print(best_friends)

#We can also use the pop() method to remove the last item

best_friends.pop()

print(best_friends)

#del is to remove an item from a specific index in a list

del best_friends[1]

print(best_friends)

#clear() empties the list

best_friends.clear()

print(best_friends)

###

#FUNCTIONS - are like MyBlocks in Scratch

def greeting(): #greeting is the function name, brackets contain parameters
    print(datetime.datetime.now()) #get full time reading
    print(datetime.datetime.now().strftime("%H")) #get 24 hour 'hour' reading
    #full reference for datetime: https://www.w3schools.com/python/python_datetime.asp

    if int(datetime.datetime.now().strftime("%H")) < 12:
        print('Good morning master')
    elif int(datetime.datetime.now().strftime("%H")) < 17:
        print('Good afternoon master')
    else:
        print('Good evening master')
    
greeting()





