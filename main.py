# -*- coding: utf-8 -*-
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder # Write the interfacer code with KV

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'My App'
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x]]
        TelaLogin:

<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color
        
        MDLabel:
            text: 'Mudar senha'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
        MDIconButton:
            icon: 'close'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1  
            on_release: root.fechar()
    
    MDFloatLayout:
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Código enviado por e-mail'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Nova senha:'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar nova senha:'
        MDRaisedButton:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            text: 'Recadastrar senha!'
        
<TelaLogin>:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'piggy-bank'
        user_font_size: '75sp'
    MDTextField:
        size_hint_x: .9
        hint_text: 'Email:'
        pos_hint: {'center_x': .5, 'center_y': .6}
    MDTextField:
        size_hint_x: .9
        hint_text: 'Senha:'
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDRaisedButton:
        size_hint_x: .9
        pos_hint: {'center_x': .5, 'center_y': .4}
        text: 'Login'
    MDLabel:
        text: 'Esqueceu sua senha?'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .3}
    MDTextButton:
        text: 'Clique aqui!'
        pos_hint: {'center_x': .5, 'center_y': .25}
        on_release: root.abrir_card()
'''

class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '700'
        return Builder.load_string(KV)

MyApp().run()
