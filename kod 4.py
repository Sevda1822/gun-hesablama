sagird_sayi = int(input("Sinifdəki şagirdlərin sayını daxil edin: "))
qelem_sayi = int(input("Qələmlərin ümumi sayını daxil edin: "))
her_sagire_dusen = qelem_sayi // sagird_sayi
artiq_qelem = qelem_sayi % sagird_sayi
print(f"Hər şagirdə {her_sagire_dusen} qələm düşür, {artiq_qelem} qələm artıq qalır.")
