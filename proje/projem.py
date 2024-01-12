import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget,QMessageBox
from pymongo import MongoClient

class Ilkekran(QDialog):
    def __init__(self):
        super(Ilkekran, self).__init__()
        loadUi("ilk.ui", self)
        self.Pushbutton.clicked.connect(self.gotoogrencigiris)
        self.ogretmengirisbuton.clicked.connect(self.gotoogretmengiris)

    def gotoogrencigiris(self):
        giris = OgrenciGiris()
        widget.addWidget(giris)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoogretmengiris(self):
        giris1 = OgretmenGiris()
        widget.addWidget(giris1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class OgrenciGiris(QDialog):
    def __init__(self):
        super(OgrenciGiris, self).__init__()
        loadUi("ögrenci.ui", self)
        self.ogrenicigirisbutton.clicked.connect(self.loginfunction)
        # MongoDB bağlantı bilgileri
        self.host = 'localhost'  # MongoDB sunucu adresi
        self.port = 27017  # MongoDB port numarası
        self.database_name = 'ogrencigiris'  # Kullanmak istediğiniz veritabanı adı

        # MongoDB'ye bağlanma
        self.client = MongoClient(self.host, self.port)

        # Veritabanını seçme veya oluşturma
        self.database = self.client[self.database_name]

        # Bağlantıyı test etmek için bir koleksiyon örneği alabilirsiniz
        self.collection_name = 'ogrencigiris'
        self.collection = self.database[self.collection_name]



    def loginfunction(self):
        numara = self.ogrenicinumara.text()
        sifre = self.ogrenicisifre.text()
        print("giriş başarılı Numara:", numara, "Şifre:", sifre)
        query = {'numara':numara,'sifre':sifre}
        print(query)
        found_document = self.collection.find_one(query)

        if found_document:
            print("Bulunan belge:", found_document)
            secim_ekrani = secimekran()
            secim_ekrani.exec_()
            self.close()


        else:
            # Hatalı giriş durumu
            QMessageBox.warning(self, 'Hata', 'Geçersiz numara veya şifre')

class OgretmenGiris(QDialog):
    def __init__(self):
        super(OgretmenGiris, self).__init__()
        loadUi("ögretmen.ui", self)
        self.ogretmenbutton.clicked.connect(self.loginfunction1)

    def loginfunction1(self):
        numara = self.ogretmennumara.text()
        sifre = self.ogretmensifre.text()
        print("giriş başarılı Numara:", numara, "Şifre:", sifre)


class secimekran(QDialog):
    def __init__(self):
        super(secimekran, self).__init__()
        loadUi("secim.ui", self)
        self.videobuton.clicked.connect(self.gotovideo)
        self.sorubuton.clicked.connect(self.gotosoru)



    def gotosoru(self):
        giris = soru()
        widget.addWidget(giris)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)
        self.hide()  # veya self.setVisible(False)

    def gotovideo(self):
        giris1 = video()
        widget.addWidget(giris1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)
        self.hide()  # Pencereyi gizle

