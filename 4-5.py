class Mama:
    def __init__(self, hair, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hair = hair
        self.growth = 165
class Papa:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.coloreye = "green"
class Children(Papa, Mama):
    def print_info(self):
        print(self.hair)
        print(self.coloreye)
        print(self.growth)
baby = Children(hair ="blond")
baby.print_info()