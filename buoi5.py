# Bài 1
hoTen = input("Nhap ho va ten:")
namSinh = int(input("Nhap nam sinh:"))
namSinh = 2026 - namSinh
print(f"Xin chào {hoTen}, năm nay bạn {namSinh} tuổi.")

# Bài 2
char1 = input("Nhập kí tự 1: ")
char2 = input("Nhập kí tự 2: ")
char3 = input("Nhập kí tự 3: ")
print(char1,char2,char3,sep = '-')
print("Chúc bạn học tốt Python", end='!!!')

# Bài 3
ho_ten = input("Nhập họ tên: ")
ho_ten = ho_ten.title()
print(f"Tên sau khi chuẩn hóa: {ho_ten}")

# Bài 4
s = input("Nhập chuỗi kí tự: ")
print("Tổng số ký tự: ", len(s))
print("Viết hoa: ", s.upper())

# Bài 5: 
s2 = input("Nhập vào 1 chuỗi: ")
reverse = s2[::-1]
if s2 == reverse:
    print("là chuỗi đối xứng")

# Bài 6:
ma = input("Nhập mã: ")
c1 = ma[0:2]
c2 = ma[3:7]
c3 = ma[8:]
print(f"Loại sp: {c1}")
print(f"Năm sản xuất: {c2}")
print(f"Tên sp: {c3}")

# Bài 7:
s3 = input("Nhập họ và tên: ")
s3 = s3.lower()
i = s3.rfind(" ")
ten = s3[i + 1 :]
ho_lot = s3[:i].replace(" ", "")
email = f"{ten}.{ho_lot}@company.com"
print(f"Email công ty: {email}")

# Bài 8:
tieu_de1 = input("Nhập tiêu đề: ")
vien_tren_duoi = "=" * 40
noi_dung = tieu_de1.center(34)
dong_giua = f"***{noi_dung}***"
print(vien_tren_duoi)
print(dong_giua)
print(vien_tren_duoi)

# Bài 9:
s4 = input("Nhập chuỗi: ").strip().lower()
print(f"Chuỗi sạch: {s4}")
print(f"Độ dài: {len(s4)} ký tự")
print(f"3 ký tự đầu: {s4[:3]} | 3 ký tự cuối: {s4[-3:]}")

#Bài 10:
ten = input("Nhập tên: ").strip().title()
mau = input("Nhập màu yêu thích: ").strip().title()
con_vat = input("Nhập con vật yêu thích: ").strip().title()
ten_dao = ten[::-1][:3].upper()
biet_danh = f"{mau} {con_vat} {ten_dao}"
khung = "=" * 40
tieu_de = "THẺ SIÊU HÙNG".center(40)
print(khung)
print(tieu_de)
print(f"Họ tên    : {ten}")
print(f"Biệt danh : ⚡ {biet_danh} ⚡")
print(khung)