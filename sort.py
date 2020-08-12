# -*- coding:utf8 -*-

import os
import shutil

class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''
    def __init__(self):
        self.path = './imgsrc/01'
        self.newpath = './new_pic'

    def tiqu(self):
        filelist = os.listdir(self.path)
        # print(filelist)
        # total_num = len(filelist)
        for file in filelist:
            # print file
            filedir = os.path.join(self.path, file)
            # print filedir
            (shotname, extension) = os.path.splitext(file)
#            a = os.path.splitext(file)
#             b = shotname.split('.')[0]
            b = shotname
            # print(shotname)

            if (int(b) % 10 == 1):
                print (shotname)
                # print(str(filedir))
                shutil.copy(str(filedir), os.path.join(self.newpath, b+'.png'))

if __name__ == '__main__':
    demo = BatchRename()
    demo.tiqu()

