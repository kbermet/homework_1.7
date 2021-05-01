import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']

my_file = open(random.choice(names), 'w', encoding='utf-8')

def func(files):
    for i in files:
            try:
                with open(i, 'r', encoding='utf-8') as f:
                    return f.readlines()
            except FileNotFoundError:
                print("There is no such file")
            else:
                i.write("Bermet")
                i.close()
print (func(names))


