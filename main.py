from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import random
import os
import weakref

class Dize():

    def __init__(self,icerik,sairismi,donem, anlayis = "-" , topluluk = "-"):
        self.icerik = icerik
        self.sairismi = sairismi
        self.donem = donem
        self.anlayis = anlayis
        self.topluluk = topluluk

    def bilgilerigoster(self):
        print("Şair: {}, {}, {}, {}".format(self.sairismi,self.donem,self.anlayis,self.topluluk))
    def dizeyiyazdir(self):
        print(self.icerik)
    def dize(self):
        return self.icerik
    def bilgiler(self):
        self.sairismi = self.sairismi.replace(".txt", "")
        self.sairismi = self.sairismi.replace("-", " ")
        self.sairismi = self.sairismi.capitalize()
        return "{} ,   {} ,  {} , {}".format(self.sairismi,self.donem,self.anlayis,self.topluluk)

#DİVAN DÖNEMİNİ SINIFA SOKMA
Divanliste = []
with open("Divansairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'Divan', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] , "Divan Edebiyatı")
                    Divanliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'Divan', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] , "Divan Edebiyatı")
                    Divanliste.append(i)
#AsikHalk DÖNEMİNİ SINIFA SOKMA
AsikHalkliste = []
with open("AsikHalksairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'AsikHalk', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Halk Edebiyatı","Aşık Tarzı")
                    AsikHalkliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'AsikHalk', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Halk Edebiyatı", "Aşık Tarzı")
                    AsikHalkliste.append(i)
