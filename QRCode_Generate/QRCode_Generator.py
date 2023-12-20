import qrcode
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=7,border=1)
qr.add_data("https://www.youtube.com")
img=qr.make_image(fill_color="green",back_color="white")
img.save("youtube.jpg")

#Read QRCode
import cv2
d=cv2.QRCodeDetector()
val,points,straight_qrcode=d.detectAndDecode(cv2.imread("youtube.jpg"))
print(val)