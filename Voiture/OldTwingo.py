from Car.Car import Twingo

class OldTwingo(Twingo):
    def __init__(self, licenceNumber: str):
        super().__init__(licenceNumber, nbDoors=3)