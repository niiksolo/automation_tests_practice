# class Cats:
#     name: None
#     age: None
#     isHappy: None
#
#     def set_data(self, name, age, isHappy):     # сюда можно писать что угодно , это не значит что name в class и name здесь это одно и тоже просто так принято писать
#         self.name = name                          # вот здесь мы приравниваем self.name - это name из класса и он равен нашому name в set_data
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, self.age, self.isHappy)
#
# cat1 = Cats()
# cat1.set_data('Буся', 0.2, True)
#
# cat2 = Cats()
# cat2.name = 'Барсик'                      # записи cat1 и cat2 работают одинаково но насколько меньше кода в первом варианте
# cat2.age = 3
# cat2.isHappy = False
#
# cat1.get_data()
# cat2.get_data()



class Cats:
    name: None
    age: None
    isHappy: None
    def __init__(self, name, age, isHappy):
        self.set_data(name, age, isHappy)



    def set_data(self, name, age,isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, self.age, self.isHappy)

class StreetCat(Cats):                         # наследственный класс
    where_find_cat: None
    def __init__(self, name, age, isHappy, where_find_cat):
        super(StreetCat, self).__init__(name, age, isHappy)
        self.where_find_cat = where_find_cat
    def get_data(self):                       # полиморфизм переписываем метод get_data
        super().get_data()
        print('where find cat:',self.where_find_cat)

cat1 = Cats('Буся', 0.2, True)
cat2 = Cats("Барсик", 3, False)
cat3 = StreetCat("Пупсик", 7, False, 'street GO')

cat1.get_data()
cat2.get_data()
cat3.get_data()