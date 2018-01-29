""""
@desc:网络爬虫练习
@date:2018-01-29
@author:SZW
"""
#导入request获取请求包
from urllib import request
#导入json数据解析包
import json

"""
@desc:数据获取及解析
@date:2018-01-29
@author:SZW
"""
def write_json_file():
    #定义url变量
    url = 'http://h5.quna.com/hotel_h5/allCities/1/get.html'
    # 获取网络数据
    response = request.urlopen(url)
    #数据读取及编码
    data = response.read()
    result = data.decode("utf-8")
    print(result)
    #将数据进行解析
    target = json.loads(result)
    # 将数据写入文件格式要求每一条数据用换行分割，一条数据，字段之间按\分割
    # 0101\5292\1\北京\.
    # 0201\5293\..
    for data in target:
        colum=''
        code = data["code"]
        id = data["id"]
        isHot = data["isHot"]
        name = data["name"]
        pinyin = data["pinyin"]
        platformCode = data["platformCode"]
        sort = data["sort"]
        colum = code + "|" + str(id) + "|" + isHot + "|" + name + "|" + pinyin + "|" + platformCode + "|" + sort + "\n"
        #写入文件
        write_data(colum)

"""
@desc:文件写入
@date:2018-01-29
@author:SZW
"""
def write_data(clumn):
    with open("data.txt", "a+") as file_obj:
        file_obj.write(clumn)
        file_obj.flush()


"""
@desc:将数据写入数据库
@date:2018-01-29
@author:SZW
"""
def write_data_db(colum):
    print("写入数据库")
    #连接数据库
    #写入数据库
    #关闭数据库

"""
入口函数
"""
if __name__=='__main__':
    print("主函数开始")
    write_json_file()