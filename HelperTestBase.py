import unittest

class HelperTestBase(unittest.TestCase):

    def __init__(self): # заменил на конструктор иначе плохо импортирует
        self.base_url = 'https://premier.ua/zhilaia-nedvizhimost'

add_point_list = ['/arenda-zhilia', '/pokupka-zhilia', '/kvartiry-v-novostroykakh', '/prodazha-mn-kh-elitnykh',
                  '/garazhi']

