class Box:
    # mutable whatever 
    def __init__(self, x):
        self.x = x

    def of(x):
        return Box(x)
    
    def map(self, func):
        return Box.of(func(self.x))
    
    def get(self):
        return self.x