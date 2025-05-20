import sys
from PyQt5 import QtWidgets
from user_interface import Ui_MainWindow  # предполагается, что вы используете Qt Designer

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаём интерфейс
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Настраиваем слайдеры
        self.setup_sliders()

        # Обновляем текст на слайдерах при запуске
        self.update_slider_texts()

        # Настраиваем кнопки
        self.setup_buttons()

        # Устанавливаем начальное состояние текста на кнопках
        self.set_initial_button_states()

    def setup_sliders(self):
        # Когда пользователь двигает слайдер, вызывается функция для обновления текста
        self.ui.horizontalSliderDown.valueChanged.connect(self.horizontal_slider_changed)
        self.ui.verticalSliderRight.valueChanged.connect(self.vertical_slider_changed)

    def horizontal_slider_changed(self, value):
        # Обновляем текст рядом с горизонтальным слайдером
        self.ui.horizontalSliderDownTextBar.setText(str(value) + "%")

    def vertical_slider_changed(self, value):
        # Обновляем текст рядом с вертикальным слайдером
        self.ui.verticalSliderRightTextBar.setText(str(value) + "%")

    def update_slider_texts(self):
        # Устанавливаем текст по текущему значению слайдера при запуске
        self.horizontal_slider_changed(self.ui.horizontalSliderDown.value())
        self.vertical_slider_changed(self.ui.verticalSliderRight.value())

    def setup_buttons(self):
        # Подключаем кнопки к функциям
        self.ui.pushButtonLeft.clicked.connect(self.toggle_left)
        self.ui.pushButtonMid.clicked.connect(self.toggle_mid)
        self.ui.pushButtonRight.clicked.connect(self.toggle_right)

    def set_initial_button_states(self):
        # Начальное состояние — выключено (Off)
        self.set_off(self.ui.textLeft)
        self.set_off(self.ui.textMid)
        self.set_off(self.ui.textRight)

    def toggle_left(self):
        self.toggle(self.ui.textLeft)

    def toggle_mid(self):
        self.toggle(self.ui.textMid)

    def toggle_right(self):
        self.toggle(self.ui.textRight)

    def toggle(self, label):
        # Если сейчас Off — включаем, иначе выключаем
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
