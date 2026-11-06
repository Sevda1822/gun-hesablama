ad_soyad = input("Ad ve soyadinizi daxil edin: ")
sozler = ad_soyad.split()
inisiallar = ""
for soz in sozler:
  inisiallar += soz[0].upper() + "."
print(inisiallar)
