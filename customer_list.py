import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from mysql import *

class customer_listDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('customer_list.ui', self)
        self.myDB = mySqlDB()

        self.updateList()  # 시작할 때 고객 목록 업데이트

    def updateList(self):
        customers = self.myDB.retrieve_all_customers()
        self.listWidget.clear()
        for customer in customers:
            customer_info = f"{customer['code']} {customer['name']} {customer['tel']} {customer['addr']}"
            self.listWidget.addItem(customer_info)  # 반복문 내에서 addItem 호출
            
if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # CustomerDialog 인스턴스 생성
    dialog = customer_listDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
