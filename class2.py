class Automobile:
    def __init__(self,brand,nomi,rangi):
        self.brand=brand
        self.nomi=nomi
        self.rangi=rangi

    def get(self):
        brand = f'{self.brand}'
        return brand

    def get1(self):
        nomi = f'{self.nomi}'
        return nomi

    def get2(self):
        rang=f'{self.rangi}'
        return rang
    def get_info(self):
        info = f'brand: {self.brand},\nNomi: {self.nomi},\nRangi: {self.rangi}'
        return info
class xususiyat(Automobile):

    def __init__(self,brand,nomi, rangi, yili,narxi):
        super().__init__(brand,nomi,rangi)
        self.yili=yili
        self.narxi=narxi
    def get_yil(self):
        yil=f'{self.narxi}'
        return yil
    def get_narxi(self):
        narx=f'{self.narxi}'
        return narx

    def get_xislat(self):
        info = f'brend: {self.brand}, \nNomi {self.nomi},\nRangi:{self.rangi},\nYili: {self.yili},\nNarxi: {self.narxi}'
        return info
mashina=xususiyat('Tayota','Supra','Oq', 2000,3000)
print(mashina.get_xislat())