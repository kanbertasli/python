"""
Code the Hangman Game.
You are free on this assignment.
You can set the rules yourself. There is only one thing expected of you.
When entering the game. The User's name and for example "Welcome John" should be pressed to the screen.
When the game is over. exit the game. So let the game end.
"""
"""

    DEĞİŞKENLER TÜRKÇE BİLERKEN KULLANILMIŞTIR. TÜRKÇE KAYNAK ARTMASI İÇİN....BİRAZDA ONLAR TÜRKÇE ÖĞRENSİNLER:)


"""


import random

EkranGösterimi=['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']

GirilenHarfler = ''
YeniGirilenHarfler = ''
# kaç harf tahmini girebileceğini sabitleyelim.
TahminSayisi = 7
EkranYazisi = ''

 
name = input("Size daha rahat hitap edebilmek için isminizi öğrenebilir miyim? ")
#ismini öğrenelim sonra bir hoşgeldin yazalım ekrana.
 
print("Hoşgeldin ", name)

#oyun kuralları hakkında kısa bir bilgi verelim.
print("Bildiğin üzere rast gele bir kelime tutacağım ve senden harfler girerek bunu tahmin etmeni umacağım. Ufak bir ipucu kelimelerimiz meyvelerden oluşuyor. 7 harf tahmininde bulunabilirsin.")
 
#random seçim yapacağımız bir liste oluşturalım.
meyveler = ['portal', 'elma', 'mandalina', 'muz', 
         'kivi', 'çilek', 'avakoda', 'ayva', 
         'nar', 'pomelo'] 
 
RandomSecilenMeyve = random.choice(meyveler)



#random bir meyve seçelim. ve uzunluğu kadar ekran _ basalım.
MeyveUzunluk = len(RandomSecilenMeyve) 

for i in RandomSecilenMeyve:
    EkranYazisi+='_ '

 
print("Hadi bir harf bulmaya çalış bakalım")
 
 
 
while TahminSayisi > 0: #sıfırdan büyük olduğu sürece tekrar soralım.
     
    # hatasayisini sayalım.
    HataSayisi = 0
    BulunanHarfinIndexi=0
     
    for Harf in RandomSecilenMeyve: 
         
        # girilen harfi kontrol edelim.
        if Harf == YeniGirilenHarfler: 
            EkranYazisi = EkranYazisi[:BulunanHarfinIndexi*2] + Harf + EkranYazisi[BulunanHarfinIndexi*2+1:]        
            #print(BulunanHarfinIndexi)
        else: 
            HataSayisi += 1
        BulunanHarfinIndexi+=1
    
    print(EkranYazisi) 
 
    if EkranYazisi.find('_',0) == -1:  # eğer ekran yazısında _ kalmadıysa doğru tahmin etmiş demektir!
        print("Tebrikler Doğru Tahmin Ettin!") 
        break
     
    YeniGirilenHarfler = input("Bir harf gir: ")
     
    GirilenHarfler += YeniGirilenHarfler 
     
    if YeniGirilenHarfler not in RandomSecilenMeyve:
         
        TahminSayisi -= 1

        print(EkranGösterimi[6-TahminSayisi]) 
        print("Malesef bu harf yok")
        print("Kalan Tahmin sayın:", + TahminSayisi)
         
         
        if TahminSayisi == 0:
            print("Üzgünüm bilemedin...")