import os
import rumus_luas

while True:
    os.system('cls')
    print(f'\n{'OPERASI':=^50}')
    
    # pilih operasi
    print('''
    0. Keluar
    1. Luas
    ''')
    input_operasi: int = int(input('Masukkan pilihan: ')) 
    
    # keluar
    if input_operasi == 0:
        break
    
    # pilih operasi luas
    elif input_operasi == 1:
        print('''
        1. Luas Persegi
        2. Luas Persegi Panjang
        3. Luas Trapesium
        4. Luas Lingkaran
        5. Luas Jajar Genjang
        6. Luas Layang - Layang
        7. Luas Segitiga
        ''')
        input_luas: int = int(input('Masukkan pilihan: '))
        
        # luas persegi
        if input_luas == 1:
            sisi: float = float(input('Masukkan panjang sisi: '))
            hasil: float = rumus_luas.luas_persegi(sisi)
            print(f'{sisi} x {sisi} = {hasil:.2f}')
        
        # luas persegi panjang
        elif input_luas == 2:
            panjang: float = float(input('Masukkan panjang: '))
            lebar: float = float(input('Masukkan lebar: '))
            hasil: float = rumus_luas.luas_persegi_panjang(panjang, lebar)
            print(f'{panjang} x {lebar} = {hasil:.2f}')
            
        # luas trapesium
        elif input_luas == 3:
            atas: float = float(input('Masukkan sisi atas: '))
            bawah: float = float(input('Masukkan sisi bawah: '))
            tinggi: float = float(input('Masukkan tinggi: '))
            hasil: float = rumus_luas.luas_trapesium(atas, bawah, tinggi)
            print(f'({atas} + {bawah}) * {tinggi} / 2 = {hasil:.2f}')
        
        # luas lingkaran 
        elif input_luas == 4:
            radius: float = float(input('Masukkan radius: '))
            hasil: float = rumus_luas.luas_lingkaran(radius)
            print(f'22 / 7 * {radius} ** 2 = {hasil:.2f}')
            
        # luas jajar genjang
        elif input_luas == 5:
            alas: float = float(input('Masukkan alas: '))
            tinggi: float = float(input('Masukkan tinggi: '))
            hasil: float = rumus_luas.luas_jajar_genjang(alas, tinggi)
            print(f'{alas} x {tinggi} = {hasil:.2f}')
            
        # luas layang-layang
        elif input_luas == 6:
            d1: float = float(input('Masukkan d1: ')) 
            d2: float = float(input('Masukkan d2: ')) 
            hasil: float = rumus_luas.luas_layang_layang(d1, d2)
            print(f'{d1} x {d2} / 2 = {hasil:.2f}')
            
        # luas segitiga
        elif input_luas == 7:
            alas: float = float(input('Masukkan alas: '))
            tinggi: float = float(input('Masukkan tinggi: '))
            hasil: float = rumus_luas.luas_segitiga(alas, tinggi)
            print(f'{alas} x {tinggi} = {hasil:.2f}')
    
    
    
    # break
    is_done: str = str(input('Apakah sudah selesai (y/n)? '))
    if is_done.lower() == 'y':
        break
    else:
        None