#DİNİHALK DÖNEMİNİ SINIFA SOKMA
DiniHalkliste = []
with open("DiniHalksairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'DiniHalk', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] , "Halk Edebiyatı","Dini-Tasavvufi Anlayış")
                    DiniHalkliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'DiniHalk', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Halk Edebiyatı", "Dini-Tasavvufi Anlayış")
                    DiniHalkliste.append(i)
#TANZİMAT DÖNEMİNİ SINIFA SOKMA
Tanzimatliste = []
with open("Tanzimatsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'Tanzimat', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] , "Tanzimat Edebiyatı")
                    Tanzimatliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'Tanzimat', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Tanzimat Edebiyatı")
                    Tanzimatliste.append(i)
#ServetiFunun DÖNEMİNİ SINIFA SOKMA
ServetiFununliste = []
with open("ServetiFununsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'ServetiFunun', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"ServetiFunun Edebiyatı","-","ServetiFunun Topluluğu")
                    ServetiFununliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'ServetiFunun', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "ServetiFunun Edebiyatı", "-", "ServetiFunun Topluluğu")
                    ServetiFununliste.append(i)
#FECRİATİ
Fecriatiliste = []
with open("FecriAtisairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'FecriAti', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Fecriati Edebiyatı","-","Fecriati Topluluğu")
                    Fecriatiliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'FecriAti', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Fecriati Edebiyatı", "-", "Fecriati Topluluğu")
                    Fecriatiliste.append(i)
#MİLLİ DÖNEMİNİ SINIFA SOKMA
Milliliste = []
with open("Millisairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'Milli', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Milli Edebiyat")
                    Milliliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'Milli', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Milli Edebiyat")
                    Milliliste.append(i)
#MİLLİ DÖNEMİ BEŞ HECECİLER
BesHececilerliste = []
with open("BesHececilersairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'BesHececiler', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Milli Edebiyat","-","Beş Hececiler")
                    BesHececilerliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'BesHececiler', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Milli Edebiyat", "-", "Beş Hececiler")
                    BesHececilerliste.append(i)
###############################################################  CUMHURİYET
#CUMHURİYET DÖNEMİ SAF ŞİİR ANLAYIŞI
CHSafSiirliste = []
with open("CHSafsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'CHSaf', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Saf Şiir Anlayışı")
                    CHSafSiirliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'CHSaf', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Saf Şiir Anlayışı")
                    CHSafSiirliste.append(i)
#YediMesaleciler
YediMesalecilerliste = []
with open("YediMesalecilersairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'YediMesaleciler', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Saf Şiir Anlayışı","Yedi Meşaleciler")
                    YediMesalecilerliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'YediMesaleciler', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Saf Şiir Anlayışı", "Yedi Meşaleciler")
                    YediMesalecilerliste.append(i)
#CUMHURİYET DÖNEMİ TOPLUMCU ŞİİR ANLAYIŞI
CHToplumculiste = []
with open("CHToplumcusairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'CHToplumcu', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Toplumcu Şiir Anlayışı")
                    CHToplumculiste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'CHToplumcu', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Toplumcu Şiir Anlayışı")
                    CHToplumculiste.append(i)
#MAVİCİLER
Mavicilerliste = []
with open("Mavicilersairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'Maviciler', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] , "Cumhuriyet Dönemi","Toplumcu Şiir Anlayışı","Maviciler")
                    Mavicilerliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'Maviciler', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Toplumcu Şiir Anlayışı", "Maviciler")
                    Mavicilerliste.append(i)
#CUMHURİYET DÖNEMİNDE MİLLİ EDEBİYAT
CHMilliliste = []
with open("CHMillisairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'CHMilli', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Milli Şiir Anlayışı")
                    CHMilliliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'CHMilli', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Milli Şiir Anlayışı")
                    CHMilliliste.append(i)
#CUMHURİYET DÖNEMİNDE GARİP AKIMI
Garipliste = []
with open("Garipsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'Garip', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Garip Akımı(I. Yeni)")
                    Garipliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'Garip', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Garip Akımı(I. Yeni)")
                    Garipliste.append(i)
#CUMHURİYET DÖNEMİNDE İKİNCİ YENİ AKIMI
ikinciYeniliste = []
with open("ikinciYenisairleri.txt", "r", encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'ikinciYeni', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","II. Yeni Akımı")
                    ikinciYeniliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'ikinciYeni', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "II. Yeni Akımı")
                    ikinciYeniliste.append(i)
#DİN GELENEK VE METAFİZİK ÖGELERİNE BAĞLI ANLAYIŞ
DinGMliste = []
with open("DinGMsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'DinGM', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Din,Gelenek,Metafizik Ögelerine Bağlı")
                    DinGMliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'DinGM', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Din,Gelenek,Metafizik Ögelerine Bağlı")
                    DinGMliste.append(i)
#Hisarcilar
Hisarcilarliste = []
with open("Hisarcilarsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'Hisarcilar', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Din,Gelenek,Metafizik Ögelerine Bağlı","Hisarcilar")
                    Hisarcilarliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'Hisarcilar', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Din,Gelenek,Metafizik Ögelerine Bağlı", "Hisarcilar")
                    Hisarcilarliste.append(i)
#60 SONRASI TOPLUMCU ŞİİR
AltmisSliste = []
with open("AltmisSsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'AltmisS', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","60 Sonrası Toplumcu Şiir")
                    AltmisSliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'AltmisS', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "60 Sonrası Toplumcu Şiir")
                    AltmisSliste.append(i)
# 80 Sonrası TÜRK ŞİİRİ
SeksenSliste = []
with open("SeksenSsairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'SeksenS', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","80 Sonrası Toplumcu Şiir")
                    SeksenSliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'SeksenS', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "80 Sonrası Toplumcu Şiir")
                    SeksenSliste.append(i)
# Cumhuriyet Dönemindeki Halk Şiiri
CHHalkliste = []
with open("CHHalksairleri.txt","r",encoding="utf-8") as file:
    for filename in file:
        try:
            with open(os.path.join('Siirler', 'CHHalk', filename),"r",encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4] ,"Cumhuriyet Dönemi","Cumhuriyet Dönemi Halk Şiiri")
                    CHHalkliste.append(i)
        except:
            filename = filename[:-1]
            with open(os.path.join('Siirler', 'CHHalk', filename), "r", encoding="utf-8") as fl:
                for i in fl:
                    i = Dize(i, filename[:-4], "Cumhuriyet Dönemi", "Cumhuriyet Dönemi Halk Şiiri")
                    CHHalkliste.append(i)
TumCH = CHSafSiirliste + YediMesalecilerliste + CHToplumculiste + Mavicilerliste + CHMilliliste + Garipliste + ikinciYeniliste + DinGMliste + Hisarcilarliste + AltmisSliste + SeksenSliste + CHHalkliste

dler = ["AltmisSsairleri.txt", "AsikHalksairleri.txt", "BesHececilersairleri.txt", "CHHalksairleri.txt",
        "CHMillisairleri.txt", "CHSafsairleri.txt", "CHToplumcusairleri.txt", "DinGMsairleri.txt",
        "DiniHalksairleri.txt", "Divansairleri.txt", "FecriAtisairleri.txt", "Garipsairleri.txt",
        "Hisarcilarsairleri.txt", "ikinciYenisairleri.txt", "Mavicilersairleri.txt", "Millisairleri.txt",
        "SeksenSsairleri.txt", "ServetiFununsairleri.txt", "Tanzimatsairleri.txt", "YediMesalecilersairleri.txt"]

class HomeScreen(Screen):
    pass
class ImageButton(ButtonBehavior,Image):
    pass
class SaveScreen(Screen):
    pass
class DonemsairScreen(Screen):
    pass
class AciklamaScreen(Screen):
    pass
class DonemScreen(Screen):
    pass
class UyaksecScreen(Screen):
    pass
class OutputScreen(Screen):
    pass
