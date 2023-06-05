import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from customer import CustomerDialog
from goods import GoodsDialog
from junphyo import JunphyoDialog
from customer_list import customer_listDialog
from goods_list import goods_listDialog
from junphyo_list import junphyo_listDialog
from situation import situationDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('mainWindow.ui', self)


        # 창 크기 조절 막기
        self.setFixedSize(self.size())

        # 메뉴 액션 생성
        self.actionCustomer.triggered.connect(self.openDialogCustomer)
        self.actionGoods.triggered.connect(self.openDialogGoods) 
        self.actionjunphyo.triggered.connect(self.openDialogjunphyo)
        self.actioncustomer_list.triggered.connect(self.openDialogcustomer_list)
        self.actiongoods_list.triggered.connect(self.openDialoggoods_list)
        self.actionjunphyo_list.triggered.connect(self.openDialogjunphyo_list)
        self.actionsituation.triggered.connect(self.openDialogsituation)
    
    def openDialogCustomer(self):
        dialog = CustomerDialog()
        dialog.exec_()
        
    def openDialogGoods(self):
        dialog = GoodsDialog()
        dialog.exec_()

    def openDialogjunphyo(self):
        dialog = JunphyoDialog()
        dialog.exec_()
        
    def openDialogcustomer_list(self):
        dialog = customer_listDialog()
        dialog.exec_()

    def openDialoggoods_list(self):
        dialog = goods_listDialog()
        dialog.exec_()
        
    def openDialogjunphyo_list(self):
        dialog = junphyo_listDialog()
        dialog.exec_()
     
    def openDialogsituation(self):
        dialog = situationDialog()
        dialog.exec_()    

if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # MyWindow 인스턴스 생성
    window = MyWindow()

    # 창 보이기
    window.show()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
