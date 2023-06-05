import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from mysql import *

class junphyo_listDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('junphyo_list.ui', self)
        self.myDB = mySqlDB()

        self.listWidget.clear()  # 생성자에서 clear() 호출

        self.updateList()  # 시작할 때 전표 목록 업데이트

    def updateList(self):
        junphyos = self.myDB.retrieve_all_junphyos()
        junphyo_info_list = []
        for junphyo in junphyos:
            junphyo_info = f"{junphyo['Year']} {junphyo['date1']} {junphyo['date2']} {junphyo['situation']} {junphyo['place']} {junphyo['object']} {junphyo['count']} {junphyo['money']}"
            junphyo_info_list.append(junphyo_info)
        self.listWidget.addItems(junphyo_info_list)

            
if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # junphyoDialog 인스턴스 생성
    dialog = junphyo_listDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
