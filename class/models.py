from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    
    __tablename__="flights"
        
    id=Flight.counter
    Flight.counter+=1
    
    # Keep track of passenger 
    self.passengers =[]


        #  Details of flights 
        self.origin=origin
        self.destination=destination
        self.duration=duration

    # print function
    def print_info(self):
      print(f"FLight Ori: {self.origin}")
      print(f"FLight des: {self.destination}")
      print(f"FLight duration: {self.duration}")

      print()

      print("passengers:")

      for passenger in self.passengers:
          print(f"Passenger name: {passenger.name}")

    # Method used to reduce the duration of flight by certain amount,
    def delay(self, amount):
        self.duration+=amount

     # Method used to tight together the flight and the passenger ,
    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id=self.id
      
      
class passenger:

    def __init__(self,name):
        # name  of passenger
        self.name=name



def main():
    # creating a flight object 
    f1 =Flight(origin="New York", destination="Paris",duration=540)

    #creating a passenger object 
    alice=passenger(name="Alice")
    bob=passenger(name="Bob")

    #adding the passenger object to the flight object using the method add_passeger method of the flights object
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    # printing the result 
    f1.print_info()
    
    
if __name__ == "__main__":
    main()
