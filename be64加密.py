#byDT
import base64 #导入base64模块
import os #导入os文件，保存文件
url=""
#取url为名称，要解密的文本
str_url = base64.b64decode(url).decode("utf-8") #bese64-utf8解密，str_url为名字
print(str_url,"\n解密完成") #打印解密后的文本和文字
with open('解密完成.txt','w') as f: f.write(str_url) #保存str_url文本到test文件
print("文件保存在",os.getcwd(),"\解密完成.txt")