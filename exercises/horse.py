# 4 Horse OOP

class Horse:
    def __init__(self, food, jobs, horse,):
        self._jobs_style = jobs
        self._food_type = food
        self._horse_size = horse

    @property
    def jobs_style(self):
        return self._jobs_style

    @jobs_style.setter
    def jobs_style(self, style):
        self._jobs_style = style

    @property
    def food_type(self):
        return self._food_type

    @food_type.setter
    def food_type(self, type):
        self._food_type = type

    @property
    def horse_size(self):
        return self._horse_size

    @horse_size.setter
    def horse_size(self, size):
        self._horse_size = size


class Yak(Horse):
    def __init__(self, food, jobs, horse):
        super().__init__(food, jobs, horse)
        self._jobs_style = jobs
        self._food_type = food
        self._horse_size = horse

    @property
    def jobs_style(self):
        return self._jobs_style

    @jobs_style.setter
    def jobs_style(self, style):
        self._jobs_style = style

    @property
    def food_type(self):
        return self._food_type

    @food_type.setter
    def food_type(self, type):
        self._food_type = type

    @property
    def horse_size(self):
        return self._horse_size

    @horse_size.setter
    def horse_size(self, size):
        self._horse_size = size


class Donkey(Horse):
    def __init__(self, food, jobs, horse):
        super().__init__(food, jobs, horse)
        self._jobs_style = jobs
        self._food_type = food
        self._horse_size = horse

    @property
    def jobs_style(self):
        return self._jobs_style

    @jobs_style.setter
    def jobs_style(self, style):
        self._jobs_style = style

    @property
    def food_type(self):
        return self._food_type

    @food_type.setter
    def food_type(self, type):
        self._food_type = type

    @property
    def horse_size(self):
        return self._horse_size

    @horse_size.setter
    def horse_size(self, size):
        self._horse_size = size


my_horse = Horse('Race Horse', 'hay', 7)
print(my_horse.horse_size)
print(my_horse.food_type)
print(my_horse.jobs_style)
my_yak = Yak('Pack Yak', 'grass', 8)
print(my_yak.horse_size)
print(my_yak.food_type)
print(my_yak.jobs_style)
my_donkey = Donkey('field work', 'straw', 6)
print(my_donkey.horse_size)
print(my_donkey.food_type)
print(my_donkey.jobs_style)
