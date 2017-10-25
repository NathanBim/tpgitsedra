import math, pickle

class Sphere(object):

    def __init__(self, radius):
        self.radius = radius
        pass

    STEP 2
    
    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self.radius)

    def surface(self):
        return 4.0 * math.pi * self.radius ** 2
        pass

    def volume(self):
        return 4.0/3.0 * 3.1416 * self.radius ** 3
        pass

    def diameter(self):
<<<<<<< master
        return self.radius
=======


        return self.radius*2
>>>>>>> local
        pass

    def dump(self, filename):
        # *** STEP 6 ***
        # uncomment the 2 following line
        #with open(filename, "w") as f:
        #    pickle.dump(self, f)
        pass

def loadSphere(filename):
    # *** STEP 7 ***
    # uncomment the 3 following line
    #with open(filename, "r") as f:
    #    sphere = pickle.load(f)
    #    return sphere
    pass
