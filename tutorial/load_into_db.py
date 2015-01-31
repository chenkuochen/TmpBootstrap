# coding=utf-8
import csv
import os
import sys
import time
import django

import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")

from restfulAPI.models import Person, Meal, Location, Table
#f = open('data/table.csv', 'r')
#for row in csv.DictReader(f, ["Host","AttendanceNum","Attendance","Menu","Price","Datetime:","latitude?","longitude","Description","Title","Gallery","Pet","Smoking","Wine","Type"]):
#    print row['Datetime:']
#f.close()

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

m1 = Meal.objects.create(name="鮭魚義大利細麵", photo="https://dl.dropboxusercontent.com/s/a6dfojge7gp4pa1/%E9%AE%AD%E9%AD%9A%E7%BE%A9%E5%A4%A7%E5%88%A9%E7%B4%B0%E9%BA%B5.png?dl=0")
m2 = Meal.objects.create(name="火腿凱薩沙拉", photo="https://dl.dropboxusercontent.com/s/89h1cnt0ue9cm2b/%E7%81%AB%E8%85%BF%E5%87%B1%E8%96%A9%E6%B2%99%E6%8B%89.png?dl=0")
m3 = Meal.objects.create(name="酥皮濃湯", photo="https://dl.dropboxusercontent.com/s/lk1jv5yafzllm01/%E9%85%A5%E7%9A%AE%E6%BF%83%E6%B9%AF.jpg?dl=0")
m4 = Meal.objects.create(name="日式明太子煎蛋捲", photo="https://dl.dropboxusercontent.com/s/wq5br0wpx2qto80/%E6%97%A5%E5%BC%8F%E6%98%8E%E5%A4%AA%E5%AD%90%E7%85%8E%E8%9B%8B%E5%8D%B7.jpg?dl=0")
m5 = Meal.objects.create(name="日式味增拉麵", photo="https://dl.dropboxusercontent.com/s/xdrxmb5bd5141lh/%E6%97%A5%E5%BC%8F%E5%91%B3%E5%A2%9E%E6%8B%89%E9%BA%B5.jpg?dl=0")
m6 = Meal.objects.create(name="大阪燒", photo="https://dl.dropboxusercontent.com/s/06im19n2y7lqfqs/%E5%A4%A7%E9%98%AA%E7%87%92.jpg?dl=2")
m7 = Meal.objects.create(name="西班牙燉飯", photo="https://dl.dropboxusercontent.com/s/pbz7ndsjv1bg4h1/%E8%A5%BF%E7%8F%AD%E7%89%99%E6%B5%B7%E9%AE%AE%E7%87%89%E9%A3%AF.jpg?dl=4")
m8 = Meal.objects.create(name="西班牙烘蛋", photo="https://dl.dropboxusercontent.com/s/dbh8qi1jszzfbjd/%E8%A5%BF%E7%8F%AD%E7%89%99%E7%83%98%E8%9B%8B.jpg?dl=0")
m9 = Meal.objects.create(name="韓式部隊鍋", photo="https://dl.dropboxusercontent.com/s/9mzt3iuqpg1w26j/%E9%9F%93%E5%BC%8F%E9%83%A8%E9%9A%8A%E9%8D%8B.jpg?dl=0")
m10 = Meal.objects.create(name="韓式泡菜蘿蔔糕", photo="https://dl.dropboxusercontent.com/s/dujs9pvjzgot0y8/%E9%9F%93%E5%BC%8F%E6%B3%A1%E8%8F%9C%E8%98%BF%E8%94%94%E7%B3%95.jpg?dl=0")
m11 = Meal.objects.create(name="香煎法式里肌排", photo="https://dl.dropboxusercontent.com/s/p3b3b242d5kqnfj/%E9%A6%99%E7%85%8E%E6%B3%95%E5%BC%8F%E9%87%8C%E8%82%8C%E6%8E%92.jpg?dl=0")
m12 = Meal.objects.create(name="鮭魚生魚片蓋飯", photo="https://dl.dropboxusercontent.com/s/b1o3ox045p6rsxi/%E9%AE%AD%E9%AD%9A%E7%94%9F%E9%AD%9A%E7%89%87%E8%93%8B%E9%A3%AF.jpg?dl=0")
m13 = Meal.objects.create(name="醋嫩鱈魚肝", photo="https://DL.dropbox.com/s/a8cqys7vj777ej0/%E9%86%8B%E5%AB%A9%E9%B1%88%E9%AD%9A%E8%82%9D.jpg?dl=0")

