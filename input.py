# input จะรับค่า string แม้ว่าผู้ใช้จะป้อนตัวเลขมาก็ตาม

name = input("กรุณาป้อนชื่อ : ")
print("Your name is " +name)
print(type(name))

num1 = input("กรุณาป้อนตัวเลขตัวที่ 1 : ") # 1
num2 = input("กรุณาป้อนตัวเลขตัวที่ 2 : ") # 3

"""
    ทำการแปลงให้เป็น int ตั้งแต่กรอกมาเลย
num1 = int(input("กรุณาป้อนตัวเลขตัวที่ 1 : "))
num2 = int(input("กรุณาป้อนตัวเลขตัวที่ 2 : ") )
"""

total = num1 + num2
print(total) # จะแสดงเป็น 13 เนื่องจากเป็นการเอา string มาต่อกัน

num1 = int(num1)
num2 = int(num2)
total = num1 + num2
print(total) # จะแสดงเป็น 4 เนื่องจากได้แปลง str -> int แล้ว
