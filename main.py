# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sqlite3
class University():
    def __init__(self,name,country):
        self.name=name
        self.country=country
        self.status=True

        self.connectDatabase()

    def run(self):
        self.menu()
        chocie=self.chocie()

        if chocie==1:
            self.studentAdd()
        if chocie==2:
            self.studentDelete()
        if chocie==3:
            self.studentUpdate()
        if chocie==4:
            sec=int(input("1)Tüm öğrencileri listele\n2)Bölümelere göre listele\n3)Departmana göre listele\n4)Öğrenim Tipine göre listele\n5)Durumuna göre listele\nSeç:"))
            self.studentAllShow(sec)
        if chocie==5:
            self.Exit()

    def menu(self):
        print("*** {} Yönetim Sistemi ***".format(self.name))
        print("\n1)Öğrenci Ekle\n2)Öğrenci Sil\n3)Öğrenci Güncelle\n4)Öğrencileri Göster\n5)Çıkış")
    def chocie(self):
        while True:
            try:
                choice=int(input("Yapmak İstediğiniz İşlemi Seçiniz:"))
                if choice>=1 and choice<=5:
                    return choice
                else:
                    print("Lütfen 1-5 arası seçim yapınız!!!")
            except ValueError:
                print("Lütfen 1-5 arası seçim yapınız!!!")
    def studentAdd(self):
        print("*** Öğrenci Kayıt ***\n")
        ad=input("İsim :").lower().capitalize()
        soyad=input("Soyisim:").lower().capitalize()
        fakulte=input("Fakülte:").lower().capitalize()
        departman=input("Departman:").lower().capitalize()
        no=input("Öğrenci Numara:")

        while True:
            try:
                ögrenim=int(input("Öğretim Türü:"))
                if ögrenim<1 or ögrenim>2:
                    print("1-2 arası değer giriniz")
                    continue
                break
            except ValueError:
                print("1-2 arasında seçim yapınız!!!")

        durum="aktif"
        self.cursor.execute("INSERT INTO student VALUES('{}','{}','{}','{}','{}',{},'{}')".format(ad,soyad,fakulte,departman,no,ögrenim,durum))
        self.connect.commit()
        print("{} {} öğrenci  kaydedildi!".format(ad,soyad))


    def connectDatabase(self):
        self.connect=sqlite3.connect("EGE.db")
        self.cursor=self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student(ad TEXT,soyad TEXT,fakülte TEXT,departman TEXT,no TEXT,öğrenim INT,durum TEXT)")

        self.connect.commit()

    def studentControl(self):
        pass
    def studentDelete(self):
        self.cursor.execute("SELECT * FROM student")
        allstudents=self.cursor.fetchall()

        convertstudent=lambda x: [str(y) for y in x]

        for sayi,student in enumerate(allstudents,1):
            print("{})".format(sayi)," ".join(convertstudent(student)))
        while True:
            try:
                secim=int(input("Silmek İstediğiniz öğrenci id giriniz:"))
                break
            except ValueError:
                print("Lütfen sayı giriniz!!!")

        self.cursor.execute("DELETE FROM student WHERE rowid={}".format(secim))
        self.connect.commit()
        print("{} id numaralı öğrenci silinmiştir! ".format(secim))

    def studentUpdate(self):
        self.cursor.execute("SELECT * FROM student")
        students=self.cursor.fetchall()

        convertstudent=lambda x:[str(y) for y in x]

        for sayi,student in enumerate(students,1):
            print("{})".format(sayi)," ".join(convertstudent(student)))
        while True:
            try:
                secim=int(input("Güncelleme yapmak istediğniz öğrencinin id'sini giriniz:"))
                break
            except ValueError:
                print("Lütfen id giriniz!!!")
        while True:
            try:
                updateselect=int(input("1)Ad\n2)Soyad\n3)Fakülte\n4)Departman\n5)Numara\n6)Öğrenim Türü\n7)Durum\nSeçim:"))
                if updateselect<1 or updateselect>7:
                    print("1-7 arasında seçim yapınız!!!")
                    continue
                break
            except ValueError:
                print("1-7 arasında seçim yapınız!!!")
        opration=["ad","soyad","fakülte","departman","no","öğrenim","durum"]
        if updateselect==6:
            while True:
                try:
                    newValue=int(input("Yeni değeri giriniz:"))
                    if newValue not in(1,2):
                        continue
                    break
                except ValueError:
                    print("1-2 arasında değer giriniz!!!")

            self.cursor.execute("UPDATE student SET öğrenim={} WHERE rowid={}".format(newValue,secim))
        else:
            newValue=input("Yeni değeri giriniz:")
            self.cursor.execute("UPDATE student SET {}='{}' WHERE rowid={}".format(opration[updateselect-1],newValue,secim))
        print("Bilgiler başarıyla güncellendi!!!")
        self.connect.commit()



    def studentAllShow(self,sec):
        if sec==1:
            self.cursor.execute("SELECT * FROM student")

            allstudent=self.cursor.fetchall()

            convertstudent=lambda x: [str(y) for y in x]

            for sayi,student in enumerate(allstudent,1):
                print("{})".format(sayi)," ".join(convertstudent(student)))

        if sec==2:
            self.cursor.execute("SELECT fakülte FROM student")

            fakulteler=list(enumerate(list(set(self.cursor.fetchall())),1))

            for sayi,fakulte in fakulteler:
                print("{}){}".format(sayi,fakulte[0]))

            while True:
                try:
                    choice=int(input("(1-{}) Arsında Seçiniz:".format(sayi)))
                    if choice<1 or choice>sayi:
                        print("Tekrar deneyiniz!!!")
                        continue
                    break
                except ValueError:
                    print("Yanlış seçim tekrar deneyiniz!!!")

            self.cursor.execute("SELECT * FROM student WHERE fakülte='{}'".format(fakulteler[choice-1][1][0]))

            allstudent=self.cursor.fetchall()

            convertstudent = lambda x: [str(y) for y in x]

            for sayi, student in enumerate(allstudent, 1):
                print("{})".format(sayi), " ".join(convertstudent(student)))
        if sec==3:
            self.cursor.execute("SELECT departman FROM student")

            departmanlar = list(enumerate(list(set(self.cursor.fetchall())), 1))

            for sayi, departman in departmanlar:
                print("{}){}".format(sayi, departman[0]))

            while True:
                try:
                    choice = int(input("(1-{}) Arsında Seçiniz:".format(sayi)))
                    if choice < 1 or choice > sayi:
                        print("Tekrar deneyiniz!!!")
                        continue
                    break
                except ValueError:
                    print("Yanlış seçim tekrar deneyiniz!!!")

            self.cursor.execute("SELECT * FROM student WHERE departman='{}'".format(departmanlar[choice - 1][1][0]))

            allstudent = self.cursor.fetchall()

            convertstudent = lambda x: [str(y) for y in x]

            for sayi, student in enumerate(allstudent, 1):
                print("{})".format(sayi), " ".join(convertstudent(student)))

        if sec==4:
            self.cursor.execute("SELECT öğrenim FROM student")

            ogrenimler = list(enumerate(list(set(self.cursor.fetchall())), 1))

            for sayi, ogrenim in ogrenimler:
                print("{}){}".format(sayi, ogrenim[0]))

            while True:
                try:
                    choice = int(input("(1-{}) Arsında Seçiniz:".format(sayi)))
                    if choice < 1 or choice > sayi:
                        print("Tekrar deneyiniz!!!")
                        continue
                    break
                except ValueError:
                    print("Yanlış seçim tekrar deneyiniz!!!")

            self.cursor.execute("SELECT * FROM student WHERE öğrenim='{}'".format(ogrenimler[choice - 1][1][0]))

            allstudent = self.cursor.fetchall()

            convertstudent = lambda x: [str(y) for y in x]

            for sayi, student in enumerate(allstudent, 1):
                print("{})".format(sayi), " ".join(convertstudent(student)))

        if sec==5:
            self.cursor.execute("SELECT durum FROM student")

            durumlar = list(enumerate(list(set(self.cursor.fetchall())), 1))

            for sayi, durum in durumlar:
                print("{}){}".format(sayi, durum[0]))

            while True:
                try:
                    choice = int(input("(1-{}) Arsında Seçiniz:".format(sayi)))
                    if choice < 1 or choice > sayi:
                        print("Tekrar deneyiniz!!!")
                        continue
                    break
                except ValueError:
                    print("Yanlış seçim tekrar deneyiniz!!!")

            self.cursor.execute("SELECT * FROM student WHERE durum='{}'".format(durumlar[choice - 1][1][0]))

            allstudent = self.cursor.fetchall()

            convertstudent = lambda x: [str(y) for y in x]

            for sayi, student in enumerate(allstudent, 1):
                print("{})".format(sayi), " ".join(convertstudent(student)))


    def Exit(self):
        self.status = False
EGE=University("Ege Üniversitesi","Türkiye")
while EGE.status:
    EGE.run()
