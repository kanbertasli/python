"""
Take 5 values from the user and write a program that prints the values you get on screen.
Print the type of values you received in this program on screen.
When using print functions, do not forget to use f-string and format usage in your program.
"""

data = list(range(5))
try:
    data[0]=type(eval(input('Lütfen integer(Örn:44),float(Örn:44.3),string(Örn:"deneme"),boolean(True/False) veya complex(Örn:3.14j) olan 1. değişkeninizi giriniz? ')))
    data[1]=type(eval(input('Lütfen integer(Örn:44),float(Örn:44.3),string(Örn:"deneme"),boolean(True/False) veya complex(Örn:3.14j) olan 2. değişkeninizi giriniz? ')))
    data[2]=type(eval(input('Lütfen integer(Örn:44),float(Örn:44.3),string(Örn:"deneme"),boolean(True/False) veya complex(Örn:3.14j) olan 3. değişkeninizi giriniz? ')))
    data[3]=type(eval(input('Lütfen integer(Örn:44),float(Örn:44.3),string(Örn:"deneme"),boolean(True/False) veya complex(Örn:3.14j) olan 4. değişkeninizi giriniz? ')))
    data[4]=type(eval(input('Lütfen integer(Örn:44),float(Örn:44.3),string(Örn:"deneme"),boolean(True/False) veya complex(Örn:3.14j) olan 5. değişkeninizi giriniz? ')))
except (ValueError, ZeroDivisionError) as error:
    print('Lütfen bir değişken giriniz! ', error)
else:
    print('Lütfen bir değişken giriniz! ')
    
print(f' 1.değişken tipiniz: {{}}\n 2.değişken tipiniz: {{}}\n 3.değişken tipiniz: {{}} \n 4.değişken tipiniz: {{}} \n 5.değişken tipiniz: {{}} \n '.format(data[0],data[1],data[2],data[3],data[4]))
