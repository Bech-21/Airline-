class Flight:
    def__init__(self,origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration
    def print_info(self):
      print(f"FLight Ori": {self.origin})
      print(f"FLight des": {self.destination})
      print(f"FLight duration": {self.duration})

def main():
    f1 =Flight(origin="New York", destination="Paris",duration=540)
    f1.print_info()
    f1 =Flight(origin="New York", destination="Paris",duration=540)
    f1.print_info()
    
if __name__ == "__main__":
main()
