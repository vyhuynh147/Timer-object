# Clock class
class Clock:
    # Constructor method
    # color and number is private prperties. 
    def __init__(self, time, number, color):
        self.time = time
        self.__number = number
        self.__color = color
    #get the number
    def get_number(self):
        return self.__number
    
    #get color and its return value
    def get_color(self):
        return self.__color
    
    def set_Alarm(self):
        self.time +=1
        print("Clock stopped and alarm is set.")

    def ringer(self):
        print(f"The bell ringer has {self.__color} color.")
        print(f"Clock time is {self.time} hours.")


#string 
    def __str__(self):
        return f" Clock number is {self.__number}, color of bell ring is {self.__color}. And the total hours of clock is {self.time} hours."

# create object of clock with time, number, color
c1 = Clock( 24 , 12 , "black")

#print the object information
print(c1)