import os
from rumus import rumus_luas

def pilih_operasi():
    print('''
    0. Keluar
    1. Konversi Satuan
    2. Luas
    3. Volume
    ''')

def pilih_operasi_luas() -> None:
    print('''
    1. Luas Persegi
    2. Luas Persegi Panjang
    3. Luas Trapesium
    4. Luas Lingkaran
    5. Luas Jajar Genjang
    6. Luas Layang - Layang
    7. Luas Segitiga
    ''')

def display_luas_persegi() -> None:
    sisi: float = float(input('Masukkan panjang sisi: '))
    hasil: float = rumus_luas.luas_persegi(sisi)
    print(f'{sisi} x {sisi} = {hasil:.2f}')

def display_luas_persegi_panjang() -> None:
    panjang: float = float(input('Masukkan panjang: '))
    lebar: float = float(input('Masukkan lebar: '))
    hasil: float = rumus_luas.luas_persegi_panjang(panjang, lebar)
    print(f'{panjang} x {lebar} = {hasil:.2f}')

def display_luas_trapesium() -> None:
    atas: float = float(input('Masukkan sisi atas: '))
    bawah: float = float(input('Masukkan sisi bawah: '))
    tinggi: float = float(input('Masukkan tinggi: '))
    hasil: float = rumus_luas.luas_trapesium(atas, bawah, tinggi)
    print(f'({atas} + {bawah}) * {tinggi} / 2 = {hasil:.2f}')

def display_luas_lingkaran() -> None:
    radius: float = float(input('Masukkan radius: '))
    hasil: float = rumus_luas.luas_lingkaran(radius)
    print(f'22 / 7 * {radius} ** 2 = {hasil:.2f}')

def display_luas_jajar_genjang() -> None:
    alas: float = float(input('Masukkan alas: '))
    tinggi: float = float(input('Masukkan tinggi: '))
    hasil: float = rumus_luas.luas_jajar_genjang(alas, tinggi)
    print(f'{alas} x {tinggi} = {hasil:.2f}')

def display_luas_layang_layang() -> None:
    d1: float = float(input('Masukkan d1: ')) 
    d2: float = float(input('Masukkan d2: ')) 
    hasil: float = rumus_luas.luas_layang_layang(d1, d2)
    print(f'{d1} x {d2} / 2 = {hasil:.2f}')

def display_luas_segitiga() -> None:
    alas: float = float(input('Masukkan alas: '))
    tinggi: float = float(input('Masukkan tinggi: '))
    hasil: float = rumus_luas.luas_segitiga(alas, tinggi)
    print(f'{alas} x {tinggi} = {hasil:.2f}')

while True:
    os.system('cls')
    print(f'\n{'OPERASI':=^50}')
    
    # pilih operasi
    pilih_operasi()
    input_operasi: int = int(input('Masukkan pilihan: ')) 
    
    # keluar
    if input_operasi == 0:
        break
    
    # pilih operasi luas
    elif input_operasi == 2:
        pilih_operasi_luas()
        input_luas: int = int(input('Masukkan pilihan: '))
        
        # luas persegi
        if input_luas == 1:
            display_luas_persegi()
            
        
        # luas persegi panjang
        elif input_luas == 2:
            display_luas_persegi_panjang()
            
            
        # luas trapesium
        elif input_luas == 3:
            display_luas_trapesium()
        
        # luas lingkaran 
        elif input_luas == 4:
            display_luas_lingkaran()
            
        # luas jajar genjang
        elif input_luas == 5:
            display_luas_jajar_genjang()
            
        # luas layang-layang
        elif input_luas == 6:
            display_luas_layang_layang()
            
        # luas segitiga
        elif input_luas == 7:
            display_luas_segitiga()
    
    
    
    # break
    is_done: str = str(input('Apakah sudah selesai (y/n)? '))
    if is_done.lower() == 'y':
        break
    else:
        None