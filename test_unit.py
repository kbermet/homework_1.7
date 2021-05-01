import unittest

def tovar (a, b):
    if a+b>99:
        return "99 usd is not enough"
    else:
        return "You did not pay the check"

print(tovar(50,32))


class TestTovar(unittest.TestCase):
  def tovar(self):
    self.assertEqual(tovar(50, 50), 100)
  def tovar_1(self):
      self.assertEqual(tovar(50,32), 82)




unittest.main()
# tovar1 = 50
# tovar2 = 32
# if tovar1 + tovar2 > 99 :
#     return "99 рублей недостаточно"
# else:
#     return "Чек оплачен"