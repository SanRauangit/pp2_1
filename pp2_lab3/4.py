class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    def dist(self,other_point):
        print(((self.x-other_point.x)**2+(self.y-other_point.y)**2)**0.5)

p1=Point(1,2)
p2=Point(4,6)

p1.show()
p1.dist(p2)
p2.move(0,0)
p2.show()