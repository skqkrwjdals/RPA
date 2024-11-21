import qrcode

# 사용자로부터 입력 받기
a = input("이름을 입력하시오 : ")
b = input("학번을 입력하시오 : ")
c = input("전공을 입력하시오 : ")

# 입력받은 정보를 하나의 문자열로 구성
qr_data = f"{a}{b}{c}"

# QR 코드 생성
qr_img = qrcode.make(qr_data)

# QR 코드 이미지 저장
save_path = 'my_info_data.png'
qr_img.save(save_path)

print(f"QR 코드가 '{save_path}'로 저장되었습니다!")
