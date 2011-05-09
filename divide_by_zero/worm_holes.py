
class worm_hole():
    def __init__(self,espace_origin,espace_destiny, time_origin, time_destiny):
        
        self.espace_origin = espace_origin
        self.espace_destiny = espace_destiny
        self.time_origin = time_origin
        self.time_destiny = time_destiny
        self.safe_hole = False
        
    def create(self, energy, safe_hole=True):
        def energySpend(self,energy):
            import math 
            #TODO: This formula
            distanceSpend = (self.espace_origin - self.espace_destiny) / math.pi
            from datetime import datetime
            td= (self.time_origin - self.time_destiny)
            timespend = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
            timeSpend = (timespend)/math.e
            totalSpent = distanceSpend + timeSpend
            print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            print distanceSpend
            print timespend
            print totalSpent
            if energy >  totalSpent:
                return True
            else:
                return False
            
        if energySpend(self,energy) == False and safe_hole:
            raise Exception("Not enougth energy to make a stable worm hole.")
        else:
            #TODO:Discover how to create a wormhole using this energy.
            return True
            

    def transport(self, passenger):
        if not self.safe_hole:
            print "Buckle Up! You'll probably have a bumpy ride!"
        
        #TODO:How to transport someone(alive) to the other side?
        
        
        if passenger.is_alive:
            print "You just arrived at your destination....alive"
        else:
            #TODO:Hide evidences?   
            return False 
        
        return passenger
