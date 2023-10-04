import qrcode
import image
qr = qrcode.QRCode(
    version = 15,#15 MEANS THE VERSION OF QR CODE HELP THE NUMBER BIGGER THE CODE IMAGE AND COMPLICATED PICTURE
    box_size = 10, #SIZE  of the box where qr code will display 
    border = 5 # it is the white part of image -- border in all 4 sides with white color
)
data = "https://www.youtube.com/@Ayush-yt9fm"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white")
img.save("test.png")