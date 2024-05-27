from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
from django.test import TestCase

class MySQLDatabaseConnectionTest(TestCase):
    def test_mysql_connection(self):
        # ใช้ connection ของฐานข้อมูล MySQL ตามที่ระบุใน settings.py
        mysql_connection = connections['mysql']
        
        # ทดสอบการเชื่อมต่อกับฐานข้อมูล MySQL
        try:
            # ลองสร้างการเชื่อมต่อ
            mysql_connection.ensure_connection()
            
            # หากการเชื่อมต่อสำเร็จ ให้แสดงข้อความนี้
            print("Connection to MySQL database successful.")
            
            # การเชื่อมต่อสำเร็จ
            self.assertTrue(True)
        except OperationalError as e:
            # หากมีปัญหาในการเชื่อมต่อ ให้แสดงข้อผิดพลาด
            print(f"Failed to connect to MySQL database: {str(e)}")
            
            # การเชื่อมต่อล้มเหลว
            self.fail("Connection to MySQL database failed.")
