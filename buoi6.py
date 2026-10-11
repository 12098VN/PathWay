import random

# Bài 1
xucxac = [1, 2, 3, 4, 5, 6]
print("Bạn đã gieo ra mặt: ", random.choice(xucxac))

# Bài 2:
tenNgDung = input("Nhập vào tên người dùng: ")
print("Ký tự may mắn của bạn là: ", random.choice(tenNgDung))

# Bài 3:
tinhTu = ["Cool", "Fast", "Smart", "Happy"]
danhTu = ["Tiger", "Eagle", "Panda", "Coder"]

print("Username gợi ý cho bạn: ", random.choice(tinhTu), random.choice(danhTu), sep = "")

# Bài 4:
chuSo = "0123456789"
print(random.choice(chuSo),random.choice(chuSo),random.choice(chuSo),random.choice(chuSo), sep ="")

# Bài 5:
passWidth = int(input("Nhập vào độ dài mk: "))
chuCai = "abcdefghijklmnopqrstuvwxyz"
chuHoa = "ABCDEFGHIJKLMNOPQRSVUTWXYZ"
password = ""
for i in range(passWidth):
    password += random.choice(chuCai)
print(f"Mật khẩu của bạn: {password}")

# Bài 6:
cau = input("Nhập vào 1 câu bất kỳ: ")
danhSachKyTu = cau.split()
random.shuffle(danhSachKyTu)
cau_sau_khi_dao = " ".join(danhSachKyTu)
print(f"Kết quả xáo trộn: {cau_sau_khi_dao}")

# Bài 7:
n = int(input("Nhập độ dài mật khẩu: "))
ktdb = "!@#$%^&*"
pass7 = [
    random.choice(chuCai),
    random.choice(chuHoa),
    random.choice(chuSo),
    random.choice(ktdb)
]
tat_ca_ky_tu = chuCai + chuHoa + chuSo + ktdb

for i in range(n - 4):
    pass7.append(random.choice(tat_ca_ky_tu))

random.shuffle(pass7)

passFinal = "".join(pass7)

print(f"Mật khẩu an toàn: {passFinal}")

# Bài 8: 
n = int(input("Nhập độ dài N: "))
ktdb2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*abcdefghijklmnopqrstuvwxyz0123456789"

print("--- GỢI Ý MẬT KHẨU ---")

for i in range(1, 4):
    pass_ngau_nhien = ""
    for j in range(n):
        pass_ngau_nhien += random.choice(ktdb2)
    

    print(f"{i}. {pass_ngau_nhien}")