from app import webscraperInstance
from infi.systray import SysTrayIcon
hover_text = "Seek Job Postings"


def close(sysTrayIcon):
    exit()


if __name__ == '__main__':
    menu_options = ()
    sysTrayIcon = SysTrayIcon("main.ico", hover_text, menu_options, on_quit=close)
    sysTrayIcon.start()
    webscraperInstance.run()
