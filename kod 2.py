eded = int(input("Ucreqemli tam eded daxil edin: "))
tekil = eded % 10
onluq = (eded // 10 ) % 10
yuzluk = eded // 100
cem = yuzluk + onluq + tekil
print(f"Yuzluk: {yuzluk}, Onluq: {onluq}, Teklik: {tekil}")
print(f"Reqemlerin cemi = {cem}")
