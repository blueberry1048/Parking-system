"""
Simple Parking System - Preliminary Version
"""

class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.spots = {}
    
    def park(self, license_plate):
        """Park a vehicle"""
        if len(self.spots) >= self.total_spots:
            return "Parking Full"
        
        if license_plate in self.spots:
            return "Already Parked"
        
        spot_number = len(self.spots) + 1
        self.spots[license_plate] = spot_number
        return f"Parked at Spot {spot_number}"
    
    def remove(self, license_plate):
        """Remove a vehicle"""
        if license_plate in self.spots:
            del self.spots[license_plate]
            return "Vehicle Left"
        return "Vehicle Not Found"
    
    def status(self):
        """Show parking status"""
        return f"{len(self.spots)}/{self.total_spots} spots occupied"


# Example usage
if __name__ == "__main__":
    lot = ParkingLot(10)
    
    print(lot.park("ABC-1234"))
    print(lot.park("DEF-5678"))
    print(lot.status())
    print(lot.remove("ABC-1234"))
    print(lot.status())
