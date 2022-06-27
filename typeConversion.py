x = 10
y = 2.5
z = "20"

# ตรวจสอบชนิดข้อมูล
print(type(x))
print(type(y))
print(type(z))

print(x+y) # 12.5
# print(x+z)  TypeError: unsupported operand type(s) for +: 'int' and 'str'

# String -> int
print(x+int(z))

# int -> string
print(str(x)+z)

# String -> float
print(y+float(z))

# หากต้องการเปลียนให้ตัวแปร z มีชนิดเป็น float จะต้องแทนค่าลงไปใน z ด้วย
z = float(z)
print(type(z))