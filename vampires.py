class Vampires:
    """ Keeps track of vampires feeding """

    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        vampire = Vampires(name, age, in_coffin, drank_blood_today)
        cls.coven.append(vampire)
        return vampire

    @classmethod
    def sunrise(cls):
        for vampire in cls.coven:
            if not vampire.drank_blood_today or not vampire.in_coffin:
                cls.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False

    def drink_blood(self):
        self.drank_blood_today = True
        return

    def go_home(self):
        self.in_coffin = True
        return

vampire1 = Vampires.create('Dracula', 100, False, False)
vampire2 = Vampires.create('Wife of Dracula', 99, True, True)
vampire3 = Vampires.create('Blade', 35, True, False)

print(Vampires.coven)
Vampires.sunrise()
print(Vampires.coven)
