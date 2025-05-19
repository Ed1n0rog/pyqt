import sys
from typing import Union
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from user_interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    PERCENT_SUFFIX = "%"
    DEFAULT_OFF_TEXT = "Off"
    DEFAULT_ON_TEXT = "On"
    
    def __init__(self):
        super().__init__()
        
        # Initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self._setup_sliders()
        self._initialize_slider_values()
        self._setup_buttons()
        self._initialize_button_states()
    
    def _setup_sliders(self) -> None:
        """Setup connections for all sliders."""
        self._connect_slider(
            self.ui.horizontalSliderDown, 
            self.ui.horizontalSliderDownTextBar
        )
        self._connect_slider(
            self.ui.verticalSliderRight, 
            self.ui.verticalSliderRightTextBar
        )
    
    def _connect_slider(self, slider: QtWidgets.QSlider, text_bar: QtWidgets.QLabel) -> None:
        """Connect slider value change to text update.
        
        Args:
            slider: QSlider instance to monitor
            text_bar: QLabel to display the slider value
        """
        slider.valueChanged.connect(
            lambda value: self._update_slider_text(value, text_bar)
        )
    
    def _initialize_slider_values(self) -> None:
        """Initialize slider text bars with current values."""
        self._update_slider_text(
            self.ui.horizontalSliderDown.value(), 
            self.ui.horizontalSliderDownTextBar
        )
        self._update_slider_text(
            self.ui.verticalSliderRight.value(), 
            self.ui.verticalSliderRightTextBar
        )
    
    def _update_slider_text(self, value: Union[int, float], text_bar: QtWidgets.QLabel) -> None:
        """Update slider text bar with formatted value.
        
        Args:
            value: Current slider value
            text_bar: QLabel to update with the value
        """
        try:
            text_bar.setText(f"{value}{self.PERCENT_SUFFIX}")
        except (TypeError, AttributeError) as e:
            print(f"Error updating slider text: {e}")

    def _setup_buttons(self) -> None:
        """Setup connections for all buttons."""
        self._connect_button(
            self.ui.pushButtonLeft,
            self.ui.textLeft
        )
        self._connect_button(
            self.ui.pushButtonMid,
            self.ui.textMid
        )
        self._connect_button(
            self.ui.pushButtonRight,
            self.ui.textRight
        )
    
    def _connect_button(self, button: QtWidgets.QPushButton, text_field: QtWidgets.QLabel) -> None:
        """Connect button click to text field update.
        
        Args:
            button: QPushButton instance to monitor
            text_field: QLabel to update on button click
        """
        button.clicked.connect(
            lambda: self._toggle_button_state(text_field)
        )
    
    def _initialize_button_states(self) -> None:
        """Initialize all button text fields to default OFF state."""
        self._set_off_state(self.ui.textLeft)
        self._set_off_state(self.ui.textMid)
        self._set_off_state(self.ui.textRight)
    
    def _toggle_button_state(self, text_field: QtWidgets.QLabel) -> None:
        """Toggle text field state between ON and OFF.
        
        Args:
            text_field: QLabel to toggle
        """
        if text_field.text() == self.DEFAULT_OFF_TEXT:
            self._set_on_state(text_field)
        else:
            self._set_off_state(text_field)
    
    def _set_on_state(self, text_field: QtWidgets.QLabel) -> None:
        """Set text field to ON state (green background).
        
        Args:
            text_field: QLabel to update
        """
        text_field.setText(self.DEFAULT_ON_TEXT)
        text_field.setStyleSheet("background-color: green; color: white;")
    
    def _set_off_state(self, text_field: QtWidgets.QLabel) -> None:
        """Set text field to OFF state (red background).
        
        Args:
            text_field: QLabel to update
        """
        text_field.setText(self.DEFAULT_OFF_TEXT)
        text_field.setStyleSheet("background-color: red; color: white;")


def main() -> None:
    """Application entry point."""
    app = QtWidgets.QApplication(sys.argv)
    
    try:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Application error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()