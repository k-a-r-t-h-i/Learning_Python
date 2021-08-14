#Class example

class Bus:
    def __init__(self,registration_name, conductor_name, driver_name, total_seats, seats_booked): #this is the constructor function
        self.registration_name=registration_name          #self.variable which creates a class variable
        self.conductor_name=conductor_name
        self.driver_name=driver_name
        self.total_seats=total_seats
        self.seats_booked=seats_booked
    
    def print_bus_details(self):   #self should be the first parameter of all functions
        print("Registration Name:",self.registration_name)
        print("Conductor Name:",self.conductor_name)
        print("Driver Name:",self.driver_name)
        print("Total Seats:",self.total_seats)
        print("Seats Booked:",self.seats_booked)
    
    def is_seat_available(self):
        if (self.total_seats-self.seats_booked)>0:
            return True
        else:
            return False
    
    def book_seat(self,no_of_seats):
        if (self.total_seats-self.seats_booked)>= no_of_seats:
            self.seats_booked+=no_of_seats
        else:
            return "Requested no of seats not available"

Bus1=Bus("TN101", "Joe", "John", 25, 12)  #object creation the arguments in this are passed to the constructors
Bus1.print_bus_details()            #the procedure to call a function
print(Bus1.book_seat(1))
print(Bus1.book_seat(12))
print(Bus1.book_seat(1))
Bus1.print_bus_details()

"""
Output:
Registration Name: TN101
Conductor Name: Joe
Driver Name: John
Total Seats: 25
Seats Booked: 12
None
None
Requested no of seats not available
Registration Name: TN101
Conductor Name: Joe
Driver Name: John
Total Seats: 25
Seats Booked: 25
"""