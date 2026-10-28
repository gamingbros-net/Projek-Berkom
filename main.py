import valid

daftar_film = [
    {"id": "F01", "judul": "Film A", "durasi": 120},
    {"id": "F02", "judul": "Film B", "durasi": 105},
    {"id": "F03", "judul": "Film C", "durasi": 130}
]

jadwal_film = [
    {"id": "F01", "harga": 35000, "jadwal": {"J01": "12:00", "J02" : "15:00"}},
    {"id": "F02", "harga": 40000, "jadwal": {"J01": "13:00"}},
    {"id": "F03", "harga": 40000, "jadwal": {"J01": "16:00", "J02" : "19:00"}}
]
while True:
    count = 1

    print("Welcome to XXI")
    print("--------------")
    print("Pilih Film yang ingin ditonton")

    for film in daftar_film:
        print(f"{count}. {film.get("judul")}")
        count += 1
    print(f"{count}. Exit Menu")
    print()
    count = 1
    while True:
        film_terpilih = input("Masukkan angka menu untuk film yang diinginkan: ")
        film_terpilih = valid.valid_int(film_terpilih, "Tolong masukkan input yang valid")
        print()
        if film_terpilih is None:
            continue
        elif film_terpilih == len(daftar_film)+1:
            print("Sampai Jumpa Kembali!")
            break
        elif film_terpilih < 1 or film_terpilih >= len(daftar_film)+1:
            print("Tolong masukkan angka yang ada di menu pilihan film")
            print()
    for i in range(1, len(daftar_film)+1):
        if film_terpilih == i:
            film_terpilih = daftar_film[film_terpilih-1].get("id")
            print(f'Anda memilih film "{daftar_film[i-1].get("judul")}"')
            print("-------------------------------------")
            print("Pilih jadwal film yang ingin ditonton")
            print()
            for jadwal in jadwal_film:
                if jadwal["id"] == film_terpilih:
                    print(f"Harga: {jadwal.get("harga")}")
                    for key, value in (jadwal.get("jadwal")).items():
                        print(f"Jadwal {count}: {value}")
                        count += 1
    while True:
        jadwal_pilihan = input("Masukkan jadwal yang diinginkan: ")
        jadwal_pilihan = valid.valid_int(jadwal_pilihan, "Tolong masukkan input yang valid")
        print()
        if jadwal_pilihan is None:
            continue
        elif jadwal_pilihan == len(jadwal_film)+1:
            print("Sampai Jumpa Kembali!")
            break
        elif jadwal_pilihan < 1 or jadwal_pilihan >= len(jadwal_film)+1:
            print("Tolong masukkan angka yang ada di menu pilihan film")
            print()
    for i in range(1, len(jadwal_film)+1):
            if jadwal_pilihan == i:
                if isinstance(d, dict):
                print(sum(count_leaves(v) for v in d.values()))
    print("-----------------------")
    print("RINGKASAN PESANAN")
    print(f"Film: {film_pilihan}")