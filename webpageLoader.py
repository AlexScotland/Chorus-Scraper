def render(source_url):
    """Fully render HTML, JavaScript and all."""

    import sys, time
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, url):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.load(QUrl(url))
            self.app.exec_()

        def _loadFinished(self, result):
            # This is an async call, you need to wait for this
            # to be called before closing the app
            time.sleep(5)
            self.page().toHtml(self._callable)

        def _callable(self, data):
            self.html = data
            # Data has been stored, it's safe to quit the app
            self.app.quit()
    return Render(source_url).html
