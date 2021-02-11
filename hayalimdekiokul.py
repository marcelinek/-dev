sınıf  Okul ():
    tip  =  "egitimyeri"

    def  __init__ ( self , adi , turu , ogretmen_sayisi , ö grenci_sayisi , sinif_sayisi ):
        öz . adi  =  adi
        öz . turu  =  turu
        öz . ogretmen_sayisi  =  ogretmen_sayisi
        öz .ö grenci_sayisi  = ö grenci_sayisi
        öz . sinif_sayisi  =  sinif_sayisi

O1  =  Okul ( "Afşin Teaş İstiklal" , "İlkÖğretim Okulu" , 20 , 450 , 25 )
O2  =  Okul ( "Afşin" , "Fen Lisesi" , 28 , 650 , 40 )
O3  =  Okul ( "Kayseri Erciyes" , "Üniversitesi" , 35 , 1450 , 60 )

Okullar  = [ O1 , O2 , O3 ]

için  OKUL  içinde  Okullar :
    baskı ( okul . adi , okul . turu , okul . ogretmen_sayisi , okul .ö grenci_sayisi , okul . sinif_sayisi )
