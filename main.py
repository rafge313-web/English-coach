from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class EnglishCoachApp(MDApp):
    def build(self):
        return MDLabel(text="مرحباً بك في تطبيق English Coach!", halign="center")

if __name__ == '__main__':
    EnglishCoachApp().run()
  
