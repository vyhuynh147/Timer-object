# Clock class
class Clock:
    # Constructor method
    # color and number is private prperties. 
    def __init__(self, timer, color):
        self.__timer = timer
        self.__color = color
    #get the number
    def get_timer(self):
        return f"Setting your {self.__timer} minute timer"
    
    #get color and its return value
    def get_color(self):
        return self.__color
    
    def set_timer(self,timer):
        self.__timer = timer
    
# create object of clock with time, number, color
c1 = Clock( 24, "black")

#print the object information
try:
    time = int(input("What time you want to set").strip().lower())

    c1.set_timer(time)
    print(c1.get_timer())
    print(c1.get_color())
except:
    print("friendly error message")