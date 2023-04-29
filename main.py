import qrcode

# Define the payload text
payload = "Сюда текст"

# Generate the QR code image
img = qrcode.make(payload)

# Save the image file
img.save("qrcode.png")