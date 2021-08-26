#loops and repetition

#for loop

for i in range(0,5,1): #count from 0 (inclusive) to 5 (exclusive) in steps of 1
    print(i)

#let's try to count from 0 - 100 in steps of 2
"""
for j in range(0,100,2):
    print(j)
"""
#a for loop is used to repeat something a fixed number of times

#while loop

k = 0
while k<5:
    print(k)
    #k = k+1
    k+=1 #increment

#the danger of a while loop is when the loop is never broken

#a while loop is used to repeat something until a condition is no longer met


#Let's find how many numbers from 0 - 100 are divisible by 7
nums_divisible_by_7 = 0
for l in range(1,101,1):
    if l%7 == 0: #if L divided by 7 and remainder is 0
        print(l)
        #nums_divisible_by_7 = nums_divisible_by_7 + 1
        nums_divisible_by_7+=1

print(nums_divisible_by_7, 'numbers between 1 - 100 are divisible by 7')

#Every day, Jonny eats half his cake. When will he have <0.1 of his cake remaining?

days = 1
cake_remaining = 1
while cake_remaining > 0.1:
    #cake_remaining = cake_remaining/2
    cake_remaining/=2
    days+=1

print('it takes',days,'days to eat that cake')

#Every minute, a flying rocketship doubles its distance
#The first minute, it flies 1 metre
#How long to fly to the moon? 384400000m

minutes = 1
rocket_dist = 1

while rocket_dist<384400000: #this is exponential growth
    rocket_dist*=2
    minutes+=1
    print('on minute',minutes,'we fly',rocket_dist,'metres')

print('the rocket takes',minutes,'minutes to reach the moon')






