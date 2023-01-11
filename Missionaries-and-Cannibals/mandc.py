source=['M','M','M','C','C','C']

boat=[]
dest=[]
print("\nStarting from Source \nSource:",source,"Boat:",boat,"Destination:",dest)

def check(space):
    countm,countc=0,0
    for i in space:
        if(i=='M'):
            countm=countm+1
        else:
            countc=countc+1
    if(countm<countc and countm!=0):
        if countm+1==countc:
            return 1
        else: return 2
    else:
        return False

while(len(source)):
    for i in range(2-len(boat)):
        boat.insert(i,source.pop())
        if(check(source)):
            source.append(boat.pop(boat.index('M')))
            boat.append(source.pop(source.index('C')))
    print("------->")
    print("Source:",source,"Boat:",boat,"Destination:",dest)

    for i in range(2):
        dest.append(boat.pop())

    if(check(dest)==2):
        boat.append(dest.pop(dest.index('M')))
    elif(len(source)==0):
        break
    else:
        boat.append(dest.pop(dest.index('C')))
    print("<-------")
    print("Source:",source,"Boat:",boat,"Destination:",dest)

print("\nReached Destination: \nSource:",source,"Boat:",boat,"Destination:",dest)
