class Kachok():

    def __init__(self, name='Арнольд', weigth=70, height=170, age=18):
        self.name = name
        self.age = age
        self.weight = weigth
        self.heigth = height

    def talk(self):
        return 'Ouff!!!'

    def constitution(self):
        const_type ='не определено'
        if self.age<18:
            norm_weight=self.heigth-110
        else:
            norm_weight=self.heigth-100

        if self.weight==norm_weight:
            const_type='эндоморф'
        elif self.weight>norm_weight:
            const_type = 'мезоморф'
        else:
            const_type = 'экзоморф'
        return const_type

alex=Kachok('Alex',80,170,19)
print(alex.constitution())
print(alex.talk()*5)


