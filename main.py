from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp

kv = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    Label:
        text: 'DK JAN Suvidha'
        font_size: '24sp'
        size_hint_y: None
        height: self.texture_size[1] + dp(20)

    TextInput:
        id: name_input
        hint_text: 'Enter your name'
        multiline: False

    Button:
        text: 'Greet'
        size_hint_y: None
        height: dp(48)
        on_release: app.greet()

    Label:
        id: greet_label
        text: ''
'''

class MainApp(App):
    def build(self):
        self.root = Builder.load_string(kv)
        return self.root

    def greet(self):
        name = self.root.ids.name_input.text.strip()
        if not name:
            name = 'Guest'
        self.root.ids.greet_label.text = f'Namaste, {name}!'

if __name__ == '__main__':
    MainApp().run()
