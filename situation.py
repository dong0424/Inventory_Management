import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from mysql import *

class situationDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('situation.ui', self)
        self.myDB = mySqlDB()

        self.updateList()  # 시작할 때 재고 현황 업데이트

    def updateList(self):
        junphyos = self.myDB.retrieve_all_junphyos()
        self.listWidget.clear()
        for junphyo in junphyos:
            junphyo_info = f"{junphyo['situation']} {junphyo['object']} {junphyo['count']} {junphyo['money']}"
            self.listWidget.addItem(junphyo_info)  # 반복문 내에서 addItem 호출


            
if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # junphyoDialog 인스턴스 생성
    dialog = situationDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
