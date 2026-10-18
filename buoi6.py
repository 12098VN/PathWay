import random
import string
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
#Bai 9:
n = int(input("Nhập độ dài N: "))
if n >= 4:
  p = [
      random.choice(string.ascii_lowercase),
      random.choice(string.ascii_uppercase),
      random.choice(string.digits),
      random.choice("!@#$%^&*"),
  ]
  all_c = (
      string.ascii_lowercase
      + string.ascii_uppercase
      + string.digits
      + "!@#$%^&*"
  )
  p += [random.choice(all_c) for _ in range(n - 4)]
  random.shuffle(p)
  print("Mật khẩu chuẩn:", "".join(p))


# bai 10
n = int(input("Nhập độ dài mật khẩu: "))
u = input("Có muốn bao gồm chữ hoa (Y/N)? ").strip().upper() == "Y"
d = input("Có muốn bao gồm chữ số (Y/N)? ").strip().upper() == "Y"
s = input("Có muốn bao gồm ký tự đặc biệt (Y/N)? ").strip().upper() == "Y"

chars = string.ascii_lowercase
p = [random.choice(string.ascii_lowercase)]

if u:
  chars += string.ascii_uppercase
  p.append(random.choice(string.ascii_uppercase))
if d:
  chars += string.digits
  p.append(random.choice(string.digits))
if s:
  chars += "!@#$%^&*"
  p.append(random.choice("!@#$%^&*"))

p += [random.choice(chars) for _ in range(n - len(p))]
random.shuffle(p)
print("Mật khẩu tùy chỉnh:", "".join(p))