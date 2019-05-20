#coding:gbk

from singleton import singleton


@singleton
class MysqlOpers:
    
    def __init__(self):
        """连接数据库"""
        print('建立mysql连接')
        
        #伪代码
        #self.db = MySQLdb.connect()

    def select(self):
        print(1111)
        pass

    def insert(self):
        pass



m = MysqlOpers()
n = MysqlOpers()
c = MysqlOpers()

print(id(m))
print(id(n))
print(id(c))

