import numpy as np 
import cv2
import os
list0=[]
target_name='zebrafish1'
file_paath='F://VOT2018//'+target_name+'//'
file_dir=file_paath+'img//'
resu_dir=file_paath+'results//'
target_path = "F:/DaSiamRPN_VOT2018/SiamRPN/baseline/"

is_reslt_dir_exi=os.path.exists(resu_dir)
if not is_reslt_dir_exi:
        os.makedirs(resu_dir)
        print("--- ... new folder...  ---")
        print("---  ...OK...  ---")

else:
        print("---  There is this folder!  ---")

for files in os.walk(file_dir):  
    list0.append(files)
img_list=[]
for ii in list0[0][2]:
        img_list.append(ii)
list_img_name=np.array(img_list)
list_img_name.sort() 
# print(len(list_img_name))

path = target_path+target_name+'/'+target_name+'_001.txt'
data=[]
for line2 in open(path):
    data.append(line2)

    #print(line2)
data1=[]
for i in data:
    data1.append(i[:len(i)-1])
data2=[]
data3=[]
for j in data1:
    data2.append(j.split(','))
# print(data2[1])
data4=[]
for k in data2:
    data3=np.array([0.0 if y=='' else float(y) for y in k])
    data4.append(data3)
data_rect=np.array(data4)
# for jj in data5:
#     print(len(jj))
for num in range(0,len(list_img_name)):
    if len(data_rect[num])>2:
        x=int(data_rect[num][0])
        y=int(data_rect[num][1])
        w=int(data_rect[num][2])
        h=int(data_rect[num][3])
        # print(x,y,w,h)
        img_file_name=file_dir+str(list_img_name[num])
                # print(img_file_name)
        src=cv2.imread(img_file_name)
                # cv2.imshow('aa',src)
                # cv2.waitKey(0)
        cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,255),)
                # cv2.imshow('aa',src)
                # cv2.waitKey(0)
        save_file_name=resu_dir+str(list_img_name[num])
        #print(save_file_name)
        cv2.imwrite(save_file_name,src)