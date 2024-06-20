'''module untuk luas bangun datar'''

def luas_persegi(sisi: float) -> float:
    hasil: float = sisi ** 2
    return hasil

def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    hasil: float = panjang * lebar
    return hasil

def luas_trapesium(atas: float, bawah: float, tinggi: float) -> float:
    hasil: float = (atas + bawah) * tinggi / 2
    return hasil

def luas_lingkaran(radius: float) -> float:
    hasil: float = 22 / 7 * radius ** 2
    return hasil

def luas_jajar_genjang(alas: float, tinggi: float) -> float:
    hasil: float = alas * tinggi
    return hasil

def luas_layang_layang(d1: float, d2: float) -> float:
    hasil: float = d1 * d2 / 2 
    return hasil

def luas_segitiga(alas: float, tinggi: float) -> float:
    hasil: float = alas * tinggi / 2
    return hasil