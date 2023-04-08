import pymysql


class Mysql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = self.connection()
        self.cursor = self.db.cursor()
        # 使用cursor()方法获取操作游标

    def connection(self):
        # try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # print("连接成功")
            return db
        # except:
        #     print("连接失败")

    def readall(self, table):
        sql = "select * from `" + table + "`;"
        try:
            self.cursor.execute(sql)
            # 执行SQL语句
            results = self.cursor.fetchall()
            # 获取所有记录列表
            for i in results:
                for j in i:
                    print(j, end="\t")
                print()
            return results
        except:
            print("读取失败")

    def readone(self, table, start):
        sql = "select * from `" + table + "` limit " + start + ",1;"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            for i in result:
                print(i, end="\t")
            print()
        except:
            print("读取失败")

    def delete(self, table, key, value):
        sql = "delete from `" + table + "` where `" + key + "`=" + value + ";"
        try:
            self.cursor.execute(sql)
            print("删除成功")
        except:
            print("删除失败")

    def insert(self, table, keys, values):
        sql = "insert into `" + table + "` (" + keys + ") values (" + values + ");"
        self.cursor.execute(sql)

    def update(self, table, varkey, varvalue, key, value):
        sql = "update `" + table + "` set `" + varkey + "` = '" + varvalue + "' where `" + key + "`=" + value + ";"
        try:
            self.cursor.execute(sql)
            print("修改成功")
        except:
            print("修改失败")

    def close(self):
        self.db.close()

# db = Mysql("127.0.0.1", "root", "123456", "pikachu")
# # db.readall("users")
# # db.readone("users", "0")
# # db.insert("users", "id,username,password,level", "4,'root','root',4")
# # db.delete("users","id","4")
# # db.update("users","level","5","id","4")
# db.close()
