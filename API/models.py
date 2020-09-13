from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):  
    __tablename__="flights"
    id= db.Column(db.Integer, primary_key=True)
    origin= db.Column(db.String, nullable=False)
    destination= db.Column(db.String, nullable=False)
    duration= db.Column(db.Integer,nullable=False)
    passengers=db.relationship("passenger", backref="flight", lazy=True)

    def add_passenger(self, name):
            # creating a passenger object
        p =passenger(name=name, flight_id=self.id)
        # adding passenger to database
        db.session.add(p)
        db.session.commit()

class passenger(db.Model):
    __tablename__="passengers"
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, nullable=False)
    flight_id= db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False) 




    
if __name__ == "__main__":
    main()
