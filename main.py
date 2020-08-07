from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from helper import code_helper

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.taptargetview import MDTapTargetView

Window.size = (400,600)


class WelcomeScreen(Screen):
    pass


class AndroidInfo(Screen):
    pass


class UsernameScreen(Screen):
    pass

class dobscreen(Screen):
    pass

class UserEnter(Screen):
    pass

class AssistantWelcome(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'firstwelcome'))
sm.add_widget(AndroidInfo(name = 'androidinfo'))
sm.add_widget(AssistantWelcome(name = 'assistantwelcome'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(dobscreen(name = 'dobentered'))
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
        self.android_target_view = MDTapTargetView(
                                                widget=self.helper_string.get_screen('androidinfo').ids.android_info,
                                                title_text="Hey!!",widget_position="center",title_text_size="20sp",title_position="right_top",
                                                description_text="I am your assistant\nClick on me",outer_radius='180dp',description_text_color=[0,0,0,1]
                                                ,outer_circle_alpha = 0.5,target_radius='50dp')
        self.skip_target_view.start()
        self.android_target_view.start()

        #self.dob initialize
        self.dob_entered= True
        return screen
    
    def tap_target_stop(self):
        self.skip_target_view.stop()


    def android_info_targerview_stop(self):
        self.android_target_view.stop()

    

    def help_chip(self, instance, value):
        help_cancel_btn_first = MDIconButton(icon = 'checkbox-marked-circle-outline',on_release = self.help_close_dialog_btn)
        self.dialog = MDDialog(title = 'Help',
                               text = 'Little android is your assistant\nClick the android for more Info',
                               size_hint = (0.7,0.1),buttons = [help_cancel_btn_first])
        self.dialog.open()

    def help_close_dialog_btn(self,obj):
        self.dialog.dismiss()
    
    
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

        #here i put the next button disbaled as False so user can enter in that window
        
        self.helper_string.get_screen('dobinput').ids.username_enter.disabled = False
AmazonApp().run()