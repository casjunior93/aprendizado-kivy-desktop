from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VendasWindow(BoxLayout):
    #Janela do App
    def __init__(self, **kwargs):
        super().__initi__(**kwargs)

class VendasApp(App):
    #Monta a aplicação
    def build(self):
        return VendasWindow()
    
if __name__ == '__main__':
    VendasApp().run()