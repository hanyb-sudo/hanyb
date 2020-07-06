import time
path="file.txt"

# f=open(path,"w",encoding="utf-8")
# with open("读文件.txt","r",encoding="utf-8") as f1:
#     while True:
#         f.write(f1.read())
#         f1.seek(0)
#         time.sleep(1)  #不设置睡眠时间会使系统一直不断的写
#         # f.flush()
#
#     f.close()


#f.chunks,分段进行读取，循环写入
with open(path, "w") as fp:
    with open("读文件.txt", "r") as f:
        for info in f.chunks:
            fp.write(info)