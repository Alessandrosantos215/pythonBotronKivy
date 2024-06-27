import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):

    def build(self):
        # Criar um botão
        btn = Button(text='Clique-me!',
                     size_hint=(.5, .5),
                     pos_hint={'center_x': .5, 'center_y': .5})

        # Associar a função on_press ao evento de clique do botão
        btn.bind(on_press=self.on_button_click)

        return btn

    def on_button_click(self, instance):
        print('Botão clicado!')




if __name__ == '__main__':
    MyApp().run()
