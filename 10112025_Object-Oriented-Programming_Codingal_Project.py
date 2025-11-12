# DOG 
class dog:
    def __init__(self, breed, color, details):
        self.breed = breed
        self.color = color
        self.details = details
goldenr = dog('Golden Retriever', 'Golden', 'Friendly')
pitbull = dog('Pitbull', 'Grey', 'Guard-Dog, Scary-like Unfriendly')
print(goldenr.breed)
print(goldenr.color)
print(goldenr.details)
print('------')
print(pitbull.breed)
print(pitbull.color)
print(pitbull.details)