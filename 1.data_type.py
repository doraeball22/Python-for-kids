# ชนิดข้อมูล
# 1.Number แบ่งออกเป็น 1.1 จำนวนเต็ม  1.2 จำนวนจริง
integerNumber = 102 # จำนวนเต็ม (integer)
flotingPointNumber = 10.5 # จำนวนจริง เป็นทศนิยม (Floating point)

# + - * / % //
num1 = 9 
num2 = 2
print("num1 + num2 = {}".format(num1+num2))
print("num1 - num2 = {}".format(num1-num2))
print("num1 * num2 = {}".format(num1*num2))
print("num1 / num2 = {}".format(num1/num2))
print("num1 % num2 = {}".format(num1%num2))
print("num1 // num2 = {}".format(num1//num2))

# 2. String คือ สายอักขระ หรือประโยค ก็คือข้อความนั่นแหละ
myString = 'hello world'
# การจัดการ string
firstName = "Sorawut"
lastName = "Wichahong"
# 2.1 เอา String มาต่อกันได้ด้วยการ +
fullName = firstName + ' ' + lastName
# My fullname: Sorawut Wichahong
print("My fullname: {} {}".format(firstName, lastName))
num1 = "1"
num2 = "2"
num3 = num1+num2
print(num3)
# การ casting คือการแปลงชนิดข้อมูล 
num3 = int(num1)+int(num2)
print(num3)
myBirthYear = "2548"
current = "2561"
age = int(current) - int(myBirthYear)
# my birth year is 2548, current year is 2561 so my age is 13
print(age)
print("my birth year is {}; current tear is {} so my age is {}".format(myBirthYear,current,age))

# 2.2 ต้องการส่วนหนึ่งของ string 
myString = "hello world"
print("ตัดสตริง: {}".format(myString[4:9])) # o wor เอาต้งแต่ตำแหน่งที่ 4 แต่ไม่ถึง 9

# 2.3 นับความยาวของ string
print("{} มี {} ตัวอักษร".format(myString, len(myString)))

# 3. ชนิดข้อมูล List
myList = [] # การประกาศลิส
myGameList = ['minecraft', 'ROV', 'APB'] 
print("my first game: {}".format(myGameList[1:3]))

# 3.1 การเพิ่มของเข้าไปใน List เราจะใช้คำสั่งว่า append()
myGameList.append('DECEIT')
print(myGameList)

# 3.2 การเอา List มารวมกัน
fahGameList = ['APB','the sims','DECEIT']
sumList = myGameList + fahGameList
print(sumList)

# 3.3 การเอาของออกจาก List จะใช้วิธี เช่น ต้องการเอาเกมแรกออกจากลิส myGameList = myGameList[1:3] หรือใช้คำสั่ง remove()
myGameList.remove('minecraft')
print("new list after remove first item: {}".format(myGameList))

# Assignment 1
# 1.ให้สร้างไฟล์ 1.bmi.py
# 2. สร้างตัวแปร น้ำหนัก(กิโลกรัม) กับ ส่วนสูง(เมตร)
# 3. bmi = น้ำหนัก/ส่วนสูง ยกกำลังสอง

# Assignment 2
# 1. องศาฟาเรนไฮต์ 	°F = (1.8 × °C) + 32 ให้องศาเซลเซียสมา แล้วแปลงไปเป็นองศาฟาเรนไฮ เช่น 0 เซลเซียส = 32 ฟาเรนไฮ
# 2. องศาเซลเซียส 	°C = (F - 32) x 5/9  ให้องศาฟาเรนไฮมา แล้วแปลงเป็นองศาเซลเซียส   เช่น 32 ฟาเรนไฮ = 0  เซลเซียส