d1 = datetime.datetime(2015, 1, 30, 12, 00, 00)
d2 = datetime.datetime(2015, 1, 30, 19, 00, 00)
d3 = datetime.datetime(2015, 1, 31, 12, 00, 00)
d4 = datetime.datetime(2015, 1, 31, 19, 00, 00)
d5 = datetime.datetime(2015, 2, 1, 12, 00, 00)
d6 = datetime.datetime(2015, 2, 1, 19, 00, 00)
d7 = datetime.datetime(2015, 2, 2, 12, 00, 00)
d8 = datetime.datetime(2015, 2, 2, 19, 00, 00)
django.setup()

t1 = Table.objects.create(
                          host=aaron,
                          attendance_num=4,
                          available_num=4,
                          #menu = m1,
                          price = 240,
                          datetime = d1,
                          location = l1,
                          description = "我們使用義大利進口的義大利麵、起司烹調傳統義式廚房料理, 希望能與大家共襄盛舉",
                          title = "托斯卡尼義式傳統料理",
                          photo = "https://dl.dropbox.com/s/a6dfojge7gp4pa1/%E9%AE%AD%E9%AD%9A%E7%BE%A9%E5%A4%A7%E5%88%A9%E7%B4%B0%E9%BA%B5.png?dl=0",
                          pet = True,
                          smoking = True,
                          wine = False,
                          )
t1.menu.add(m1, m2,m3)

t7 = Table.objects.create(
                          host=aaron,
                          attendance_num=4,
                          available_num=4,
                          #menu = m1,
                          price = 240,
                          datetime = d5,
                          location = l1,
                          description = "我們使用義大利進口的義大利麵、起司烹調傳統義式廚房料理, 希望能與大家共襄盛舉",
                          title = "托斯卡尼義式傳統料理",
                          photo = "https://dl.dropbox.com/s/a6dfojge7gp4pa1/%E9%AE%AD%E9%AD%9A%E7%BE%A9%E5%A4%A7%E5%88%A9%E7%B4%B0%E9%BA%B5.png?dl=0",
                          pet = True,
                          smoking = True,
                          wine = False,
                          )
t7.menu.add(m1,m2,m3)

t2 = Table.objects.create(
                          host = baird,
                          attendance_num = 3,
                          available_num = 3,
                          #menu =m4,
                          price = 320,
                          datetime = d2,
                          location = l2,
                          description = "我是來台旅居多年的日本人,希望和風料理能夠帶給大家感動與溫暖",
                          title = "隱藏巷內的日式和風家庭料理",
                          photo = "https://dl.dropboxusercontent.com/s/wq5br0wpx2qto80/%E6%97%A5%E5%BC%8F%E6%98%8E%E5%A4%AA%E5%AD%90%E7%85%8E%E8%9B%8B%E5%8D%B7.jpg?dl=0",
                          pet = False,
                          smoking = False,
                          wine = False,
                          )
t2.menu.add(m4, m5, m6)
t8 = Table.objects.create(
                          host = baird,
                          attendance_num = 3,
                          available_num = 3,
                          #menu =m4,
                          price = 320,
                          datetime = d4,
                          location = l2,
                          description = "我是來台旅居多年的日本人,希望和風料理能夠帶給大家感動與溫暖",
                          title = "隱藏巷內的日式和風家庭料理",
                          photo = "https://dl.dropboxusercontent.com/s/wq5br0wpx2qto80/%E6%97%A5%E5%BC%8F%E6%98%8E%E5%A4%AA%E5%AD%90%E7%85%8E%E8%9B%8B%E5%8D%B7.jpg?dl=0",
                          pet = False,
                          smoking = False,
                          wine = False,
                          )
t8.menu.add(m4, m5, m6)

t3 = Table.objects.create(
                          host=caesar,
                          attendance_num=5,
                          available_num=5,
                          #menu =m7,
                          price =400,
                          datetime = d3,
                          location = l3,
                          description = "我喜歡西班牙料理，朋友之前從西班牙帶了一個Paella鍋給我，大概可以餵飽6個人吧! 一起來開party吧~?",
                          title = "熱情洋溢西班牙大餐",
                          photo = "https://dl.dropboxusercontent.com/s/pbz7ndsjv1bg4h1/%E8%A5%BF%E7%8F%AD%E7%89%99%E6%B5%B7%E9%AE%AE%E7%87%89%E9%A3%AF.jpg?dl=0",
                          pet = True,
                          smoking = True,
                          wine = False,
                          )
