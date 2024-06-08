rumus_map = {
    "1": lambda sisi: sisi**2, # persegi
    "2": lambda panjang, lebar: panjang * lebar, # persegi panjang
    "3": lambda atas, alas, tinggi: (atas + alas) * tinggi / 2,
    "4": lambda radius: 22 / 7 * radius, #lingkaran
}

satuan_map = {
    "km": "kilometer",
    "hm": "hektometer",
    "dam": "dekameter",
    "m": "meter",
    "dm": "desimeter",
    "cm": "centimeter",
    "mm": "milimeter",
}

konversi_satuan = {
    # km ke
    "km":{
        "hm": lambda x: x * 10, 
        "dam": lambda x: x * 100,
        "m": lambda x: x * 1000,
        "dm": lambda x: x * 10000,
        "cm": lambda x: x * 100000,
        "mm": lambda x: x * 1000000,
    },
    
    # hm ke  
    "hm":{
        "km": lambda x: x / 10,
        "dam": lambda x: x * 10,
        "m": lambda x: x * 100,
        "dm": lambda x: x * 1000,
        "cm": lambda x: x * 10000,
        "mm": lambda x: x * 100000,
    },
    "dam":{
        "km": lambda x: x / 100,
        "hm": lambda x: x / 10,
        "m": lambda x: x * 10,
        "dm": lambda x: x * 100,
        "cm": lambda x: x * 1000,
        "mm": lambda x: x * 10000,
    },
    "m":{
        "km": lambda x: x / 1000,
        "hm": lambda x: x / 100,
        "dam": lambda x: x * 10,
        "dm": lambda x: x * 10,
        "cm": lambda x: x * 100,
        "mm": lambda x: x * 1000,
    },
    "dm":{
        "km": lambda x: x / 10000,
        "hm": lambda x: x / 1000,
        "dam": lambda x: x / 100,
        "m": lambda x: x / 10,
        "cm": lambda x: x * 10,
        "mm": lambda x: x * 100,
    },
    "cm":{
        "km": lambda x: x / 100000,
        "hm": lambda x: x / 10000,
        "dam": lambda x: x / 1000,
        "m": lambda x: x / 100,
        "dm": lambda x: x / 10,
        "mm": lambda x: x * 10,
    },
    "mm":{
        "km": lambda x: x / 1000000,
        "hm": lambda x: x / 100000,
        "dam": lambda x: x / 10000,
        "m": lambda x: x / 1000,
        "dm": lambda x: x / 100,
        "cm": lambda x: x / 10,
    },
}
    
    
while True:
    print("""
    0. Exit
    1. Konverter Satuan
    2. Luas Persegi
    3. Luas Persegi Panjang
    4. Luas Trapesium
    5. Luas Lingkaran  
    """)

    operasi = str(input("Masukkan opsi yang ingin dilakukan: "))
    
    # persegi
    if operasi == "0":
        break
    
    elif operasi == "1":
        angka = float(input("Masukkan angka: "))
        satuan_awal = str(input("Masukkan satuan awal: "))
        satuan_akhir = str(input("Masukkan satuan akhir: "))
        if satuan_awal == satuan_akhir:
            pass
        elif satuan_awal.lower() in satuan_map and satuan_akhir.lower() in satuan_map:
            print(f"{angka} {satuan_awal} = {konversi_satuan[satuan_awal][satuan_akhir](angka):,.2f} {satuan_akhir}")
        else:
            print("satuan tidak valid")
            continue
                
                
    elif operasi == "2":
        sisi = float(input("Masukkan panjang sisi: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"{sisi} {satuan} x {sisi} {satuan} = {rumus_map["1"](sisi)}")
    
    # persegi panjang
    elif operasi == "3":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"{panjang} {satuan} x {lebar} {satuan} = {rumus_map["2"](panjang, lebar)} {satuan_map[satuan]}")
    
    # trapesium
    elif operasi == "4":
        atas = float(input("Masukkan panjang atas: "))
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"({atas} {satuan} + {alas} {satuan}) x {tinggi} {satuan} / 2 = {rumus_map["3"](atas, alas, tinggi)} {satuan_map[satuan]}")
            
    # lingkaran
    elif operasi == "5":
        radius = float(input("Masukkan radius: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"22 / 7 x {radius} {satuan} x {radius} {satuan} = {rumus_map["4"](radius):.2f} {satuan_map[satuan]}")        
        
    # break
    is_keluar = str(input("\nApakah ingin keluar (y/n)?"))
    if is_keluar == "y":
        break
    elif is_keluar == "n":
        None
    else:
        print("Unknown Input")
        break
    
    
    
    
    
    
    
    
    
    

        

