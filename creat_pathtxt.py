import os

dir='./imgsrc'
fp = open('./img_path.txt','w+')
imgfile_list = os.listdir('./imgsrc')
imgfile_list.sort(key= lambda x:(x[:]))
#print(img_list)
seqsize = 8
skip = 2   ################ 等间隔循环
for imgfile in imgfile_list:
    filepath = os.path.join(dir,imgfile)
    img_list = os.listdir(filepath)
    img_list.sort(key=lambda x: (x[:-4]))
    #滑窗取序列，步长为8
    for i in range(0, len(img_list)-seqsize, 8):
        for j in range(i, i+seqsize):
             img = img_list[j]
             path = os.path.join(filepath, img)
             if j == i+seqsize-1:
                fp.write(path+'\n')
             #elif j != (i + seqsize - skip):    #将label跳过skip   wyf
             else:
                fp.write(path+' ')

fp.close()