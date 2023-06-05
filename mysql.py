import sys
import pymysql.cursors
from PyQt5.QtWidgets import QApplication
import pymysql

class mySqlDB():
    def __init__(self):
        pymysql.version_info = (1, 4, 2, "final", 0)
        pymysql.install_as_MySQLdb()
        self.connection = pymysql.connect(
            host='localhost',
            user='dong000424', 
            passwd='nun000424!',              
            db='aisw',
            charset='utf8',    
            port=3306,
            cursorclass=pymysql.cursors.DictCursor)

    # customer methods

    def custom_search(self, key):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM custom WHERE code LIKE %s OR name LIKE %s OR tel LIKE %s OR addr LIKE %s"
            key = '%' + key + '%'
            cursor.execute(sql, (key, key, key, key))
            result = cursor.fetchone()
        return result

    # Goods methods

    def goods_search(self, key):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM goods WHERE codenumber LIKE %s OR goodname LIKE %s OR Initial_inventory LIKE %s OR price LIKE %s"
            key = '%' + key + '%'
            cursor.execute(sql, (key, key, key, key))
            result = cursor.fetchone()
        return result
    
     # junphyo methods

    def junphyo_search(self, key):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM junphyo WHERE Year LIKE %s OR date1 LIKE %s OR date2 LIKE %s OR situation LIKE %s OR place LIKE %s OR object LIKE %s OR count LIKE %s OR money LIKE %s"
            key = '%' + key + '%'
            cursor.execute(sql, (key, key, key, key, key, key, key, key))
            result = cursor.fetchone()
        return result
    
    # custmor_list methods
    
    def retrieve_all_customers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM custom")
        result = cursor.fetchall()
        return result  
 
    # goods_list methods
    
    def retrieve_all_goods(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM goods")
        result = cursor.fetchall()
        return result
    
    # junphyo_list methods
    
    def retrieve_all_junphyos(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM junphyo")  # 쿼리 수정
        result = cursor.fetchall()
        return result
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = mySqlDB()
    
    sys.exit(app.exec_())
