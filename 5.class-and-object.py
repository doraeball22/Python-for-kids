class Giraffe():
    def walk(self):
        print("walk 4 legs")
    def walkForward(self):
        print('เดินไปข้างหน้า')
    def left(self):
        print('เลี้ยวซ้าย')
    def right(self):
        print('เลี้ยวขวา')
    def walkback(self):
        print('ถอยหลัง')      
    def findFood(self):
        print('หาใบไม้อ่อน')
        self.eatFood()
    def eatFood(self):
        print('เคี้ยวช้าๆ')
                      


class Human():
    def walk(self):
        print("walk 2 legs")

class Cat():
    def sing(self):
        print('เหมียวเหมียว')
    def walk(self):
        print('walk 4 legs')
    def eatFood(self):
        print("แง่มๆ")
    def findFood(self):
        self.walk()
        print("ฉันเจออาหารแล้ว")
        self.eatFood()


renold = Giraffe()
renold.findFood()

# renold.walk()
# renold.walkForward()
# renold.left()
# renold.right()
# renold.walkback()


# flok = Human()
# flok.walk()

# tom = Cat()
# tom.walk()
# tom.findFood()

