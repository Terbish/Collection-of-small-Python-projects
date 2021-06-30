import qrcode
import os

data = 'Did you know that the critically acclaimed MMORPG Final Fantasy XIV has a free trial, and includes the entirety of A Realm Reborn AND the award-winning Heavensward expansion up to level 60 with no restrictions on playtime? Sign up, and enjoy Eorzea today!'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='purple', back_color='black')

img.save('D:/ffxiv1.png')
os.startfile('D:/ffxiv1.png')
