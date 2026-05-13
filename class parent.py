class parent:
 
    def __init__(self, eyes, temper):
        self.eyes = eyes
        self.temper = temper
    def display(self):
        print("Your eye color is:", self.eyes)
        print("is your temper bad?:", self.temper)

class son(parent):

    def __init__(self, name, age, eyes, temper):
        self.name = name
        self.age = age

        parent.__init__(self, eyes, temper)


obj = son("Penguin", 8, "Blue", False)

obj.display()