
import shutil, os
import logging, traceback
import time
import zipfile
'''
文件和目录操作
'''

# 操作目录；
dir = r'D:\file'
curr_time = time.strftime("%y-%m-%d_%H%M%S")
print(f'Curry Time is: {curr_time}')

# 切换目录；
os.chdir('d:\\')
print(os.getcwd())

try:
    # 复制文件，但保留原有的文件名；
    shutil.copy(f'{dir}\\a.txt', f'd:\\test')
    # 复制文件，复制后的文件添加了时间戳；
    shutil.copy(f'{dir}\\a.txt', 'd:\\test\\a_test_%s.txt' % (curr_time))
    # 复制整个文件夹；
    shutil.copytree(f'{dir}', f'{dir}\\a_test_{curr_time}')

except Exception as e:
    msg = traceback.format_exc()
    logging.error(msg)



'''
文件和目录的压缩及解压缩
'''

# 1、压缩文件；
filezip = zipfile.ZipFile('d:\\python.zip', mode = 'w')

os.chdir('d:\\test')
print(os.getcwd())
# 压缩a.txt;
filezip.write('a.txt', compress_type = zipfile.ZIP_DEFLATED)

# 把b.txt添加到压缩文件；
filezip.write('b.txt', compress_type = zipfile.ZIP_DEFLATED)
filezip.close()
print("Zipfile is succry.")


# 2、解压缩；
# 把文件解压到F盘；
os.chdir('F:\\')
print(os.getcwd())

filezip = zipfile.ZipFile('d:\\python.zip')
filezip.extractall()
filezip.close()
print("unzip is ok.")


# 3、压缩目录；
# 第一个参数是压缩后的目录名称，第二参数是压缩格式，第三个参数是待压缩的目录；
shutil.make_archive('F:\\dirzip', 'zip', root_dir='D:\\test')

# 4、解压目录；
# 指定解压到的目录；
os.chdir('D:\\')
shutil.unpack_archive('F:\\dirzip.zip')
print(os.getcwd())
