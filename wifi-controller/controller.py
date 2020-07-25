from kivy.app import App
# kivy.require("1.10.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

class ScrollableLabel(ScrollView):
    text = "blah blah blah"

class AnotherScreen(Screen):
    text = StringProperty("BEGIN")
    def new(self):
        text = "SEE CONSOLE!"


class BackHomeWidget(Widget):
    pass

class MainScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("console.kv")

# class MainApp(App):

#     def goofytest(self):
#         goofy = input("Enter something: ")

#     def build(self):
#         return presentation


import threading

class MainApp(App):
    def goofytest(self):
        thread = threading.Thread(target=self.input_threading)
        thread.daemon = True
        thread.start()

    def input_threading(self):
        goofy = input("Enter something: ")
        print(goofy)

    def build(self):
        return presentation
    
    def process(self):
        print("self.text")



if __name__ == "__main__":
    MainApp().run()
