# break : break the loop, skip the all loop
"""
for i in range(20):
    print("5 x", (i+1), "=", 5*(i+1))
    if(i+1 == 10):
        break
    
print("End of the loop")
"""

# continue: break the iteration, skip that perticular condition
"""
for i in range(20):
    if(i+1 == 10):
        print("Skipp the iteration")
        continue
    print("5 x", (i+1), "=", 5*(i+1))
    
print("End of the loop")
"""

# do..while loop :  execute atleast once
i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break