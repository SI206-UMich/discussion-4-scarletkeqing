class Rectangle():
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)
    
    def verify_input(self):
        if self.width and self.height > 0:
            return True
        else: 
            return False

    def area (self):
        self.verify_input()
        if self.verify_input() == True:
            return self.width * self.height
        else:
            return "Invalid input"
        
    def perimeter (self):
        self.verify_input()
        if self.verify_input() == True:
            return self.width + self.height + self.width + self.height
        else:
            return "Invalid input"
        
def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()