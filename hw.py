# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    
    def play(self, time_played, energy_decrease):
        self.energy_decrease = self.energy -= energy



zack = Animal('zack', 50)

print(zack.energy)
