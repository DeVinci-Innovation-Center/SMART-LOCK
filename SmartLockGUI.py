from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

import os

os.environ["KIVY_WINDOW"] = "egl_rpi"
os.environ["KIVY_GL_BACKEND"] = "gl"

screen_helper="""

ScreenManager:
    HomeScreen:
    PinCodeScreen:
    LockerOpenScreen:

<HomeScreen>:
    name: 'home'
    
    Image:
        source: 'dvic_logo.png'
        size_hint: (0.4,0.4)
        pos_hint: {"center_x":0.75,"center_y":0.9}
        
    MDFillRoundFlatButton:
        text:'CODE PIN'
        font_size:36
        pos_hint:{"center_x":0.5,"center_y":0.1}
        on_press: root.manager.current='code PIN'
        
    MDLabel:
        text:'PASSEZ VOTRE CARTE SUR LE LECTEUR OU ENTREZ LE CODE PIN'
        halign:'center'
        font_style:'H3'
        padding: (10,10)
        pos_hint:{"center_x":0.5,"center_y":0.5}

<PinCodeScreen>:
    name: 'code PIN'
    
    MDLabel:
        id: stars
        text:''
        halign:'center'
        font_style:'H3'
        font_size:65
        pos_hint:{"center_x":0.5,"center_y":0.73}
    
    MDFillRoundFlatButton:
        text:'   1   '
        font_size:70
        pos_hint:{"center_x":0.2,"center_y":0.55}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '1'
        on_press: root.addStar()
    
    MDFillRoundFlatButton:
        text:'   2   '
        font_size:70
        pos_hint:{"center_x":0.5,"center_y":0.55}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '2'
        on_press: root.addStar()

    MDFillRoundFlatButton:
        text:'   3   '
        font_size:70
        pos_hint:{"center_x":0.8,"center_y":0.55}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '3'
        on_press: root.addStar()
    
    MDFillRoundFlatButton:
        text:'   4   '
        font_size:70
        pos_hint:{"center_x":0.2,"center_y":0.42}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '4'
        on_press: root.addStar()
        
    MDFillRoundFlatButton:
        text:'   5   '
        font_size:70
        pos_hint:{"center_x":0.5,"center_y":0.42}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '5'
        on_press: root.addStar()
        
    MDFillRoundFlatButton:
        text:'   6   '
        font_size:70
        pos_hint:{"center_x":0.8,"center_y":0.42}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '6'
        on_press: root.addStar()
    
    MDFillRoundFlatButton:
        text:'   7   '
        font_size:70
        pos_hint:{"center_x":0.2,"center_y":0.29}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '7'
        on_press: root.addStar()
        
    MDFillRoundFlatButton:
        text:'   8   '
        font_size:70
        pos_hint:{"center_x":0.5,"center_y":0.29}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '8'
        on_press: root.addStar()
    
    MDFillRoundFlatButton:
        text:'   9   '
        font_size:70
        pos_hint:{"center_x":0.8,"center_y":0.29}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '9'
        on_press: root.addStar()  
    
    MDFillRoundFlatButton:
        text:'        '
        font_size:70
        pos_hint:{"center_x":0.2,"center_y":0.16}
        md_bg_color: 0.89, 0.22, 0.21, 1
        on_press: root.code = ''
        on_press: root.resetStars()
        
    MDFillRoundFlatButton:
        text:'   0   '
        font_size:70
        pos_hint:{"center_x":0.5,"center_y":0.16}
        md_bg_color: 0.3, 0.3, 0.3 ,1
        on_press: root.code += '0'
        on_press: root.addStar()
    
    MDFillRoundFlatButton:
        text:'        '
        font_size:70
        pos_hint:{"center_x":0.8,"center_y":0.16}
        md_bg_color: 0.26, 0.63, 0.28, 1
        on_press: root.verifyCode(root.code)
        on_release: root.code = ''
    
    MDIconButton:
        icon: 'chevron-left'
        user_font_size: "110sp"
        pos_hint: {"center_x":0.12,"center_y":0.9}
        on_press : root.manager.current='home'
        
<LockerOpenScreen>:
    name: 'open'
    MDFloatLayout:

        md_bg_color: 0.26, 0.63, 0.28, 1
        
        MDLabel:
            text:'CASIER OUVERT'
            halign:'center'
            font_style:'Button'
            font_size:60
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            padding: (10,10)
            pos_hint:{"center_x":0.5,"center_y":0.57}
        
        MDIconButton:
            icon: 'shield-check'
            user_font_size: "150sp"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            pos_hint: {"center_x":0.5,"center_y":0.43}
        
"""

def change_screen(self,screen_name):
    self.manager.current = screen_name

class HomeScreen(Screen):
    pass

class PinCodeScreen(Screen):
    
    code = ''
        
    def addStar(self):
        if self.ids.stars.text == 'CODE INCORRECT':
            self.ids.stars.text = '*'
        elif len(self.ids.stars.text) < 20:
            self.ids.stars.text += '*'
            
    def resetStars(self):
        self.ids.stars.text = ''
        
    def verifyCode(self,code):
        self.ids.stars.text = ''
        if code == '123456':
            change_screen(self,'open')
        elif code != '':
            self.ids.stars.text = 'CODE INCORRECT'

    def on_leave(self, *args):
        self.ids.stars.text = ''
        self.manager.get_screen('code PIN').code = ''

    pass

class LockerOpenScreen(Screen):

    def on_enter(self, *args):
        Clock.schedule_once(self.callbackfun, 5)

    def callbackfun(self, dt):
        self.manager.current = 'code PIN'
    
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(PinCodeScreen(name='code PIN'))
sm.add_widget(LockerOpenScreen(name='open'))

class MainApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

Window.size = (600, 1024)

MainApp().run()