t3.menu.add(m7,m8)
t9 = Table.objects.create(
                          host=caesar,
                          attendance_num=5,
                          available_num=5,
                          #menu =m7,
                          price =400,
                          datetime = d2,
                          location = l3,
                          description = "我喜歡西班牙料理，朋友之前從西班牙帶了一個Paella鍋給我，大概可以餵飽6個人吧! 一起來開party吧~?",
                          title = "熱情洋溢西班牙大餐",
                          photo = "https://dl.dropboxusercontent.com/s/pbz7ndsjv1bg4h1/%E8%A5%BF%E7%8F%AD%E7%89%99%E6%B5%B7%E9%AE%AE%E7%87%89%E9%A3%AF.jpg?dl=0",
                          pet = True,
                          smoking = True,
                          wine = False,
                          )
t9.menu.add(m7, m8)

t4 = Table.objects.create(
                          host=dana,
                          attendance_num=2,
                          available_num=2,
                          #menu = m9,
                          price =300,
                          datetime = d4,
                          location = l4,
                          description = "冬天就是要來一鍋這種熱熱辣辣的火鍋才溫暖",
                          title = "熱滾滾的韓式部隊鍋",
                          photo = "https://dl.dropboxusercontent.com/s/9mzt3iuqpg1w26j/%E9%9F%93%E5%BC%8F%E9%83%A8%E9%9A%8A%E9%8D%8B.jpg?dl=0",
                          pet = False,
                          smoking = False,
                          wine = False,
                          )
t4.menu.add(m9, m10)

t10 = Table.objects.create(
                          host=dana,
                          attendance_num=2,
                          available_num=2,
                          #menu = m9,
                          price =300,
                          datetime = d7,
                          location = l4,
                          description = "冬天就是要來一鍋這種熱熱辣辣的火鍋才溫暖",
                          title = "熱滾滾的韓式部隊鍋",
                          photo = "https://dl.dropboxusercontent.com/s/9mzt3iuqpg1w26j/%E9%9F%93%E5%BC%8F%E9%83%A8%E9%9A%8A%E9%8D%8B.jpg?dl=0",
                          pet = False,
                          smoking = False,
                          wine = False,
                          )
t10.menu.add(m9,m10)

t5 = Table.objects.create(
                          host=ada,
                          attendance_num=2,
                          available_num=2,
                          #menu = m11,
                          price = 450,
                          datetime = d7,
                          location = l5,
                          description = "我是崇尚浪漫與自然的女生,希望與大家度過一個溫馨的夜晚",
                          title = "浪漫巴黎料理",
                          photo = "https://dl.dropboxusercontent.com/s/p3b3b242d5kqnfj/%E9%A6%99%E7%85%8E%E6%B3%95%E5%BC%8F%E9%87%8C%E8%82%8C%E6%8E%92.jpg?dl=0",
                          pet = False ,
                          smoking = False,
                          wine = False,
                          )
t5.menu.add(m11)

t11 = Table.objects.create(
                          host=ada,
                          attendance_num=2,
                          available_num=2,
                          #menu = m11,
                          price = 450,
                          datetime = d5,
                          location = l5,
                          description = "我是崇尚浪漫與自然的女生,希望與大家度過一個溫馨的夜晚",
                          title = "浪漫巴黎料理",
                          photo = "https://dl.dropboxusercontent.com/s/p3b3b242d5kqnfj/%E9%A6%99%E7%85%8E%E6%B3%95%E5%BC%8F%E9%87%8C%E8%82%8C%E6%8E%92.jpg?dl=0",
                          pet = False ,
                          smoking = False,
                          wine = False,
                          )
t11.menu.add(m11)

t6 = Table.objects.create(
                          host=barbara,
                          attendance_num=3,
                          available_num=3,
                          #menu =m12,
                          price =320,
                          datetime = d6,
                          location = l6,
                          description ="大海是生命的起源,讓我們重回母親的懷抱吧",
                          title = "想念嗎！大海的味道",
                          photo = "https://dl.dropboxusercontent.com/s/06im19n2y7lqfqs/%E5%A4%A7%E9%98%AA%E7%87%92.jpg?dl=4",
                          pet = True,
                          smoking = True,
                          wine = False,
                          )
t6.menu.add(m12,m13)

t12 = Table.objects.create(
                          host=barbara,
                          attendance_num=3,
                          available_num=3,
                          #menu =m12,
                          price =320,
                          datetime = d8,
                          location = l6,
                          description ="大海是生命的起源,讓我們重回母親的懷抱吧",
                          title = "想念嗎！大海的味道",
                          photo = "https://dl.dropboxusercontent.com/s/06im19n2y7lqfqs/%E5%A4%A7%E9%98%AA%E7%87%92.jpg?dl=4",
                          pet = True,
                          smoking = True,
                          wine = False,
                          )
t12.menu.add(m12,m13)
