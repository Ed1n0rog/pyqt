import sys
from typing import Union
from PyQt5 import QtWidgets
from user_interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    PERCENT_SUFFIX = "%"
    
    def __init__(self):
        super().__init__()
        
        # Initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self._setup_sliders()
        self._initialize_slider_values()
    
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