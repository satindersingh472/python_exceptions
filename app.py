
try:
   result = 5 + '5'
except TypeError:
    print(' unsupported operand type(s) for +: "int" and "string_y"')
except:
    print('Only the same data type can be added')
finally: 
    print('i wil run')