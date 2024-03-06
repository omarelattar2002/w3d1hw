#excercise 1

# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    def __init__(self, name, energy, kind):
        self.name = name
        self.energy = energy
        self.kind = kind
    
    def play(self, time_played):      # Nvm
        self.energy -= time_played
        print(f"{self.name} has played for {time_played} minutes and his energy now is {self.energy}")

    def sleep(self, time_slept):
        self.energy += time_slept
        print(f"{self.name} slept for {time_slept} and now he is energetic and has an energy of {self.energy}")

    def eat(self, amount_of_food, food_kind, amount_of_plates):
        self.energy *= amount_of_food
        self.food_kind = food_kind
        self.amount_of_plates = amount_of_plates
        print(f"{self.name} ate {amount_of_plates} of {food_kind} which has {amount_of_food} calories so now his energy is {self.energy}")



d1 = Animal('zack', 50, 'german shepard')
d2 = Animal('mark', 20, 'plates of chicken', )


d2.eat(10,'plates of pasta', 3)



print(d2.energy)




#excercise 2