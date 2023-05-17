import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout
#import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Browser")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView(self)
        self.browser.load(QUrl("https://www.google.com"))

        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.address_bar)
        self.layout.addWidget(self.browser)

        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def load_url(self):
        url = self.address_bar.text()
        self.browser.load(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

#pip code to install PyQt5