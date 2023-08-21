class ClassesOfVideoGames:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Привіт, я {self.name}")

    def attack(self, target):
        print(f"{self.name} атакує {target}")


class Knight(ClassesOfVideoGames):
    def __init__(self, name, weapon):
        super().__init__(name)
        self.weapon = weapon

    def attack(self, target):
        print(f"{self.name} атакує {target} зброєю {self.weapon}")


class Mage(ClassesOfVideoGames):
    def __init__(self, name, spell, mana):
        super().__init__(name)
        self.spell = spell
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} кастує {self.spell}")
        else:
            print(f"{self.name} немає стільки мани щоб кастанути {self.spell}")


warrior = Knight("Arthur", "меч")
mage = Mage("Gandalf", "файрбол", 15)

warrior.speak()
warrior.attack("орка")

mage.speak()
mage.cast_spell()
