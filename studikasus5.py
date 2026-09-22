def biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

    total_biaya = tarif * lama_menginap
    return total_biaya

jenis_kamar = input("Jenis kamar (Standard/Deluxe): ")
check_in = int(input("Tanggal check-in: "))
check_out = int (input("Tanggal check-out: "))

lama_menginap = (check_out - check_in)

total_biaya = biaya(jenis_kamar, lama_menginap)

print("=== PEMESANAN HOTEL ===")
print("Jenis Kamar      :", jenis_kamar)
print("Tanggal Check-in :", check_in)
print("Tanggal Check-out:", check_out)
print("Lama Menginap    :", lama_menginap, "malam")
print("Total Biaya      : Rp", total_biaya)