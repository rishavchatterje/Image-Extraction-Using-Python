import crop
for i in range(0,29):
     str_i = str(i)
     if i<10:
             str_i = "00"+str(i)+".jpg"
     else:
             str_i = "0"+str(i)+".jpg"
     crop.crop_imgs(str_i)
