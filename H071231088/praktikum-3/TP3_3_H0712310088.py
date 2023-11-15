try:
    while True:
        S = float(input(""))
        if 0 <= S <= 360:
            # Pertama kita konversi sudut yang dimasukkan ke detik
            detik = int(S * 240) 
            jam = (detik // 3600 + 6) % 24
            

            if 6 <= jam < 12:
                pesan = "Selamat pagi"
            elif 12 <= jam < 15:
                pesan = "Selamat siang"
            elif 15 <= jam < 18:
                pesan = "Selamat sore"
            else:
                pesan = "Selamat malam"

            menit = (detik // 60) % 60
            detik = detik % 60
            waktu = f'{jam:02}:{menit:02}:{detik:02}'

            print(f"{pesan}\n{waktu}")

            #break untuk menghentikan loop setelah selesai
            break
        else:
            print("Sudut harus dalam rentang 0 hingga 360 derajat.")
except EOFError:
    pass