class soru(QDialog):
    def __init__(self):
        super(soru, self).__init__()
        loadUi("ders.ui", self)
        self.pushButton.clicked.connect(self.gotofen)
        self.pushButton1.clicked.connect(self.gotohayat)
        self.pushButton2.clicked.connect(self.gotomat)
        self.pushButton3.clicked.connect(self.gototurkce)

    def gotofen(self):
        gidis = fen()
        widget.addWidget(gidis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotohayat(self):
        gidis2 = hayat()
        widget.addWidget(gidis2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotomat(self):
        gidis1 = mat()
        widget.addWidget(gidis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gototurkce(self):
        gidis3 = turkce()
        widget.addWidget(gidis3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)


class video(QDialog):
    def __init__(self):
        super(video, self).__init__()
        loadUi("ders.ui", self)
        self.pushButton.clicked.connect(self.gotofen)
        self.pushButton1.clicked.connect(self.gotohayat)
        self.pushButton2.clicked.connect(self.gotomat)
        self.pushButton3.clicked.connect(self.gototurkce)
    def gotofen(self):
        gidis4 = fen1()
        widget.addWidget(gidis4)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotohayat(self):
        gidis6 = hayat1()
        widget.addWidget(gidis6)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotomat(self):
        gidis5 = mat1()
        widget.addWidget(gidis5)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gototurkce(self):
        gidis7 = turkce1()
        widget.addWidget(gidis7)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)


class fen(QDialog):
    def __init__(self):
        super(fen,self).__init__()
        loadUi("fenkonu.ui",self)
        self.fenkonu1.clicked.connect(self.gotofenkonu1)
        self.fenkonu2.clicked.connect(self.gotofenkonu2)
        self.fenkonu3.clicked.connect(self.gotofenkonu3)
        self.fenkonu4.clicked.connect(self.gotofenkonu4)
    def gotofenkonu1(self):
        gelis=fenkonu1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotofenkonu2(self):
        gelis1 = fenkonu2()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)
    def gotofenkonu3(self):
        giris2=fenkonu3()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotofenkonu4(self):
        giris3=fenkonu4()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

class mat(QDialog):
    def __init__(self):
        super(mat,self).__init__()
        loadUi("matematikkonu.ui",self)
        self.matkonu1.clicked.connect(self.gotomatkonu1)
        self.matkonu2.clicked.connect(self.gotomatkonu2)
        self.matkonu3.clicked.connect(self.gotomatkonu3)
        self.matkonu4.clicked.connect(self.gotomatkonu4)

    def gotomatkonu1(self):
        gelis = matkonu1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotomatkonu2(self):
        gelis1 = matkonu2()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotomatkonu3(self):
        giris2 = matkonu3()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotomatkonu4(self):
        giris3 = matkonu4()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

class turkce(QDialog):
    def __init__(self):
        super(turkce,self).__init__()
        loadUi("turkcekonu.ui",self)
        self.turkcekonu1.clicked.connect(self.gototurkcekonu1)
        self.turkcekonu2.clicked.connect(self.gototurkcekonu2)
        self.turkcekonu3.clicked.connect(self.gototurkcekonu3)
        self.turkcekonu4.clicked.connect(self.gototurkcekonu4)

    def gototurkcekonu1(self):
        gelis = turkcekonu1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gototurkcekonu2(self):
        gelis1 = turkcekonu2()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gototurkcekonu3(self):
        giris2 = turkcekonu3()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gototurkcekonu4(self):
        giris3 = turkcekonu4()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

class hayat(QDialog):
    def __init__(self):
        super(hayat,self).__init__()
        loadUi("hayatbilgisikonu.ui",self)
        self.hayatkonu1.clicked.connect(self.gotohayatkonu1)
        self.hayatkonu2.clicked.connect(self.gotohayatkonu2)
        self.hayatkonu3.clicked.connect(self.gotohayatkonu3)
        self.hayatkonu4.clicked.connect(self.gotohayatkonu4)

    def gotohayatkonu1(self):
        gelis = hayatkonu1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotohayatkonu2(self):
        gelis1 = hayatkonu2()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotohayatkonu3(self):
        giris2 = hayatkonu3()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

    def gotohayatkonu4(self):
        giris3 = hayatkonu4()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(760)
        widget.setFixedHeight(820)

class fen1(QDialog):
    def __init__(self):
        super(fen1,self).__init__()
        loadUi("fenkonu.ui",self)
        self.fenkonu1.clicked.connect(self.gotofen1konu1)
        self.fenkonu2.clicked.connect(self.gotofen1konu2)
        self.fenkonu3.clicked.connect(self.gotofen1konu3)
        self.fenkonu4.clicked.connect(self.gotofen1konu4)

    def gotofen1konu1(self):
        gelis = video1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotofen1konu2(self):
        gelis1 = video1()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotofen1konu3(self):
        giris2 = video1()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotofen1konu4(self):
        giris3 = video1()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

class mat1(QDialog):
    def __init__(self):
        super(mat1,self).__init__()
        loadUi("matematikkonu.ui",self)
        self.matkonu1.clicked.connect(self.gotomat1konu1)
        self.matkonu2.clicked.connect(self.gotomat1konu2)
        self.matkonu3.clicked.connect(self.gotomat1konu3)
        self.matkonu4.clicked.connect(self.gotomat1konu4)

    def gotomat1konu1(self):
        gelis = video1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotomat1konu2(self):
        gelis1 = video1()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotomat1konu3(self):
        giris2 = video1()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotomat1konu4(self):
        giris3 = video1()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)
