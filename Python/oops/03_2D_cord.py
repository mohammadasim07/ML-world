class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5
    
class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)

    def cod_lie_on_line(self,point):
        if self.A*point.x_cod + self.B*point.y_cod + self.C == 0:
            print("co-ordinate on the line")
        else:
            print("co_ordinate is not lie on the line")

    def shortest_distance(line,point):
         return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)

#write a code to check two line are intercept or not





p5 = Line(1,1,-2)
print(p5)
p1 = Point(1,1)
p5.cod_lie_on_line(p1)
print(p5.shortest_distance(p1))
p2 = Point(5,4)
result_of_euclidean_distance = p1.euclidean_distance(p2)
print(result_of_euclidean_distance)
a = p1.distance_from_origin()
print(a)
