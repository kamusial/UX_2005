class Auto:
    def __init__(self, brand, rocznik, barwa):
        self.marka = brand
        self.kolor = barwa
        self.wiek = 2023 - rocznik
        self.kondycja = 5
        self.ilosc_paliwa = 10
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.przebieg = 0

    def zasieg(self):
        _zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(_zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.spalanie_na_100 = 10
            self.tryb_ekonomiczny = True
            print('Tryb eco')
        elif tryb == 'normal':
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            print('Tryb normal')
        else:
            print('tryb nierozpoznany, brak zmian')

# class BMW(Auto):
#     init

moje_auto = Auto('bmw', 1997, 'czerwone')

print(moje_auto.spalanie_na_100)
moje_auto.ustaw_tryb('ecssso')
print(moje_auto.spalanie_na_100)


