import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from mysql import *

class goods_listDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('goods_list.ui', self)
        self.myDB = mySqlDB()

        self.listWidget.clear()  # 생성자에서 clear() 호출

        self.updateList()  # 시작할 때 상품 목록 업데이트

    def updateList(self):
        goods = self.myDB.retrieve_all_goods()
        good_info_list = []
        for good in goods:
            good_info = f"{good['codenumber']} {good['goodname']} {good['Initial_inventory']} {good['price']}"
            good_info_list.append(good_info)
        self.listWidget.addItems(good_info_list)


           
if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # goodsDialog 인스턴스 생성
    dialog = goods_listDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
