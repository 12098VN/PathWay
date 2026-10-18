import random

print("========================================")
print("     TRÌNH TẠO MẬT KHẨU NGẪU NHIÊN        ")
print("========================================")

chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
dac_biet = "!@#$%^&*()_+"

dai = int(input("👉 Nhập độ dài mật khẩu (ví dụ 12): "))
hoa = input("👉 Bao gồm chữ HOA? (y/n): ").strip().lower()
so = input("👉 Bao gồm chữ SỐ? (y/n): ").strip().lower()
DacBiet = input("👉 Bao gồm KÝ TỰ ĐẶC BIỆT? (y/n): ").strip().lower()

kho = chu_thuong
if hoa == "y":
  kho += chu_hoa
if so == "y":
  kho += chu_so
if DacBiet == "y":
  kho += dac_biet

mat_khau = ""
for _ in range(dai):
  mat_khau += random.choice(kho)

print("----------------------------------------")
print("🔑 MẬT KHẨU CỦA BẠN:", mat_khau)
print("----------------------------------------")