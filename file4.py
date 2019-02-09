#outside of the class

class Mobile:
    def __init__(self):
        self.model="mI 4"
        self.name="Red MI 4"
        self.price=8500


m=Mobile()
m.display_size=4.5
print(m.__dict__)