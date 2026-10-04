import qrcode as qr

url = "https://youtube.com/shorts/sD5w9Ue5X9E?si=wQz-j8D1bWWeYYRu"

code = qr.QRCode(
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=15,  # Increase or decrease to change image size
    border=6,
)
code.add_data(url)
code.make(fit=True)

colored_img = code.make_image(
    fill_color="blue",
    back_color="yellow",
)
colored_img.save("myqrcode.png")

