class dog_breed:
    

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


golden_retriever = dog_breed("Golden retriever", "Gold/blonde")
german_shepard = dog_breed("German shepard", "Black and hazel")

print(golden_retriever.breed)
print("Color", golden_retriever.color)
print(german_shepard.breed)
print("Color", german_shepard.color)