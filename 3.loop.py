# print('hello'*10)

# การทำซ้ำ (Loop)
# for x in range(0, 10):
#     print('hello')

# for f in range(50, 101) :
#     print(f)

# gameList = ['dota', 'ROV', 'Minecraft', 'PUBG']
# for game in gameList:
#     print(game)

# colors = ['red ', 'yellow' , 'green']
# for color in colors:
#     print(color)
#     for color in colors:
#         print(color)


# for i in range(0, 5):
#     for j in range(0, 5):
#         print(i)
#     print('\n')

# for i in range(0, 5):
#     for j in range(0, 3):
#         print()
#     print('\n')

# # วนลูปตั้งแต่เลข 0 - 10 ถ้าเป็นเลขคู่ พิมพ์เลขนั้น(เลขคู่) 2(เลขคู่)
# for x in range(0,11) :
#    if x % 2 ==0 :
#     print('{}เลขคู่'.format(x))
    
# 1 % 2 = 1
# 2 % 2 = 0
# 3 % 2 = 1
# 4 % 2 = 0
# 5 % 2 = 1

# การเขียนลูปโดยการใช้ while
# x = 0
# while x < 10:
#     print("hello")

#     x = x+1

# k = 1
# while k < 10:
#     print(k)
#     k =k+1

# f = 0
# while f < 21:
#     if(f % 2 == 0):    
#         print("x={}".format(f))
#     f = f + 1


# p = 0
# while p < 11:
#     if(p % 2 ==1):
#         print("s={}".format(p))
#     p = p +1

# for x in range(0,11) :
#   if x % 2 ==1 :
#     print('{}เลขคี่'.format(x))


# ถ้าเราชั่งน้ำหนักบนดวงจันทร์ น้ำหนักเราจะเป็น 16.5 เปอร์เซ็นของน้ำหนักบนโลก 
# เราจะคำนวณโดยการ เอาน้ำหนักบนโลกคูณด้วย 0.165 เช่น น้ำหนักบนโลกเราคือ 67 จะได้ 67*0.165 เราจะได้น้ำหนักบนดวงจันทร์คือ 11.055
# คำถามคือ ถ้าน้ำหนักเราเพิ่มปีละ 1 กิโลกรัม แล้วเวลาผ่านไป 15 ปี เราไปชั่งน้ำหนักบนดวงจันทร์ น้ำหนักของเราบนดวงจันทร์จะเป็นเท่าไร
# จงเขียนโปรแกรมคำนวณ
 
# for x in range(67):
#    z = x+15
#    z = x * 0.165
#    print(z)

 
# f = 67
# while f < 16:
#      (f + 1 ):
#         print("z={}".format(f))
#     f = f * 0.165
  
weight = 67
for year in range(16):
    weight =  weight + 1
    
weight = weight * 0.165
print(weight)