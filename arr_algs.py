def minMass(mass):
    min = mass[0]
    for i in range(len(mass)):
        if mass[i] < min:
            min = mass[i]
    return min

def sredMass(mass):
    sum = 0
    for i in range(len(mass)):
        sum += mass[i]
    return(sum / len(mass))



mass = [1,2,3,-5]
print(minMass(mass))
print(sredMass(mass))
