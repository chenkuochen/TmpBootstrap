# coding=utf-8
import django
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

import datetime
from restfulAPI.models import Person, Meal, Location, Table
from restfulAPI.views import TableViewSet

class TableTests(APITestCase):
    def setUp(self):
        self.db_initialize()

    def test_table_list(self):
        response = self.client.get('/api/tables/')
        expected_response_body = self.get_expected_response_body()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.trim(response.data), expected_response_body)

    def db_initialize(self):
        aaron = Person.objects.create(name="Aaron", contact_number="939123456",photo="https://dl.dropboxusercontent.com/s/nsg98icvvuzcw5e/aaron%E7%9A%84%E5%AE%B6.jpg?dl=0")
        baird = Person.objects.create(name="Baird", contact_number="918234567",photo="https://dl.dropbox.com/s/3pb2568jhwge0n0/Baird%E7%9A%84%E5%AE%B6.jpg?dl=0")
        caesar = Person.objects.create(name="Caesar", contact_number="910345678",photo="https://dl.dropboxusercontent.com/s/r9q9kwsett0j096/Caesar%E7%9A%84%E5%AE%B6.jpg?dl=0")
        dana = Person.objects.create(name="Dana", contact_number="921456789",photo="https://dl.dropboxusercontent.com/s/02g7b9lpydfi1gw/Dana%E7%9A%84%E5%AE%B6.jpg?dl=0")
        ada = Person.objects.create(name="Ada", contact_number="910345678",photo="https://dl.dropboxusercontent.com/s/ubo1ay8k9452urm/Ada%E7%9A%84%E5%AE%B6.jpg?dl=0")
        barbara = Person.objects.create(name="Barbara", contact_number="939123456",photo="https://dl.dropbox.com/s/3pb2568jhwge0n0/Baird%E7%9A%84%E5%AE%B6.jpg?dl=0")

        l1 = Location.objects.create(latitude=25.04035, longitude=121.557294,address="台北市大安區光復南路260巷5號")
        l2 = Location.objects.create(latitude=25.03928, longitude=121.556213,address="台北市大安區光復南路290巷27號")
        l3 = Location.objects.create(latitude=25.040254, longitude=121.555074,address="台北市大安區光復南路260巷51-1號")
        l4 = Location.objects.create(latitude=25.038662, longitude=121.556807,address="光復南路346巷24號")
        l5 = Location.objects.create(latitude=25.038968, longitude=121.555484,address="台北市大安區光復南路308巷42號")
        l6 = Location.objects.create(latitude=25.040181, longitude=121.556895,address="台北市大安區光復南路260巷1號")

        m1 = Meal.objects.create(name="鮭魚義大利細麵", photo="../../static/ui/photos/spagetti.png")
        m2 = Meal.objects.create(name="火腿凱薩沙拉", photo="../../static/ui/photos/hamsalad.png")
        m3 = Meal.objects.create(name="酥皮濃湯", photo="../../static/ui/photos/peesoup.jpg")
        m4 = Meal.objects.create(name="日式明太子煎蛋捲", photo="../../static/ui/photos/eggnut.jpg")
        m5 = Meal.objects.create(name="日式味增拉麵", photo="../../static/ui/photos/lamien.jpg")
        m6 = Meal.objects.create(name="大阪燒", photo="../../static/ui/photos/daiban.jpg")
        m7 = Meal.objects.create(name="西班牙燉飯", photo="../../static/ui/photos/spainrice.jpg")
        m8 = Meal.objects.create(name="西班牙烘蛋", photo="../../static/ui/photos/spainegg.jpg")
        m9 = Meal.objects.create(name="韓式部隊鍋", photo="../../static/ui/photos/koreanspot.jpg")
        m10 = Meal.objects.create(name="韓式泡菜蘿蔔糕", photo="../../static/ui/photos/koreancake.jpg")
        m11 = Meal.objects.create(name="香煎法式里肌排", photo="../../static/ui/photos/frechpork.jpg")
        m12 = Meal.objects.create(name="鮭魚生魚片蓋飯", photo="../../static/ui/photos/fishrice.jpg")
        m13 = Meal.objects.create(name="醋嫩鱈魚肝", photo="../../static/ui/photos/fishgan.jpg")

        d1 = datetime.datetime(2015, 2, 1, 12, 00, 00)
        d2 = datetime.datetime(2015, 2, 1, 19, 00, 00)
        d3 = datetime.datetime(2015, 2, 2, 12, 00, 00)
        d4 = datetime.datetime(2015, 2, 2, 19, 00, 00)
        d5 = datetime.datetime(2015, 2, 3, 12, 00, 00)
        d6 = datetime.datetime(2015, 2, 3, 19, 00, 00)
        d7 = datetime.datetime(2015, 2, 4, 12, 00, 00)
        d8 = datetime.datetime(2015, 2, 4, 19, 00, 00)
        django.setup()

        t1 = Table.objects.create(
                host=aaron,
                attendance_num=0,
                available_num=4,
                #menu = m1,
                price = 240,
                datetime = d1,
                location = l1,
                description = "我們使用義大利進口的義大利麵、起司烹調傳統義式廚房料理, 希望能與大家共襄盛舉",
                title = "托斯卡尼義式傳統料理",
                photo="../../static/ui/photos/aaron_home.jpg",
                pet = True,
                smoking = True,
                wine = False,
                )
        t1.menu.add(m1, m2,m3)

        t7 = Table.objects.create(
                host=aaron,
                attendance_num=0,
                available_num=4,
                #menu = m1,
                price = 240,
                datetime = d5,
                location = l1,
                description = "我們使用義大利進口的義大利麵、起司烹調傳統義式廚房料理, 希望能與大家共襄盛舉",
                title = "托斯卡尼義式傳統料理",
                photo="../../static/ui/photos/aaron_home.jpg",
                pet = True,
                smoking = True,
                wine = False,
                )
        t7.menu.add(m1,m2,m3)

        t2 = Table.objects.create(
                host = baird,
                attendance_num = 0,
                available_num = 3,
                #menu =m4,
                price = 320,
                datetime = d2,
                location = l2,
                description = "我是來台旅居多年的日本人,希望和風料理能夠帶給大家感動與溫暖",
                title = "隱藏巷內的日式和風家庭料理",
                photo="../../static/ui/photos/bairdhome.jpg",
                pet = False,
                smoking = False,
                wine = False,
                )
        t2.menu.add(m4, m5, m6)
        t8 = Table.objects.create(
                host = baird,
                attendance_num = 0,
                available_num = 3,
                #menu =m4,
                price = 320,
                datetime = d4,
                location = l2,
                description = "我是來台旅居多年的日本人,希望和風料理能夠帶給大家感動與溫暖",
                title = "隱藏巷內的日式和風家庭料理",
                photo="../../static/ui/photos/bairdhome.jpg",
                pet = False,
                smoking = False,
                wine = False,
                )
        t8.menu.add(m4, m5, m6)

        t3 = Table.objects.create(
                host=caesar,
                attendance_num=0,
                available_num=5,
                #menu =m7,
                price =400,
                datetime = d3,
                location = l3,
                description = "我喜歡西班牙料理，朋友之前從西班牙帶了一個Paella鍋給我，大概可以餵飽6個人吧! 一起來開party吧~?",
                title = "熱情洋溢西班牙大餐",
                photo="../../static/ui/photos/caesarhome.jpg",
                pet = True,
                smoking = True,
                wine = False,
                )
        t3.menu.add(m7,m8)
        t9 = Table.objects.create(
                host=caesar,
                attendance_num=0,
                available_num=5,
                #menu =m7,
                price =400,
                datetime = d2,
                location = l3,
                description = "我喜歡西班牙料理，朋友之前從西班牙帶了一個Paella鍋給我，大概可以餵飽6個人吧! 一起來開party吧~?",
                title = "熱情洋溢西班牙大餐",
                photo="../../static/ui/photos/caesarhome.jpg",
                pet = True,
                smoking = True,
                wine = False,
                )
        t9.menu.add(m7, m8)

        t4 = Table.objects.create(
                host=dana,
                attendance_num=0,
                available_num=2,
                #menu = m9,
                price =300,
                datetime = d4,
                location = l4,
                description = "冬天就是要來一鍋這種熱熱辣辣的火鍋才溫暖",
                title = "熱滾滾的韓式部隊鍋",
                photo="../../static/ui/photos/danahome.jpg",
                pet = False,
                smoking = False,
                wine = False,
                )
        t4.menu.add(m9, m10)

        t10 = Table.objects.create(
                host=dana,
                attendance_num=0,
                available_num=2,
                #menu = m9,
                price =300,
                datetime = d7,
                location = l4,
                description = "冬天就是要來一鍋這種熱熱辣辣的火鍋才溫暖",
                title = "熱滾滾的韓式部隊鍋",
                photo="../../static/ui/photos/danahome.jpg",
                pet = False,
                smoking = False,
                wine = False,
                )
        t10.menu.add(m9,m10)

        t5 = Table.objects.create(
                host=ada,
                attendance_num=0,
                available_num=2,
                #menu = m11,
                price = 450,
                datetime = d7,
                location = l5,
                description = "我是崇尚浪漫與自然的女生,希望與大家度過一個溫馨的夜晚",
                title = "浪漫巴黎料理",
                photo="../../static/ui/photos/adahome.jpg",
                pet = False ,
                smoking = False,
                wine = False,
                )
        t5.menu.add(m11)

        t11 = Table.objects.create(
                host=ada,
                attendance_num=0,
                available_num=2,
                #menu = m11,
                price = 450,
                datetime = d5,
                location = l5,
                description = "我是崇尚浪漫與自然的女生,希望與大家度過一個溫馨的夜晚",
                title = "浪漫巴黎料理",
                photo="../../static/ui/photos/adahome.jpg",
                pet = False ,
                smoking = False,
                wine = False,
                )
        t11.menu.add(m11)

        t6 = Table.objects.create(
                host=barbara,
                attendance_num=0,
                available_num=3,
                #menu =m12,
                price =320,
                datetime = d6,
                location = l6,
                description ="大海是生命的起源,讓我們重回母親的懷抱吧",
                title = "想念嗎！大海的味道",
                photo="../../static/ui/photos/bbhome.jpg",
                pet = True,
                smoking = True,
                wine = False,
                )
        t6.menu.add(m12,m13)

        t12 = Table.objects.create(
                host=barbara,
                attendance_num=0,
                available_num=3,
                #menu =m12,
                price =320,
                datetime = d8,
                location = l6,
                description ="大海是生命的起源,讓我們重回母親的懷抱吧",
                title = "想念嗎！大海的味道",
                photo="../../static/ui/photos/bbhome.jpg",
                pet = True,
                smoking = True,
                wine = False,
                )
        t12.menu.add(m12,m13)
    def get_expected_response_body(self):
        expected = "{\"count\":12,\"next\":\"http:\/\/testserver\/api\/tables\/?page=2\",\"previous\":null,\"results\":[{\"host\":{\"id\":1,\"name\":\"Aaron\",\"contact_number\":\"939123456\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/nsg98icvvuzcw5e\/aaron%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":4,\"attendance\":[],\"menu\":[{\"id\":1,\"name\":\"鮭魚義大利細麵\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/spagetti.png\"},{\"id\":2,\"name\":\"火腿凱薩沙拉\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/hamsalad.png\"},{\"id\":3,\"name\":\"酥皮濃湯\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/peesoup.jpg\"}],\"price\":240,\"datetime\":\"2015-02-01T12:00:00Z\",\"location\":{\"id\":1,\"latitude\":25.04035,\"longitude\":121.557294,\"address\":\"台北市大安區光復南路260巷5號\"},\"description\":\"我們使用義大利進口的義大利麵、起司烹調傳統義式廚房料理, 希望能與大家共襄盛舉\",\"title\":\"托斯卡尼義式傳統料理\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/aaron_home.jpg\",\"pet\":true,\"smoking\":true,\"wine\":false},{\"host\":{\"id\":1,\"name\":\"Aaron\",\"contact_number\":\"939123456\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/nsg98icvvuzcw5e\/aaron%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":4,\"attendance\":[],\"menu\":[{\"id\":1,\"name\":\"鮭魚義大利細麵\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/spagetti.png\"},{\"id\":2,\"name\":\"火腿凱薩沙拉\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/hamsalad.png\"},{\"id\":3,\"name\":\"酥皮濃湯\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/peesoup.jpg\"}],\"price\":240,\"datetime\":\"2015-02-03T12:00:00Z\",\"location\":{\"id\":1,\"latitude\":25.04035,\"longitude\":121.557294,\"address\":\"台北市大安區光復南路260巷5號\"},\"description\":\"我們使用義大利進口的義大利麵、起司烹調傳統義式廚房料理, 希望能與大家共襄盛舉\",\"title\":\"托斯卡尼義式傳統料理\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/aaron_home.jpg\",\"pet\":true,\"smoking\":true,\"wine\":false},{\"host\":{\"id\":2,\"name\":\"Baird\",\"contact_number\":\"918234567\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropbox.com\/s\/3pb2568jhwge0n0\/Baird%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":3,\"attendance\":[],\"menu\":[{\"id\":4,\"name\":\"日式明太子煎蛋捲\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/eggnut.jpg\"},{\"id\":5,\"name\":\"日式味增拉麵\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/lamien.jpg\"},{\"id\":6,\"name\":\"大阪燒\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/daiban.jpg\"}],\"price\":320,\"datetime\":\"2015-02-01T19:00:00Z\",\"location\":{\"id\":2,\"latitude\":25.03928,\"longitude\":121.556213,\"address\":\"台北市大安區光復南路290巷27號\"},\"description\":\"我是來台旅居多年的日本人,希望和風料理能夠帶給大家感動與溫暖\",\"title\":\"隱藏巷內的日式和風家庭料理\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/bairdhome.jpg\",\"pet\":false,\"smoking\":false,\"wine\":false},{\"host\":{\"id\":2,\"name\":\"Baird\",\"contact_number\":\"918234567\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropbox.com\/s\/3pb2568jhwge0n0\/Baird%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":3,\"attendance\":[],\"menu\":[{\"id\":4,\"name\":\"日式明太子煎蛋捲\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/eggnut.jpg\"},{\"id\":5,\"name\":\"日式味增拉麵\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/lamien.jpg\"},{\"id\":6,\"name\":\"大阪燒\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/daiban.jpg\"}],\"price\":320,\"datetime\":\"2015-02-02T19:00:00Z\",\"location\":{\"id\":2,\"latitude\":25.03928,\"longitude\":121.556213,\"address\":\"台北市大安區光復南路290巷27號\"},\"description\":\"我是來台旅居多年的日本人,希望和風料理能夠帶給大家感動與溫暖\",\"title\":\"隱藏巷內的日式和風家庭料理\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/bairdhome.jpg\",\"pet\":false,\"smoking\":false,\"wine\":false},{\"host\":{\"id\":3,\"name\":\"Caesar\",\"contact_number\":\"910345678\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/r9q9kwsett0j096\/Caesar%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":5,\"attendance\":[],\"menu\":[{\"id\":7,\"name\":\"西班牙燉飯\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/spainrice.jpg\"},{\"id\":8,\"name\":\"西班牙烘蛋\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/spainegg.jpg\"}],\"price\":400,\"datetime\":\"2015-02-02T12:00:00Z\",\"location\":{\"id\":3,\"latitude\":25.040254,\"longitude\":121.555074,\"address\":\"台北市大安區光復南路260巷51-1號\"},\"description\":\"我喜歡西班牙料理，朋友之前從西班牙帶了一個Paella鍋給我，大概可以餵飽6個人吧! 一起來開party吧~?\",\"title\":\"熱情洋溢西班牙大餐\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/caesarhome.jpg\",\"pet\":true,\"smoking\":true,\"wine\":false},{\"host\":{\"id\":3,\"name\":\"Caesar\",\"contact_number\":\"910345678\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/r9q9kwsett0j096\/Caesar%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":5,\"attendance\":[],\"menu\":[{\"id\":7,\"name\":\"西班牙燉飯\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/spainrice.jpg\"},{\"id\":8,\"name\":\"西班牙烘蛋\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/spainegg.jpg\"}],\"price\":400,\"datetime\":\"2015-02-01T19:00:00Z\",\"location\":{\"id\":3,\"latitude\":25.040254,\"longitude\":121.555074,\"address\":\"台北市大安區光復南路260巷51-1號\"},\"description\":\"我喜歡西班牙料理，朋友之前從西班牙帶了一個Paella鍋給我，大概可以餵飽6個人吧! 一起來開party吧~?\",\"title\":\"熱情洋溢西班牙大餐\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/caesarhome.jpg\",\"pet\":true,\"smoking\":true,\"wine\":false},{\"host\":{\"id\":4,\"name\":\"Dana\",\"contact_number\":\"921456789\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/02g7b9lpydfi1gw\/Dana%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":2,\"attendance\":[],\"menu\":[{\"id\":9,\"name\":\"韓式部隊鍋\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/koreanspot.jpg\"},{\"id\":10,\"name\":\"韓式泡菜蘿蔔糕\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/koreancake.jpg\"}],\"price\":300,\"datetime\":\"2015-02-02T19:00:00Z\",\"location\":{\"id\":4,\"latitude\":25.038662,\"longitude\":121.556807,\"address\":\"光復南路346巷24號\"},\"description\":\"冬天就是要來一鍋這種熱熱辣辣的火鍋才溫暖\",\"title\":\"熱滾滾的韓式部隊鍋\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/danahome.jpg\",\"pet\":false,\"smoking\":false,\"wine\":false},{\"host\":{\"id\":4,\"name\":\"Dana\",\"contact_number\":\"921456789\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/02g7b9lpydfi1gw\/Dana%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":2,\"attendance\":[],\"menu\":[{\"id\":9,\"name\":\"韓式部隊鍋\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/koreanspot.jpg\"},{\"id\":10,\"name\":\"韓式泡菜蘿蔔糕\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/koreancake.jpg\"}],\"price\":300,\"datetime\":\"2015-02-04T12:00:00Z\",\"location\":{\"id\":4,\"latitude\":25.038662,\"longitude\":121.556807,\"address\":\"光復南路346巷24號\"},\"description\":\"冬天就是要來一鍋這種熱熱辣辣的火鍋才溫暖\",\"title\":\"熱滾滾的韓式部隊鍋\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/danahome.jpg\",\"pet\":false,\"smoking\":false,\"wine\":false},{\"host\":{\"id\":5,\"name\":\"Ada\",\"contact_number\":\"910345678\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/ubo1ay8k9452urm\/Ada%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":2,\"attendance\":[],\"menu\":[{\"id\":11,\"name\":\"香煎法式里肌排\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/frechpork.jpg\"}],\"price\":450,\"datetime\":\"2015-02-04T12:00:00Z\",\"location\":{\"id\":5,\"latitude\":25.038968,\"longitude\":121.555484,\"address\":\"台北市大安區光復南路308巷42號\"},\"description\":\"我是崇尚浪漫與自然的女生,希望與大家度過一個溫馨的夜晚\",\"title\":\"浪漫巴黎料理\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/adahome.jpg\",\"pet\":false,\"smoking\":false,\"wine\":false},{\"host\":{\"id\":5,\"name\":\"Ada\",\"contact_number\":\"910345678\",\"photo\":\"http:\/\/testserver\/api\/tables\/https%3A\/\/dl.dropboxusercontent.com\/s\/ubo1ay8k9452urm\/Ada%25E7%259A%2584%25E5%25AE%25B6.jpg%3Fdl%3D0\"},\"attendance_num\":0,\"available_num\":2,\"attendance\":[],\"menu\":[{\"id\":11,\"name\":\"香煎法式里肌排\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/frechpork.jpg\"}],\"price\":450,\"datetime\":\"2015-02-03T12:00:00Z\",\"location\":{\"id\":5,\"latitude\":25.038968,\"longitude\":121.555484,\"address\":\"台北市大安區光復南路308巷42號\"},\"description\":\"我是崇尚浪漫與自然的女生,希望與大家度過一個溫馨的夜晚\",\"title\":\"浪漫巴黎料理\",\"photo\":\"http:\/\/testserver\/static\/ui\/photos\/adahome.jpg\",\"pet\":false,\"smoking\":false,\"wine\":false}]}"
        return "QQ"


    def trim(self,data):
        return "QQ"
