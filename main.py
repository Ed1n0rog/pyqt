import sys
from PyQt5 import QtWidgets
from user_interface import Ui_MainWindow  # Интерфейс, созданный в Qt Designer

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Загружаем интерфейс
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Настройка слайдеров
        self.ui.horizontalSliderDown.valueChanged.connect(
            lambda value: self.ui.horizontalSliderDownTextBar.setText(str(value) + "%")
        )
        self.ui.verticalSliderRight.valueChanged.connect(
            lambda value: self.ui.verticalSliderRightTextBar.setText(str(value) + "%")
        )

        # Обновим значения слайдеров при запуске
        self.ui.horizontalSliderDownTextBar.setText(str(self.ui.horizontalSliderDown.value()) + "%")
        self.ui.verticalSliderRightTextBar.setText(str(self.ui.verticalSliderRight.value()) + "%")

        # Подключение кнопок с помощью lambda
        self.ui.pushButtonLeft.clicked.connect(
            lambda: self.toggle_text(self.ui.textLeft)
        )
        self.ui.pushButtonMid.clicked.connect(
            lambda: self.toggle_text(self.ui.textMid)
        )
        self.ui.pushButtonRight.clicked.connect(
            lambda: self.toggle_text(self.ui.textRight)
        )

        # Установка начального состояния кнопок
        self.set_off(self.ui.textLeft)
        self.set_off(self.ui.textMid)
        self.set_off(self.ui.textRight)

    def toggle_text(self, label):
        # Меняет текст и цвет: если "Off" → "On", иначе обратно
        if label.text() == "Off":
            self.set_on(label)
        else:
            self.set_off(label)

    def set_on(self, label):
        label.setText("On")
        label.setStyleSheet("background-color: green; color: white;")

    def set_off(self, label):
        label.setText("Off")
        label.setStyleSheet("background-color: red; color: white;")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
