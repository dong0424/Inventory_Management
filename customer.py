import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
from mysql import mySqlDB

class CustomerDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('customer.ui', self)
        self.myDB = mySqlDB()
        self.searched = False

        # 버튼 클릭 이벤트 처리
        self.pushButton_Customer1.clicked.connect(self.onSearchClick)

        # 입력 필드 초기 상태 설정
        self.setFieldsEnabled(False)

    def clearLineEdit(self):
        self.lineEdit_1.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.searched = False

    def onSearchClick(self):
        search_string = self.lineEdit_1.text()
        if search_string:  # 검색 문자열이 있을 때만 검색을 수행
            print('Search customer')
            result = self.myDB.custom_search(search_string)

            if result:
                if result['code'] == search_string:
                    self.lineEdit_1.setText(str(result['code']))
                    self.lineEdit_2.setText(result['name'])
                    self.lineEdit_3.setText(result['tel'])
                    self.lineEdit_4.setText(result['addr'])
                    self.searched = True
                else:
                    self.clearLineEdit()
                    QMessageBox.information(self, '경고문', '조회된 결과가 없습니다.')
            else:
                self.clearLineEdit()
                QMessageBox.information(self, '경고문', '조회된 결과가 없습니다.')
        else:  # 검색 문자열이 없을 때
            self.clearLineEdit()
            QMessageBox.information(self, '알림', '검색어를 입력하세요.')

        # 입력 필드 상태 설정
        self.setFieldsEnabled(not self.searched)

    def setFieldsEnabled(self, enabled):
        self.lineEdit_2.setEnabled(enabled)
        self.lineEdit_3.setEnabled(enabled)
        self.lineEdit_4.setEnabled(enabled)
        # 검색 버튼 클릭 후 검색된 상태가 아닌 경우 입력 필드를 비활성화
        if not self.searched:
            self.lineEdit_2.setReadOnly(True)
            self.lineEdit_3.setReadOnly(True)
            self.lineEdit_4.setReadOnly(True)

if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # CustomerDialog() 인스턴스 생성
    dialog = CustomerDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
