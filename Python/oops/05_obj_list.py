class person:
    counter = 0
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        person.counter = person.counter + 1


p1 = person('asim','male')
print(p1.counter)
p2 = person('saqib','male')
print(p2.counter)
p3 = person('tariq', 'male')

L = [p1,p2,p3]

print(L)  # it gives address of three objects


for i in L:
    print(i.name,i.gender)