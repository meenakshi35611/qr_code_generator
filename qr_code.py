import qrcode

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' # you can change it to any link you want 

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5) #defines the size, no. of pixels per box and width of box
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white') 
img.save('youtube_qr.png') #saves the qr as image 
