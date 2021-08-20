# 1zadanie
class Student: #Создаем класс Student
    def __init__(self, name, lastname, department, year_of_entrance): #Инициализируем
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
    def get_student_info(self): #Создаем метод,  который возвращает имя,фамилию, год поступления и факультет
        print(self.name, self.lastname, self.department, self.year_of_entrance)
m = Student('Вася', 'Иванов', 'поступил в 2017 г', 'на факультет Програмиста') #
m.get_student_info()

# --------------------------------------------------------------------

# 2zadanie
class Airplane:

    def init(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        print(f'Самолет {self.model} взлетел, скорость {self.max_speed} км/ч, расстояние {self.odometer}')

    def fly(self, km):
        self.odometer += 100

    def land(self):
        self.is_flying = False


'''            
start = Airplane("Viktory","RF-27","2018",2500)
print(start.take_off())
print(start.fly(600))
print(start.fly(600))
print(start.land())

'''
# 2 вариант
samolet = Airplane(
    model='Viktory RF-27',
    year='2018',
    max_speed=2500
)

samolet.fly(5000)
samolet.take_off()

# ----------------------------------------------------------------------

# 3zadanie
class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def drive(self, distance):
        fuel = distance / 10
        if self.fuel >= fuel:
            self.__add_distance(distance)
            self.__subtract_fuel(fuel)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, fuel):
        self.fuel -= fuel


a = Car('sedan', 'avto', '2020')


# a._Car__add_distance(100)


# a._Car__subtract_fuel(100)


print(a.drive(int('100')))

# --------------------------------------------------------------------

# 4zadanie
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [] на all_contacts =
# Список контактов(). Создайте несколько контактов, используйте метод
# search_by_name.
class ContactList(list):  # Создается дочерний клас Contact который унаследет от list
    def search_by_name(self, *name):  # Создан метод search_by_name который содержит в себе аргумент name
        self.sovpadenie = []  # Создается пустой листь для хранение совпадений
        self.all_contacts = ["Bова", "Канат", "Жакып", "Азат", "Марат", "Айдай",
                             "Умар", "Динара", "Султан", "Жака", "Асан", "Нурмамат", "НУрайым",
                             "Байэл"]  # Создан лист из неких контактов

        for i in name:  # Создается цикл которое каждый раз проходится по name и передает его значения на i
            if i in self.all_contacts:  # Создается условие: если заначение i есть внутри списка all_contacts
                self.sovpadenie.append(i)  # то его добавляет в список sovpadenie
                print(f"Совпал контакт {i}!")  # Выводится значенеи котрый совпал

            elif i not in self.all_contacts:  # Создается еще одно условие: если значение i не окажется внутри списка sovpadenie
                print(f"Совпадений {i} не найдено!")  # то Выводится значение которое не совпало

        print(f"Список всех совпадений {self.sovpadenie}")  # В конце выподится список Совпавших имен


s = ContactList()  # Обявляется переменное на класс
s.search_by_name("Асан", "Тилек", "Нурмамат", "Бlайэл", "Кубат", "Айдай")  # Вызывыется метод с списком искомых имен

# ------------------------------------------------------------------------------

# 5zadanie
# TASK 5  AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

import time#импорт времени в данной задаче необходима, чтобы имитировать время выстрела оружия

class Soldier():#объявляем класс
    def init(self, name, gun):# инициализируем значения
        self.name = name #приравниваем
        self.gun = gun #приравниваем

class Guns():# объявляем еще один класс
    def shoots(self):#указываем метод
        print(f'{self.name} shoots from: {self.gun}')#выводим ззначения на экран (без переменных)
        self.ammunition = 30# кол-во боеприпасов
        while self.ammunition > 0:#начало цикла
            self.ammunition -= 1#30-1
            print('tigi-tigitishh')#выводит значения на экран (имеено звук оружия)
            time.sleep(0.3)#указываем с какой задержкой должно появляться на экране(указываем по желанию время)

        if self.ammunition == 0:#если кол-во патронов будет равно 0 то в силу вступает следющий метод
            self.reloads()#название метода который будет применим
        else:
            pass


    def reloads(self):# название метода
        self.reload = input('Do you want to reload weapon? y/n: ')#когда пули закончаться на экране будет предложена следующая опция перезарядки
        if self.reload == 'y':# yes сокрашенно y означает да
            self.shoots()# запуск предыдущего метода т.е. продолжения стрельбы
        else:
            pass


class Act_of_Shooting(Soldier, Guns):# дочерний класс т.е. происходит наследование от двух главных классов
    def init(self, name, gun):# инициализация
        Soldier.init(self, name, gun)# иницализация Soldier


soldier1 = Act_of_Shooting('Soldier Ryan', 'AK47')# объявляем переменные для вывода на экран
soldier1.shoots()#вызываем метод

# ---------------------------------------------------------------------

# 6zadanie
# Мебель:
#
#
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.



class House():
    def init(self, typehouse, areahouse):
        self.typehouse = typehouse
        self.areahouse = areahouse

    def get_house(self):
        self.totalarea = 0
        self.furnitures = {
            'Кравать' : 4,
            'Гардироб' : 2,
            'Стол' : 1.5
        }
        for value in self.furnitures.values():
            self.totalarea += value
        print('Тип дома: ',self.typehouse," -- Общая площадь:",self.areahouse, "\n",list(self.furnitures.keys()),"\n" "Оставшаяся площадь: " ,self.areahouse - self.totalarea)
b = House('Квартира', 80)
b.get_house()

# ------------------------------------------------------------------

# 7 zadanie
class Student:
  def init(self,name,lastname,age,objects):
    self.name = name
    self.lastname = lastname
    self.age = age
    self.objects = objects
  def disp(self):
    print(self.name, self.lastname, self.age, self.objects)

Steve = Student("Steven",'Shultz' , 23, "English")
Johny = Student("Jonathan","Rosenberg", 24 , "Biology")
Penny = Student("Penelope","Meramveliotakis", 21 , "Physics")
Steve.disp()
Johny.disp()
Penny.disp()

# -----------------------------------------------------------------------

# 8zadanie
class MoneyFmt:
  def init(self, value = 0.0):
    self.value = float(value)
  def update(self, value = None):
    self.value = value
  def str(self):
    if self.value >= 0:
      return '${:,.2f}'.format(self.value)
    else:
      return '-${:,.2f}'.format(-self.value)
  def repr(self):
    print(self.value)
    return f'{self.value}'

from AlphaMoney import MoneyFmt
def dollarize():

  cash = MoneyFmt(12345678.021)
  repr(cash)
  print(cash)
  cash.update(100000.4567)
  repr(cash)
  print(cash)
  cash.update(-0.3)
  repr(cash)
  print(cash)
  a1 = eval(input('Введите число и я переведу его в доллоровое значение: '))
  cash.update(a1)
  print(cash)

  a2 = input("Если хотите повторить процедуру введите '1' , для выхода введите Enter: ")
  while a2 == '1':
    a3 = eval(input('Введите число: \n'))
    cash.update(a3)
    print(cash)
dollarize()

# ------------------------------------------------------------------

# 9zadanie

class Car:
    def call(self):
      print('Автомобиль заведен')

class Calls:
    def call(self):
      print('Автомобиль заглушен')

class Date:
    def call(self):
      print('2003')

class Type:
    def call(self):
      print('Универсал')

class Color:
    def call(self):
      print('Серый')

car1 = Car()
car2 = Calls()
car3 = Date()
car4 = Type()
car5 = Color()
for i in(car1, car2, car3, car4, car5):
    i.call()