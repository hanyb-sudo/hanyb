# 引入了三方库
from PIL import Image

# 打开图片
im = Image.open(r"D:\python\girl.jpg")

print(im)
# 查看图片信息
print(im.format,im.size,im.mode)

# 设置图片的大小
im.thumbnail((500,500))

# 保存成新的图片
im.save("girl.jpg","JPEG")

