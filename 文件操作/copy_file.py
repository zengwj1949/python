# 些脚本用于把指定的文件复制到另一个文件；

# 导入相关模块；
from sys import argv
from os.path import exists

# 传递参数；
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# 打开并读取源文件；
in_file = open(from_file)
indate = in_file.read()

# print(f"The input file is {len(indate)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

# 打开目标文件，并且是写入状态；
out_file = open(to_file, 'w')
out_file.write(indate)

print("Alright, all done.")

out_file.close()
in_file.close()
