# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    
    def play(self, energy_decrease):      # Nvm
        self.energy -= energy_decrease
        print(f"{self.name} has played for {self.time_played} and his energy now is {self.energy}")


    def sleep():
        pass


zack = Animal('zack', 50)


zack.play(5)



print(zack.energy)
