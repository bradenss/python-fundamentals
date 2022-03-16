class Boat:
    def __init__(self, hull_material, motor, boat,):
        self._hull_material_style = hull_material
        self._motor_type = motor
        self._boat_size = boat

    @property
    def hull_material_style(self):
        return self._hull_material_style

    @hull_material_style.setter
    def hull_material_style(self, style):
        self._hull_material_style = style

    @property
    def motor_type(self):
        return self._motor_type

    @motor_type.setter
    def motor_type(self, type):
        self._motor_type = type

    @property
    def boat_size(self):
        return self._boat_size

    @boat_size.setter
    def boat_size(self, size):
        self._boat_size = size


my_boat = Boat('steel', 'Yamaha', 50)
print(my_boat.boat_size)
print(my_boat.hull_material_style)
print(my_boat.motor_type)


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


my_horse = Horse('Race Horse', 'hay', 7)
print(my_horse.horse_size)
print(my_horse.food_type)
print(my_horse.jobs_style)


class Watch:
    def __init__(self, material, band_face, casing,):
        self._material_style = material
        self._band_face_type = band_face
        self._casing_size = casing

    @property
    def material_style(self):
        return self._material_style

    @material_style.setter
    def material_style(self, style):
        self._material_style = style

    @property
    def band_face_type(self):
        return self._band_face_type

    @band_face_type.setter
    def band_face_type(self, type):
        self._band_face_type = type

    @property
    def casing_size(self):
        return self._casing_size

    @casing_size.setter
    def casing_size(self, size):
        self._casing_size = size


my_watch = Watch(40, 'Sterling Silver', 'Stainless Steel')
print(my_watch.casing_size)
print(my_watch.band_face_type)
print(my_watch.material_style)


class Guitar:
    def __init__(self, craftsmanship, material, guitar,):
        self._craftsmanship_style = craftsmanship
        self._material_type = material
        self._guitar_size = guitar

    @property
    def craftsmanship_style(self):
        return self._craftsmanship_style

    @craftsmanship_style.setter
    def craftsmanship_style(self, style):
        self._craftsmanship_style = style

    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, type):
        self._material_type = type

    @property
    def guitar_size(self):
        return self._guitar_size

    @guitar_size.setter
    def guitar_size(self, size):
        self._guitar_size = size


my_guitar = Guitar('Gibson', 'wood', 4)
print(my_guitar.craftsmanship_style)
print(my_guitar.material_type)
print(my_guitar.guitar_size)
