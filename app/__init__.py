from win10toast import ToastNotifier


class MyToastNotifier(ToastNotifier):
    def on_destroy(self, hwnd, msg, wparam, lparam):
        pass


toaster = MyToastNotifier()

from app.WebScraper import WebScraper
webscraperInstance = WebScraper()
