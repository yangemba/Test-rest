import requests
from HelperTestBase import HelperTestBase, add_point_list
from urllib.parse import urljoin

'''urljoin  - хороший метод для слияния основного УРЛа с Эдд-поинт. Так как даже если ты осташь "/" и в коне УКРла и в 
начале Эдд-поинта - то он уберет лишний. Экономит кучу времени на поиск ошибки'''

add_point_qnt = len(add_point_list) # Кол-во елеметов в эдд поинте (фактическое, начинаеться с 1-го)
print(add_point_qnt)

class TestCheckStatus(HelperTestBase):

    counter = 0 # - счетчик для проверки что мы не вышли закол-во. По дэфолту ноль, так как первый элемент - нулевой
    def test_CheckStatusCode(self,):

        for element in add_point_list: #Проходка по каждому элементу

            if self.counter != add_point_qnt - 1:# "-1" отнимает от фактического, так как индекс должен быть пайтоновский
                url = urljoin(self.base_url, add_point_list[self.counter])# собственно сам индекс
                response = requests.get(url)
                # print(response)
                if response.status_code == 200:
                    print('Get ' + ' ' + str(url))
                    print(str(response) + '\n')
                    self.assertIs(True, str(response) == '<Response [200]>')
                else:

                    print('Get ' + ' ' + str(url))
                    print(str(response) + '\n' )
                    self.assertIs(True, str(response) == '<Response [200]>')

                self.counter = self.counter + 1
            else:
                break


TestCheckStatus().test_CheckStatusCode()

