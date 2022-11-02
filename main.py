from data import Data
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Sport(Button):
    def __init__(self, name="", next_date="", location="", **kwargs):
        super(Sport, self).__init__(**kwargs)
        self.bind(on_press=self.on_press)
        self.text = f'{name}'

    def on_press(self, instance):
        print("I am pressed")

class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        self.sports = Data('https://sites.uclouvain.be/uclsport/api/v1/sport')
        self.lieux = Data('https://sites.uclouvain.be/uclsport/api/v1/lieu')
        self.activites = Data('https://sites.uclouvain.be/uclsport/api/v1/activite')
        self.seances = Data('https://sites.uclouvain.be/uclsport/api/v1/seance')
        for sport in self.sports.data:
            self.add_widget(Button(text=sport['label']))



class UclSport(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    UclSport().run()
