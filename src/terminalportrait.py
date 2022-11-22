import numpy as np
from PIL import Image




img = Image.open("C:\\Users\\eziod\\Documents\\yy3.jpg")
arr = np.array(img)
print(arr[0][0])
print(arr.shape)
arr.shape[0] 
arr.shape[1] 

# print(arr[719][0])

if len(arr.shape)==3:
    arr2D = arr[:,:,0]
    arr2D_rescale = arr2D.copy()//37
    print(np.amax(arr2D_rescale))
else:
    arr2D_rescale = arr.copy()//37

# 6 -> @
# 5 -> M
# 4 -> X
# 3 -> /
# 2 -> ;
# 1 -> -
# 0 -> ,

payload=''

for line in arr2D_rescale:
    for score in line:
        if score==6:
            payload += ",,"
        if score==5:
            payload += "--"
        if score==4:
            payload += ";;"
        if score==3:
            payload += "//"
        if score==2:
            payload += "XX"
        if score==1:
            payload += "MM"
        if score==0:
            payload += "@@"
    payload += "\n"


text_file = open("data4_2_b.txt", "w")
text_file.write(payload)
text_file.close()
