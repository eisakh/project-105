import os
import cv2

path = "C:\\Users\\DELL\\Desktop\\PYTHON PROJECTS\\project 105\\Images"

images=[]

for files in os.listdir(path):
    
    file,ext=os.path.splitext(files)
   

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
     file_name=path+"\\"+files

    
     images.append(file_name)


count=len(images)
print(count)

frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
print(size)
output=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)


for i in range(0,count-1,1):
   frame=cv2.imread(images[i])
   output.write (frame)

output.release()
print("video saved")