class turkce1(QDialog):
    def __init__(self):
        super(turkce1,self).__init__()
        loadUi("turkcekonu.ui",self)
        self.turkcekonu1.clicked.connect(self.gototurkce1konu1)
        self.turkcekonu2.clicked.connect(self.gototurkce1konu2)
        self.turkcekonu3.clicked.connect(self.gototurkce1konu3)
        self.turkcekonu4.clicked.connect(self.gototurkce1konu4)

    def gototurkce1konu1(self):
        gelis = video1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gototurkce1konu2(self):
        gelis1 = video1()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)
    def gototurkce1konu3(self):
        giris2 = video1()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gototurkce1konu4(self):
        giris3 = video1()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)


class hayat1(QDialog):
    def __init__(self):
        super(hayat1,self).__init__()
        loadUi("hayatbilgisikonu.ui",self)
        self.hayatkonu1.clicked.connect(self.gotohayat1konu1)
        self.hayatkonu2.clicked.connect(self.gotohayat1konu2)
        self.hayatkonu3.clicked.connect(self.gotohayat1konu3)
        self.hayatkonu4.clicked.connect(self.gotohayat1konu4)

    def gotohayat1konu1(self):
        gelis = video1()
        widget.addWidget(gelis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotohayat1konu2(self):
        gelis1 = video1()
        widget.addWidget(gelis1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotohayat1konu3(self):
        giris2 = video1()
        widget.addWidget(giris2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)

    def gotohayat1konu4(self):
        giris3 = video1()
        widget.addWidget(giris3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1120)
        widget.setFixedHeight(590)


class fenkonu1(QDialog):
    def __init__(self):
        super(fenkonu1,self).__init__()
        loadUi("fenskonu1soru.ui",self)

class fenkonu2(QDialog):
    def __init__(self):
        super(fenkonu2,self).__init__()
        loadUi("fenkonu2soru.ui",self)

class fenkonu3(QDialog):
    def __init__(self):
        super(fenkonu3,self).__init__()
        loadUi("fenkonu3soru.ui",self)
class fenkonu4(QDialog):
    def __init__(self):
        super(fenkonu4,self).__init__()
        loadUi("fenkonu4soru.ui",self)

class matkonu1(QDialog):
    def __init__(self):
        super(matkonu1,self).__init__()
        loadUi("matkonu1soru.ui",self)

class matkonu2(QDialog):
    def __init__(self):
        super(matkonu2,self).__init__()
        loadUi("matkonu2soru.ui",self)

class matkonu3(QDialog):
    def __init__(self):
        super(matkonu3,self).__init__()
        loadUi("matkonu3soru.ui",self)
class matkonu4(QDialog):
    def __init__(self):
        super(matkonu4,self).__init__()
        loadUi("matkonu4soru.ui",self)

class turkcekonu1(QDialog):
    def __init__(self):
        super(turkcekonu1,self).__init__()
        loadUi("turkcekonu1soru.ui",self)

class turkcekonu2(QDialog):
    def __init__(self):
        super(turkcekonu2,self).__init__()
        loadUi("turkcekonu2soru.ui",self)

class turkcekonu3(QDialog):
    def __init__(self):
        super(turkcekonu3,self).__init__()
        loadUi("turkcekonu3soru.ui",self)
class turkcekonu4(QDialog):
    def __init__(self):
        super(turkcekonu4,self).__init__()
        loadUi("turkcekonu4soru.ui",self)

class hayatkonu1(QDialog):
    def __init__(self):
        super(hayatkonu1,self).__init__()
        loadUi("hayatkonu1soru.ui",self)

class hayatkonu2(QDialog):
    def __init__(self):
        super(hayatkonu2,self).__init__()
        loadUi("hayatkonu2soru.ui",self)

class hayatkonu3(QDialog):
    def __init__(self):
        super(hayatkonu3,self).__init__()
        loadUi("hayatkonu3soru.ui",self)
class hayatkonu4(QDialog):
    def __init__(self):
        super(hayatkonu4,self).__init__()
        loadUi("hayatkonu4soru.ui",self)

class video1(QDialog):
    def __init__(self):
        super(video1,self).__init__()
        loadUi("video.ui",self)

app = QApplication(sys.argv)
ilk = Ilkekran()
widget = QStackedWidget()
widget.setFixedWidth(450)
widget.setFixedHeight(600)
widget.addWidget(ilk)
widget.show()
app.exec_()

