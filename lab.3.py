import random

my_randoms=[]
for i in range (20):
    my_randoms.append(random.randrange(0,100,1))

print (my_randoms)

my_randoms.sort()

print (my_randoms)

print("Max:", max(my_randoms), "\nMin:", min(my_randoms))

def Average(my_randoms):
    return sum(my_randoms)/len(my_randoms)

print ("Average:", Average(my_randoms))