
import random
def random_name():
        first_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤",
                      "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水",
                      "窦", "章", "云", "苏", "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方"]
        second_name = ["静", "霞", "雪", "思", "平", "东", "志宏", "峰", "磊", "雷", "文", "明浩", "光", "超", "军", "达", "伟", "华", "建国",
                       "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕","风","博凯","徐坤","震","倩倩","鹏","均","达智","欣欣","易鹏","蕾蕾"]
        name = random.choice(first_name) + random.choice(second_name)
        return name


if __name__ == '__main__':
    i=0
    for i in range(0,270):
     print(random_name())
     i+=1
