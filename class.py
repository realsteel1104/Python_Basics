class Human:
    def __init__(self,n,o):                     #its going to initialize properties of the class
        self.name = n                 #self means class itself
        self.occupation = o

    def doing_work(self):
        if self.occupation == "tennis":
            print(self.name,"plays tennis")
        elif self.occupation == "acting":
            print(self.name, "is a actor")

    def speaking(self):
        print(self.name, "Hi how are you")

Pratik = Human("Pratik","actor")
Pratik.speaking()
Pratik.doing_work()
