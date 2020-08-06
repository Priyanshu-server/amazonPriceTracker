from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivymd.app import MDApp
# from helper import code_helper

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.taptargetview import MDTapTargetView

Window.size = (400,600)

code_helper = """
ScreenManager:
    WelcomeScreen:
    UsernameScreen:
    UserEnter:


<WelcomeScreen>:
    name: 'firstwelcome'
    MDLabel:
        text: 'Welcome'
        pos_hint: {'center_y':0.8}
        halign: 'center'
        font_style: 'H2'
    MDLabel:
        text: 'to'
        pos_hint: {'center_y':0.65}
        halign: 'center'
        font_style: 'H3'
    MDLabel:
        text: 'Amazon Price Tracker'
        pos_hint: {'center_y':0.5}
        halign: 'center'
        font_style: 'H4'
    MDFloatingActionButton:
        id : welcome_skip
        icon: "arrow-right"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.25}
        on_press: app.tap_target_stop()
        user_font_size: "50sp"
        on_release :
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'

<UsernameScreen>:
    name: 'usernamescreen'
    MDLabel:
        text: 'User Info'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H4'
    MDIconButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.12,'center_y':0.1}
        user_font_size: "40sp"
        on_release :
            root.manager.current = 'firstwelcome'
            root.manager.transition.direction = 'right'
    MDTextField:
        hint_text: "Enter Username"
        helper_text: "Required"
        helper_text_mode: "on_error"
        #mode: "rectangle"
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.7}
        required: True
        size_hint: (0.8,0.1)
    
    MDRectangleFlatButton:
        id : dob
        text: 'Date Of Birth'   
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: "40sp"
        on_release : app.show_date_picker()
    MDIconButton:
        disabled: True
        id : username_enter 
        icon: "arrow-right"
        pos_hint: {'center_x':0.85,'center_y':0.1}
        user_font_size: "40sp"
        on_release:
            root.manager.current = 'userenter'

<UserEnter>:
    name: 'userenter'
    MDLabel:
        text: 'Hello World'
    MDIconButton:
        id : username_enter
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.1}
        user_font_size: "40sp"
        on_release:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    

"""
class WelcomeScreen(Screen):
    pass


class UsernameScreen(Screen):
    pass
class UserEnter(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'firstwelcome'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(UserEnter(name = 'userenter'))

class AmazonApp(MDApp):
    
    def build(self):
        screen = Screen()
        self.helper_string = Builder.load_string(code_helper)
        screen.add_widget(self.helper_string)
        self.skip_target_view = MDTapTargetView(
                                                widget=self.helper_string.get_screen('firstwelcome').ids.welcome_skip,
                                                title_text="Next",widget_position="left_bottom",title_text_size="20sp",
                                                description_text="GO next",outer_radius='80dp',description_text_color=[1, 0, 0, 0]
                                                ,outer_circle_alpha = 0.40,target_radius='40dp')
        self.skip_target_view.start()

        #self.dob initialize
        self.dob_entered= True
        return screen
    
    def tap_target_stop(self):
        self.skip_target_view.stop()
    
    
# DOB Picker
#self.dob for Date of birth

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2010,
            month=2,
            day=12,
        )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        self.helper_string.get_screen('usernamescreen').ids.username_enter.disabled = False
        print(self.dob)

AmazonApp().run()