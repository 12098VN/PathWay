# Buoi 2_2

#Bai 1
dai = 8
rong = 5
print("Dien tich:", dai * rong, "\n")

#Bai 2
print("Ket qua:", 2 ** 10, "\n")

#Bai 3
print(5 > 3)
print(10 == 7)
print(4 <= 4, "\n")

# Bai 4
so1 = int(input("Nhap so nguyen n1:"))
so2 = int(input("Nhap so nguyeb n2:"))

print("Tong: ", so1 + so2, "\n")

# Bai 5
phut = int(input("Nhap tổng phút:"))
print(phut // 60, " gio ", phut % 60, " phut", "\n")

# Bai 6
soNguyen = int(input("Nhap so de lay so du:"))
print("So du khi chia 2 la:", soNguyen % 2, "\n")

# Bai 7
soLy = int(input("Nhap so ly:"))
gia1ly = int(input("gia:"))
print("Tong tien:", soLy * gia1ly, "\n")

# Bai 8
toan = float(input("Nhap diem toan:"))
ly = float(input("Nhap diem ly:"))
hoa = float(input("Nhap diem hoa:"))

print("Diem trung binh:", (toan + ly + hoa) / 3, "\n")

# Bai 9
canNang = float(input("Nhap can nang:"))
chieuCao = float(input("Nhap chieu cao:"))
print("BMI:", canNang / (chieuCao **2))

# Bai 10
nhietDo = float(input("Nhap nhiet do(Do C):"))
print("Nhiet do ", nhietDo, " do C = ", nhietDo * 9 / 5 + 32, " do F")