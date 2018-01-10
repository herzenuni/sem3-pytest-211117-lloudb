def fact(n):
    res = None
    if type(n) is not int:
        raise TypeError
    try:
        n = int(n)
    except (ValueError, TypeError) as e:
        print('Argument "{}" is not a number '.format(n))
    else:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 1
        else:
            res = n * fact(n - 1)
            return res

print("3. {}".format(fact(3)))


#assert fact(5) == 120 # "Факториал при n = 5 должен быть равен 120"
#assert fact(0.5) == None # ("При n = 0.5, значение факториала вычисляться не должно. Вернет None")
#assert fact(-5) == None # ("При отрицательных значениях Ф. не вычисляется, возвращаем None")

if __name__ == '__main__':
    import unittest


    class TestFactorialMethods(unittest.TestCase):
        def test_normal_values(self):
            self.assertEqual(fact(5), 120)
            self.assertEqual(fact(0.5), None)
            self.assertEqual(fact(-5), None)

        def test_except_ValueError(self):
            with self.assertRaises(ValueError):
                fact(-1)

        def test_except_TypeError(self):
            with self.assertRaises(TypeError):
                fact([0, 1])
            with self.assertRaises(TypeError):
                fact('hello')
            with self.assertRaises(TypeError):
                fact(0.5)
