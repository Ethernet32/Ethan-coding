class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name}     {self.breed}"

dogs = [
    Dog("Marceline","German Shepherd"),
    Dog("Cajun","Belgian Malinois"),
    Dog("Daisy","Border Collie"),
    Dog("Rocky","Golden Retriever"),
    Dog("Bella","Irish Setter")
]
count=1
for item in dogs:
    print(f"{count} {item}")
    count += 1