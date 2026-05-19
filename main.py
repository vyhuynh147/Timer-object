# 
class Clock:
    def __init__(self, time, number, color):
        self.time = time
        self.number = number
        self.__color = color
    
    def set_Alarm(self):
        self.time +=1
        # print(f"{self.number} stop the clock.")

    def ringer(self):
        print(f"The bell ringer have{self.__color} color. And total {self.time} hours.")

    def __str__(self):
        return f" A clock stop at {self.number}, the color of bell ring is {self.__color}. And the total hours of clock is {self.time} hours."

c1 = Clock( 24 , 12 , "black")

print(c1.__color)

# print(c1)