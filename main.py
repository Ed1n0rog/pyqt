import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore
from user_interface import Ui_MainWindow  # Интерфейс, созданный в Qt Designer
import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = ""

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

        # === Настройка видеопотока с камеры ===

        # Запуск камеры (0 — встроенная веб-камера)
        self.cap = cv2.VideoCapture(0)

        # Таймер для обновления кадров
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # обновление каждые 30 мс

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

    def update_frame(self):
        # Получаем кадр с камеры
        ret, frame = self.cap.read()
        if ret:
            # Меняем цвет с BGR (OpenCV) на RGB (Qt)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Преобразуем изображение в формат Qt
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

            # Показываем изображение в QLabel camera
            self.ui.camera.setPixmap(QtGui.QPixmap.fromImage(q_img))

    def closeEvent(self, event):
        # Закрываем видеопоток при выходе
        if self.cap.isOpened():
            self.cap.release()
        event.accept()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
