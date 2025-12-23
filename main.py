class Vehicle:
    def __init__(self,total_fare):
        self.total_fare=total_fare
    def display(self):
        print("The total fare is",self.total_fare)
class Bus(Vehicle):
    def __init__(self,total_fare):
        self.total_fare=total_fare
        Vehicle.__init__(self,total_fare)
ob=Bus("75%")
ob.display()