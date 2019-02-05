import requests
from HelperTestBase import HelperTestBase, add_point_list
from urllib.parse import urljoin


add_point_qnt = len(add_point_list)
print(add_point_qnt)

class TestCheckStatus(HelperTestBase):

    counter = 0
    def test_CheckStatusCode(self,):


        for element in add_point_list:

            if self.counter != add_point_qnt - 1:
                url = urljoin(self.base_url, add_point_list[self.counter])
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

