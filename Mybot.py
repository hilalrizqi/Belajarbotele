import telebot
import mysql.connector

import mytoken

from datetime import date
from datetime import datetime

TOKEN = mytoken.TOKEN
mybot = telebot.TeleBot(TOKEN)
mydb = mysql.connector.connect(host='localhost',user='root',database='db_starbot')
sql = mydb.cursor()
from  telebot import apihelper
waktusekarang = datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @mybot.message_handler(commands=['start','help'])
    def start(message):
        photo = open('img/starbot.jpg', 'rb')
        mybot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n-- admin & developer @Hilalrizqi - SMK TARUNA BHAKTI -- "+"\n" \
                                "hari ini tanggal"+str(waktusekarang)
        mybot.reply_to(message, teks)

    @mybot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd, nama, kelas from tabel_siswa "
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if(jmldata>0):
                #print(data)
                no = 0
                for x in data:
                    no += 1
                    kumpuldata = kumpuldata + str(x) + "\n"
                    print(kumpuldata)
                    kumpuldata = kumpuldata.replace('(', '')
                    kumpuldata = kumpuldata.replace(')', '')
                    kumpuldata = kumpuldata.replace("'", '')
                    kumpuldata = kumpuldata.replace(",", '')
        else:
            print('datakosong')


        mybot.reply_to(message,str(kumpuldata))

print(mydb)
print("-- bot sedang berjalan --")
mybot.polling(none_stop=True)