class MillibolumScreen(Screen):
    pass
class CumhuriyetbolumScreen(Screen):
    pass
class SairlerScreen(Screen):
    pass
silmesayi = 0
harfsayisi= 3
sayim = 0
donemsecimi="yok"
bsayisi = 0
ksayisi = 0

GUI = Builder.load_file("main.kv")
class MainApp(App):
    liste = []
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
    def on_start(self):
        baslik = self.root.ids["home_screen"].ids["baslik"]
        baslik.text = "ŞİİR KARMA"
        anamenu = self.root.ids["home_screen"].ids["anamenu"]
        anamenu.text = "Oluştur"
        
        siirlerim = self.root.ids["home_screen"].ids["siirlerim"]
        siirlerim.text = "    Şiirlerim"
        tum_cumhuriyet = self.root.ids['cumhuriyetbolum_screen'].ids['tum_cumhuriyet']
        tum_cumhuriyet.text = "Tüm Cumhuriyet Dönemi"
        ch_saf = self.root.ids['cumhuriyetbolum_screen'].ids['ch_saf']
        ch_saf.text = "Saf Şiir Anlayışı"
        yedi_mesaleciler = self.root.ids['cumhuriyetbolum_screen'].ids['yedi_mesaleciler']
        yedi_mesaleciler.text = "Yedi Meşaleciler"
        ch_toplumcu = self.root.ids['cumhuriyetbolum_screen'].ids['ch_toplumcu']
        ch_toplumcu.text = "Toplumcu Şiir Anlayışı"
        maviciler = self.root.ids['cumhuriyetbolum_screen'].ids['maviciler']
        maviciler.text = "Maviciler"
        ch_milli = self.root.ids['cumhuriyetbolum_screen'].ids['ch_milli']
        ch_milli.text = "Milli Edebiyat Anlayışı"
        garip = self.root.ids['cumhuriyetbolum_screen'].ids['garip']
        garip.text = "Garip Akımı(I. Yeni)"
        ikinci_yeni = self.root.ids['cumhuriyetbolum_screen'].ids['ikinci_yeni']
        ikinci_yeni.text = "İkinci Yeni Akımı"
        din_gm = self.root.ids['cumhuriyetbolum_screen'].ids['din_gm']
        din_gm.text = "Din Gelenek, Metafiziğe Bağlı"
        Hisarcilar = self.root.ids['cumhuriyetbolum_screen'].ids['Hisarcilar']
        Hisarcilar.text = "Hisarcilar"
        ch_saf = self.root.ids['cumhuriyetbolum_screen'].ids['ch_saf']
        ch_saf.text = "Saf Şiir Anlayışı"
        altmis_s = self.root.ids['cumhuriyetbolum_screen'].ids['altmis_s']
        altmis_s.text = "60 Sonrası Toplumcu Şiir"
        seksen_s = self.root.ids['cumhuriyetbolum_screen'].ids['seksen_s']
        seksen_s.text = "80 Sonrası Türk Şiiri"
        ch_halk = self.root.ids['cumhuriyetbolum_screen'].ids['ch_halk']
        ch_halk.text = "Cumhuriyet Döneminde Halk Şiiri"
        asik_halk = self.root.ids['donem_screen'].ids['asik_halk']
        asik_halk.text = "Aşık Halk Şiiri"
        dini_halk = self.root.ids['donem_screen'].ids['dini_halk']
        dini_halk.text = "Dini Halk Şiiri"
        divan = self.root.ids['donem_screen'].ids['divan']
        divan.text = "Divan Şiiri"
        tanzimat = self.root.ids['donem_screen'].ids['tanzimat']
        tanzimat.text = "Tanzimat Şiiri"
        servetifunun = self.root.ids['donem_screen'].ids['servetifunun']
        servetifunun.text = "ServetiFunun Şiiri"
        fecriati = self.root.ids['donem_screen'].ids['fecriati']
        fecriati.text = "Fecriati Şiiri"
        milligiris = self.root.ids['donem_screen'].ids['milligiris']
        milligiris.text = "Milli Edebiyat Şiiri"
        cumhuriyetgiris = self.root.ids['donem_screen'].ids['cumhuriyetgiris']
        cumhuriyetgiris.text = "Cumhuriyet Şiiri"
        duz_uyak1 = self.root.ids['uyaksec_screen'].ids['duz_uyak1']
        duz_uyak1.text = " Düz Uyak \n  (a,a,a,b) \n -önerilen-"
        duz_uyak = self.root.ids['uyaksec_screen'].ids['duz_uyak']
        duz_uyak.text = " Düz Uyak \n  (a,a,b,b)"
        capraz_uyak = self.root.ids['uyaksec_screen'].ids['capraz_uyak']
        capraz_uyak.text = "Çapraz Uyak\n  (a,b,a,b)"
        sarma_uyak = self.root.ids['uyaksec_screen'].ids['sarma_uyak']
        sarma_uyak.text = "Sarma Uyak\n  (a,b,b,a)"
        donem_kar = self.root.ids['donemsair_screen'].ids['donem_kar']
        donem_kar.text = "Dönem Seçip Karıştır\n         -Önerilen-"
        sair_kar = self.root.ids['donemsair_screen'].ids['sair_kar']
        sair_kar.text = "Şair Seçip Karıştır"
        siir_grid = self.root.ids["save_screen"].ids["siir_grid"]
        kar = self.root.ids["output_screen"].ids["kar"]
        kar.text = "Karıştır"
        aciklama_label=self.root.ids["aciklama_screen"].ids["aciklama_label"]
        aciklama_label.text="   Şiir Karma uygulamasıyla farklı sanatçıların, farklı zihinlerin ürünlerinin bir araya gelince nasıl bir uyum sağladığını göstermeyi amaçladık. Şairlerimizden seçtiğimiz şiirle geniş bir havuz oluşturduk. Bu havuzdan istediğiniz edebi dönemi ve şairi seçip onların şiirlerinden rastgele dizeler alarak bir dörtlük oluşturabilirsiniz. Hoşunuza gidene kadar karıştırıp beğendiğiniz dörtlüğü kaydedebilirsiniz. Kayıtlı şiirlerinizi görmek için bazen uygulamayı kapatıp açmanız gerekebilir. \n\n\n Her türlü görüş ve önerinizi uygulama yorumlarında belirtmeyi unutmayın! \n\n İletişim için: drhakki@icloud.com"
        divanin_farki = self.root.ids["uyaksec_screen"].ids["divanin_farki"]
        divanin_farki.text = "Buradan dizelerinizin sonu için uyak seçebilirsiniz."
        sil = self.root.ids["save_screen"].ids["sil"]
        sil.text="Tümünü Sil"
        with open("saved.txt", "r", encoding="utf-8") as file1:
            for a in file1:
                l = Label(text=a,font_size= "15sp")
                siir_grid.add_widget(l)

        sair_grid = self.root.ids["sairler_screen"].ids["sair_grid"]

        for a in dler:
            with open(a,"r",encoding="utf-8") as file1:
                for b in file1:
                    btn = Button(text=b,on_press=lambda x:self.change_screen("uyaksec_screen"),on_release=lambda y, b=b:self.sairi(b),background_color=(0.0, 1.0, 1.0, 1.0))
                    b = b.replace(".txt", "")
                    b = b.replace("-", " ")
                    b = b.lower()
                    b = b.capitalize()
                    btn.text = b
                    sair_grid.add_widget(btn)
    def AsikHalk(self):
        global donemsecimi
        donemsecimi = "AsikHalk"
    def DiniHalk(self):
        global donemsecimi
        donemsecimi = "DiniHalk"
    def Divan(self):
        global donemsecimi
        donemsecimi = "Divan"
    def Tanzimat(self):
        global donemsecimi
        donemsecimi = "Tanzimat"
    def ServetiFunun(self):
        global donemsecimi
        donemsecimi = "ServetiFunun"
    def FecriAti(self):
        global donemsecimi
        donemsecimi = "FecriAti"
    def Milli(self):
        global donemsecimi
        donemsecimi = "Milli"
    def BesHececiler(self):
        global donemsecimi
        donemsecimi = "BesHececiler"
    def CHSafSiir(self):
        global donemsecimi
        donemsecimi = "CHSafSiir"
    def YediMesaleciler(self):
        global donemsecimi
        donemsecimi = "YediMesaleciler"
    def CHToplumcu(self):
        global donemsecimi
        donemsecimi = "CHToplumcu"
    def Maviciler(self):
        global donemsecimi
        donemsecimi = "Maviciler"
    def CHMilli(self):
        global donemsecimi
        donemsecimi = "CHMilli"
    def Garip(self):
        global donemsecimi
        donemsecimi = "Garip"
    def ikinciYeni(self):
        global donemsecimi
        donemsecimi = "ikinciYeni"
    def DinGM(self):
        global donemsecimi
        donemsecimi = "DinGM"
    def Hisarcilar(self):
        global donemsecimi
        donemsecimi = "Hisarcilar"
    def AltmisS(self):
        global donemsecimi
        donemsecimi = "AltmisS"
    def SeksenS(self):
        global donemsecimi
        donemsecimi = "SeksenS"
    def CHHalk(self):
        global donemsecimi
        donemsecimi = "CHHalk"
    def TumCH(self):
        global donemsecimi
        donemsecimi = "TumCH"
    def sairi(self,deger):
        global liste
        liste=[]
        global donemsecimi
        donemsecimi="bos"
        for a in dler:
            try:
                with open(os.path.join('Siirler', a[:-12], deger),"r",encoding="utf-8") as file1:
                    for b in file1:
                        c = Dize(b,deger,a[:-4])
                        liste.append(c)
            except:
                continue
        for a in dler:
            try:
                with open(os.path.join('Siirler', a[:-12], deger[:-1]),"r",encoding="utf-8") as file1:
                    for b in file1:
                        c = Dize(b,deger,a[:-4])
                        liste.append(c)
            except:
                continue
    def duzuyak(self):
        global donemsecimi
        global liste
        global uyak
        global sayim
        sayim = 0
        uyak = "duz"
        if donemsecimi == "bos":
            pass
        if donemsecimi == "AsikHalk":
            liste = AsikHalkliste
        if donemsecimi == "DiniHalk":
            liste = DiniHalkliste
        if donemsecimi == "Divan":
            liste = Divanliste
        if donemsecimi == "Tanzimat":
            liste = Tanzimatliste
        if donemsecimi == "ServetiFunun":
            liste = ServetiFununliste
        if donemsecimi == "FecriAti":
            liste = Fecriatiliste
        if donemsecimi == "Milli":
            liste = Milliliste
        if donemsecimi == "BesHececiler":
            liste = BesHececilerliste
        if donemsecimi == "CHSafSiir":
            liste = CHSafSiirliste
        if donemsecimi == "YediMesaleciler":
            liste = YediMesalecilerliste
        if donemsecimi == "CHToplumcu":
            liste = CHToplumculiste
        if donemsecimi == "Maviciler":
            liste = Mavicilerliste
        if donemsecimi == "CHMilli":
            liste = CHMilliliste
        if donemsecimi == "Garip":
            liste = Garipliste
        if donemsecimi == "ikinciYeni":
            liste = ikinciYeniliste
        if donemsecimi == "DinGM":
            liste = DinGMliste
        if donemsecimi == "Hisarcilar":
            liste = Hisarcilarliste
        if donemsecimi == "AltmisS":
            liste = AltmisSliste
        if donemsecimi == "SeksenS":
            liste = SeksenSliste
        if donemsecimi == "CHHalk":
            liste = CHHalkliste
        if donemsecimi == "TumCH":
            liste = TumCH
        while True:
            global a1
            global a2
            global x1
            global x2
            a1 = random.choice(liste)
            a2 = random.choice(liste)
            x1 = random.choice(liste)
            x2 = random.choice(liste)
            if (len(a1.dize()) > 4) and (len(x1.dize()) > 4 ) and ((a1.dize() != a2.dize()) and ( x1.dize() != x2.dize())) and (len(a1.dize()) < 50)and (len(a2.dize()) < 50)and (len(x1.dize()) < 50)and (len(x2.dize()) < 50) :
                if (a1.dize()[-harfsayisi:] == a2.dize()[-harfsayisi:] )and(x1.dize()[-harfsayisi:]==x2.dize()[-harfsayisi:]):
                    break
                else:
                    continue
            else:
                continue
        label_1 = self.root.ids['output_screen'].ids['label_1']
        label_1.text = a1.dize()
        label_2 = self.root.ids['output_screen'].ids['label_2']
        label_2.text = a2.dize()
        label_3 = self.root.ids['output_screen'].ids['label_3']
        label_3.text = x1.dize()
        label_4 = self.root.ids['output_screen'].ids['label_4']
        label_4.text = x2.dize()
    def duzuyak1(self):
        global donemsecimi
        global liste
        global uyak
        global sayim
        sayim = 0
        uyak = "duz1"
        if donemsecimi == "bos":
            pass
        if donemsecimi == "AsikHalk":
            liste = AsikHalkliste
        if donemsecimi == "DiniHalk":
            liste = DiniHalkliste
        if donemsecimi == "Divan":
            liste = Divanliste
        if donemsecimi == "Tanzimat":
            liste = Tanzimatliste
        if donemsecimi == "ServetiFunun":
            liste = ServetiFununliste
        if donemsecimi == "FecriAti":
            liste = Fecriatiliste
        if donemsecimi == "Milli":
            liste = Milliliste
        if donemsecimi == "BesHececiler":
            liste = BesHececilerliste
        if donemsecimi == "CHSafSiir":
            liste = CHSafSiirliste
        if donemsecimi == "YediMesaleciler":
            liste = YediMesalecilerliste
        if donemsecimi == "CHToplumcu":
            liste = CHToplumculiste
        if donemsecimi == "Maviciler":
            liste = Mavicilerliste
        if donemsecimi == "CHMilli":
            liste = CHMilliliste
        if donemsecimi == "Garip":
            liste = Garipliste
        if donemsecimi == "ikinciYeni":
            liste = ikinciYeniliste
        if donemsecimi == "DinGM":
            liste = DinGMliste
        if donemsecimi == "Hisarcilar":
            liste = Hisarcilarliste
        if donemsecimi == "AltmisS":
            liste = AltmisSliste
        if donemsecimi == "SeksenS":
            liste = SeksenSliste
        if donemsecimi == "CHHalk":
            liste = CHHalkliste
        if donemsecimi == "TumCH":
            liste = TumCH
        while True:
            global a1
            global a2
            global x1
            global x2
            a1 = random.choice(liste)
            a2 = random.choice(liste)
            x1 = random.choice(liste)
            x2 = random.choice(liste)
            if (len(a1.dize()) > 4) and (len(x1.dize()) > 4 ) and ((a1.dize() != a2.dize()) and ( x1.dize() != x2.dize())) and (len(a1.dize()) < 50)and (len(a2.dize()) < 50)and (len(x1.dize()) < 50)and (len(x2.dize()) < 50) :
                if a1.dize()[-harfsayisi:] == a2.dize()[-harfsayisi:] == x1.dize()[-harfsayisi:]:
                    break
                else:
                    continue
            else:
                continue
        label_1 = self.root.ids['output_screen'].ids['label_1']
        label_1.text = a1.dize()
        label_2 = self.root.ids['output_screen'].ids['label_2']
        label_2.text = a2.dize()
        label_3 = self.root.ids['output_screen'].ids['label_3']
        label_3.text = x1.dize()
        label_4 = self.root.ids['output_screen'].ids['label_4']
        label_4.text = x2.dize()
    def caprazuyak(self):
        global donemsecimi
        global liste
        global uyak
        global sayim
        sayim = 0
        uyak = "sarma"
        if donemsecimi == "bos":
            pass
        if donemsecimi == "AsikHalk":
            liste = AsikHalkliste
        if donemsecimi == "DiniHalk":
            liste = DiniHalkliste
        if donemsecimi == "Divan":
            liste = Divanliste
        if donemsecimi == "Tanzimat":
            liste = Tanzimatliste
        if donemsecimi == "ServetiFunun":
            liste = ServetiFununliste
        if donemsecimi == "FecriAti":
            liste = Fecriatiliste
        if donemsecimi == "Milli":
            liste = Milliliste
        if donemsecimi == "BesHececiler":
            liste = BesHececilerliste
        if donemsecimi == "CHSafSiir":
            liste = CHSafSiirliste
        if donemsecimi == "YediMesaleciler":
            liste = YediMesalecilerliste
        if donemsecimi == "CHToplumcu":
            liste = CHToplumculiste
        if donemsecimi == "Maviciler":
            liste = Mavicilerliste
        if donemsecimi == "CHMilli":
            liste = CHMilliliste
        if donemsecimi == "Garip":
            liste = Garipliste
        if donemsecimi == "ikinciYeni":
            liste = DiniHalkliste
        if donemsecimi == "DinGM":
            liste = DinGMliste
        if donemsecimi == "Hisarcilar":
            liste = Hisarcilarliste
        if donemsecimi == "AltmisS":
            liste = AltmisSliste
        if donemsecimi == "SeksenS":
            liste = SeksenSliste
        if donemsecimi == "CHHalk":
            liste = CHHalkliste
        if donemsecimi == "TumCH":
            liste = TumCH
        while True:
            global a1
            global a2
            global x1
            global x2
            a1 = random.choice(liste)
            a2 = random.choice(liste)
            x1 = random.choice(liste)
            x2 = random.choice(liste)
            if (len(a1.dize()) > 4) and (len(x1.dize()) > 4 ) and ((a1.dize() != a2.dize()) and ( x1.dize() != x2.dize())) and (len(a1.dize()) < 50)and (len(a2.dize()) < 50)and (len(x1.dize()) < 50)and (len(x2.dize()) < 50) :
                if (a1.dize()[-harfsayisi:] == a2.dize()[-harfsayisi:]) and (x1.dize()[-harfsayisi:] == x2.dize()[-harfsayisi:]):
                    break
                else:
                    continue
            else:
                continue
        label_1 = self.root.ids['output_screen'].ids['label_1']
        label_1.text = a1.dize()
        label_2 = self.root.ids['output_screen'].ids['label_2']
        label_2.text = x1.dize()
        label_3 = self.root.ids['output_screen'].ids['label_3']
        label_3.text = a2.dize()
        label_4 = self.root.ids['output_screen'].ids['label_4']
        label_4.text = x2.dize()
    def sarmauyak(self):
        global uyak
        global donemsecimi
        global liste
        global sayim
        sayim = 0
        uyak = "sarma"
        if donemsecimi == "bos":
            pass
        if donemsecimi == "AsikHalk":
            liste = AsikHalkliste
        if donemsecimi == "DiniHalk":
            liste = DiniHalkliste
        if donemsecimi == "Divan":
            liste = Divanliste
        if donemsecimi == "Tanzimat":
            liste = Tanzimatliste
        if donemsecimi == "ServetiFunun":
            liste = ServetiFununliste
        if donemsecimi == "FecriAti":
            liste = Fecriatiliste
        if donemsecimi == "Milli":
            liste = Milliliste
        if donemsecimi == "BesHececiler":
            liste = BesHececilerliste
        if donemsecimi == "CHSafSiir":
            liste = CHSafSiirliste
        if donemsecimi == "YediMesaleciler":
            liste = YediMesalecilerliste
        if donemsecimi == "CHToplumcu":
            liste = CHToplumculiste
        if donemsecimi == "Maviciler":
            liste = Mavicilerliste
        if donemsecimi == "CHMilli":
            liste = CHMilliliste
        if donemsecimi == "Garip":
            liste = Garipliste
        if donemsecimi == "ikinciYeni":
            liste = DiniHalkliste
        if donemsecimi == "DinGM":
            liste = DinGMliste
        if donemsecimi == "Hisarcilar":
            liste = Hisarcilarliste
        if donemsecimi == "AltmisS":
            liste = AltmisSliste
        if donemsecimi == "SeksenS":
            liste = SeksenSliste
        if donemsecimi == "CHHalk":
            liste = CHHalkliste
        if donemsecimi == "TumCH":
            liste = TumCH
        while True:
            global a1
            global a2
            global x1
            global x2
            a1 = random.choice(liste)
            a2 = random.choice(liste)
            x1 = random.choice(liste)
            x2 = random.choice(liste)
            if (len(a1.dize()) > 4) and (len(x1.dize()) > 4 ) and ((a1.dize() != a2.dize()) and ( x1.dize() != x2.dize())) and (len(a1.dize()) < 50)and (len(a2.dize()) < 50)and (len(x1.dize()) < 50)and (len(x2.dize()) < 50) :
                if (a1.dize()[-harfsayisi:] == a2.dize()[-harfsayisi:]) and (x1.dize()[-harfsayisi:] == x2.dize()[-harfsayisi:]):
                    break
                else:
                    continue
            else:
                continue
        label_1 = self.root.ids['output_screen'].ids['label_1']
        label_1.text = a1.dize()
        label_2 = self.root.ids['output_screen'].ids['label_2']
        label_2.text = x1.dize()
        label_3 = self.root.ids['output_screen'].ids['label_3']
        label_3.text = x2.dize()
        label_4 = self.root.ids['output_screen'].ids['label_4']
        label_4.text = a2.dize()
    def tekrar(self):
        if uyak == "duz":
            self.duzuyak()
        if uyak == "sarma":
            self.sarmauyak()
        if uyak == "capraz":
            self.caprazuyak()
        if uyak == "duz1":
            self.duzuyak1()
        kaydedildi = self.root.ids['output_screen'].ids['kaydedildi']
        kaydedildi.text = "Kaydet"
        bilgis = self.root.ids["output_screen"].ids["bilgis"]
        bilgis.text = "Dize Bilgileri"
        global ksayisi
        ksayisi = 0
    def bilgiler(self):
        global sayim
        global bsayisi
        sayim += 1
        if sayim % 2 == 1 :
            if uyak == "duz" or uyak == "duz1":
                label_1 = self.root.ids['output_screen'].ids['label_1']
                label_1.text = a1.bilgiler()
                label_2 = self.root.ids['output_screen'].ids['label_2']
                label_2.text = a2.bilgiler()
                label_3 = self.root.ids['output_screen'].ids['label_3']
                label_3.text = x1.bilgiler()
                label_4 = self.root.ids['output_screen'].ids['label_4']
                label_4.text = x2.bilgiler()
            if uyak == "sarma":
                label_1 = self.root.ids['output_screen'].ids['label_1']
                label_1.text = a1.bilgiler()
                label_2 = self.root.ids['output_screen'].ids['label_2']
                label_2.text = x1.bilgiler()
                label_3 = self.root.ids['output_screen'].ids['label_3']
                label_3.text = a2.bilgiler()
                label_4 = self.root.ids['output_screen'].ids['label_4']
                label_4.text = x2.bilgiler()
            if uyak == "capraz":
                label_1 = self.root.ids['output_screen'].ids['label_1']
                label_1.text = a1.bilgiler()
                label_2 = self.root.ids['output_screen'].ids['label_2']
                label_2.text = x1.bilgiler()
                label_3 = self.root.ids['output_screen'].ids['label_3']
                label_3.text = x2.bilgiler()
                label_4 = self.root.ids['output_screen'].ids['label_4']
                label_4.text = a2.bilgiler()
        if sayim % 2 == 0:
            if uyak == "duz" or uyak == "duz1":
                label_1 = self.root.ids['output_screen'].ids['label_1']
                label_1.text = a1.dize()
                label_2 = self.root.ids['output_screen'].ids['label_2']
                label_2.text = a2.dize()
                label_3 = self.root.ids['output_screen'].ids['label_3']
                label_3.text = x1.dize()
                label_4 = self.root.ids['output_screen'].ids['label_4']
                label_4.text = x2.dize()
            if uyak == "sarma":
                label_1 = self.root.ids['output_screen'].ids['label_1']
                label_1.text = a1.dize()
                label_2 = self.root.ids['output_screen'].ids['label_2']
                label_2.text = x1.dize()
                label_3 = self.root.ids['output_screen'].ids['label_3']
                label_3.text = a2.dize()
                label_4 = self.root.ids['output_screen'].ids['label_4']
                label_4.text = x2.dize()
            if uyak == "capraz":
                label_1 = self.root.ids['output_screen'].ids['label_1']
                label_1.text = a1.dize()
                label_2 = self.root.ids['output_screen'].ids['label_2']
                label_2.text = x1.dize()
                label_3 = self.root.ids['output_screen'].ids['label_3']
                label_3.text = x2.dize()
                label_4 = self.root.ids['output_screen'].ids['label_4']
                label_4.text = a2.dize()
        bsayisi += 1
        if (bsayisi % 2) == 1:
            bilgis = self.root.ids["output_screen"].ids["bilgis"]
            bilgis.text = "Şiire Dön"
        if (bsayisi % 2) == 0:
            bilgis = self.root.ids["output_screen"].ids["bilgis"]
            bilgis.text = "Dize Bilgileri"
    def harfiki(self):
        global harfsayisi
        harfsayisi = 3
        harf_iki = self.root.ids["uyaksec_screen"].ids["harf_iki"]
        harf_iki.background_color = (2.55, 1.53, 1.02, 1.0)
        harf_uc = self.root.ids["uyaksec_screen"].ids["harf_uc"]
        harf_uc.background_color = (0.51, 1.46, 1.58, 1.0)
    def harfuc(self):
        global harfsayisi
        harfsayisi = 4
        harf_iki = self.root.ids["uyaksec_screen"].ids["harf_iki"]
        harf_iki.background_color = (0.51, 1.46, 1.58, 1.0)
        harf_uc = self.root.ids["uyaksec_screen"].ids["harf_uc"]
        harf_uc.background_color = (2.55, 1.53, 1.02, 1.0)
    def kaydet(self):
        global ksayisi
        ksayisi +=1
        if ksayisi == 1:
            with open("saved.txt", "a", encoding="utf-8") as dosya:
                if uyak == "duz" or uyak =="duz1":
                    dosya.write(a1.dize())
                    dosya.write(a2.dize())
                    dosya.write(x1.dize())
                    dosya.write(x2.dize())
                    dosya.write("\n")
                if uyak == "sarma":
                    dosya.write(a1.dize())
                    dosya.write(x1.dize())
                    dosya.write(x2.dize())
                    dosya.write(a2.dize())
                    dosya.write("\n")
                if uyak == "capraz":
                    dosya.write(a1.dize())
                    dosya.write(x1.dize())
                    dosya.write(a2.dize())
                    dosya.write(x2.dize())
                    dosya.write("\n")
            kaydedildi = self.root.ids['output_screen'].ids['kaydedildi']
            kaydedildi.text = "Şiiriniz Kaydedildi!"
        else:
            kaydedildi = self.root.ids['output_screen'].ids['kaydedildi']
            kaydedildi.text = "Zaten Kayıtlı!"
    def kaydedildi(self):
        kaydedildi = self.root.ids['output_screen'].ids['kaydedildi']
        kaydedildi.text = "Kaydet"
        bilgis = self.root.ids["output_screen"].ids["bilgis"]
        bilgis.text = "Dize Bilgileri"
        global ksayisi
        ksayisi = 0
        global bsayisi
        bsayisi = 0
    def silme(self):
        global silmesayi
        silmesayi +=1
        if silmesayi==1 :
            sil = self.root.ids['save_screen'].ids['sil']
            sil.text = "Tümünü Silmek İçin Tekrar Bas"
        if silmesayi==2:
            with open("saved.txt","w",encoding="utf-8") as file:
                pass
            sil = self.root.ids['save_screen'].ids['sil']
            sil.text = "Tümü silindi"
    def silmesayfasi(self):
        global silmesayi
        silmesayi = 0

MainApp().run()

