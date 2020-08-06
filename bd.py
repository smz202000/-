import os
import shutil
import time
# !本程序的作用是复制U盘文件
#todo:破坏文件
#*判断是否插入U盘
while True:
    if os.path.exists('H:'):
        try:
            print('已经检测到U盘')
            shutil.copytree('H:',r'C:\Users\Administrator\Desktop'+'\\'+'news')
        except Exception:
            exit('已经复制完毕')
    else:
        print('NO USB')
        time.sleep(9)
