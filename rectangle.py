# 5.2 Exercise #7
# Edrich Rabanes

class Rectangle():
    def __init__(self, llength, wwidth): # initialize length and width
        self.length = llength
        self.width = wwidth
    
    def perimeter(self): # returns perimeter of rectangle
        return ((2*self.length) + (2 * self.width))

    def area(self): # returns area of rectangle
        return self.length*self.width
    
    def __str__(self): # prints length, width, perimeter, and area
        print("The length of the rectangle is: ", self.length)
        print("The width of the rectangle is: ", self.width)
        print("The perimeter of the rectangle is: ", self.perimeter())
        print("The area is of rectangle is: ", self.area())

class Parallelepiped(Rectangle): #parallelepiped is child class of rectangle
    def __init__(self, llength, wwidth, hheight):
        super().__init__(llength, wwidth) #inherits length and width from rectangle
        self.height = hheight #new variable, height, for parallelepiped class
    
    def volume(self):
        return (super().area() * self.height) #uses area() from rectangle and multiplies w/ height to give volume (v = L*W*H)
    
    def __str__(self):
        super().__str__() #prints from parent class, rectangle
        print("The volume of myParallelepiped is: ", self.volume())
        print("The height of myParallelpiped is: ", self.height)
    
    
y = Parallelepiped(7,5,2)
y.__str__()

