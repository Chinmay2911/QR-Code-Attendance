from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode

os.system("title ID CARD Generator by Chinmay")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


print('\n\nAll Fields are Mandatory')
print('Avoid any kind of Spelling Mistakes')
#print('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = input('\nEnter Your College Name: ')
company = message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=50)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (600, 75)
message = input('Enter Roll no: ')
rollno = message
color = 'rgb(0, 0, 0)'  
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name = message
color = 'rgb(0, 0, 0)'  
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 350)
message = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)
(x, y) = (250, 350)
message = input('Enter Your Age: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
color = 'rgb(255, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp = message
color = 'rgb(0, 0, 0)'  
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 750)
message = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)' 
draw.text((x, y), message, fill=color, font=font)

# save the edited image

image.save(str(name) + '.png')

img = qrcode.make(str(rollno) + str(name))
img.save(str(rollno)+"." + str(name) + '.bmp')

til = Image.open(name + '.png')
im = Image.open(str(rollno)+"."+str(name) + '.bmp')  
til.paste(im, (600, 350))
til.save(name + '.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))

