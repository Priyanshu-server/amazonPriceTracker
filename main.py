from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDFlatButton,MDIconButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from helper import code_helper
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.snackbar import Snackbar

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.taptargetview import MDTapTargetView

import requests
from bs4 import BeautifulSoup

Window.size = (400,600)


class WelcomeScreen(Screen):
    pass


class AndroidInfo(Screen):
    pass


class UsernameScreen(Screen):
    pass

class UsernameHelper(Screen):
    pass


class dobscreen(Screen):
    pass

class DobHelper(Screen):
    pass

class AssistantWelcome(Screen):
    pass

class FinalWelcome(Screen):
    pass
class Main(Screen):
    pass

class Result(Screen):
    pass
class Setting(Screen):
    pass
class About(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'firstwelcome'))
sm.add_widget(AndroidInfo(name = 'androidinfo'))
sm.add_widget(AssistantWelcome(name = 'assistantwelcome'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(UsernameHelper(name = 'usernamehelper'))
sm.add_widget(dobscreen(name = 'dobentered'))
sm.add_widget(DobHelper(name = 'dobhelper'))
sm.add_widget(FinalWelcome(name = 'finalwelcome'))
sm.add_widget(Main(name = 'main'))
sm.add_widget(Result(name = "result"))
sm.add_widget(Setting(name = "setting"))
sm.add_widget(Setting(name = "about"))
class AmazonApp(MDApp):
    
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
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
    
    
    def theme_switcher(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
    
    
    
    def tap_target_stop(self):
        self.skip_target_view.stop()


    def android_info_targerview_stop(self):
        self.android_target_view.stop()

    

    def help_chip(self, instance, value):
        help_cancel_btn_first = MDIconButton(icon = 'checkbox-marked-circle-outline',on_release = self.help_close_dialog_btn)
        self.help_dialog = MDDialog(title = 'Help',
                               text = 'Little android is your assistant\nClick the android for more Info',
                               size_hint = (0.7,0.1),buttons = [help_cancel_btn_first])
        self.help_dialog.open()

    def help_close_dialog_btn(self,obj):
        self.help_dialog.dismiss()


    def username_checker(self):
        username_check_false = True
        self.username_text_data = self.helper_string.get_screen('usernamescreen').ids.username_text.text
        # print(self.username_text_data)
        try:
            int(self.username_text_data)
        except:
            
            username_check_false = False
        if username_check_false or self.username_text_data.split()==[]:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.username_dialoge = MDDialog(title = 'Invalid Username',text = 'Please Enter a valid Username',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.username_dialoge.open()
        else:
            screen_usernamescreen = self.helper_string.get_screen('usernamescreen')
            screen_usernamescreen.ids.username_enter.disabled = False
            screen_usernamescreen.ids.username_check_extra_button.icon = 'account-check-outline'
            screen_usernamescreen.ids.username_check_btn.text_color = [1,1,1,0]
            screen_usernamescreen.ids.username_check_btn.md_bg_color =[1,1,1,0]
            screen_usernamescreen.ids.username_check_extra_button.text_color = self.theme_cls.primary_color
            screen_usernamescreen.ids.username_check_extra_button.pos_hint = {'center_x':0.5,'center_y':0.62}
            screen_usernamescreen.ids.username_check_extra_button.user_font_size = '60sp'



    def close_username_dialog(self,obj):
        self.username_dialoge.dismiss()


    
# DOB Picker
#self.dob for Date of birth



    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=1999,
            month=1,
            day=1,
        )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        dob_input_screen_selector = self.helper_string.get_screen('dobinput')
        #here i put the next button disbaled as False so user can enter in that window
        dob_input_screen_selector.ids.dob_enter.disabled = False
        dob_input_screen_selector.ids.account_shield.icon = 'shield-account'
        dob_input_screen_selector.ids.dob.text = str(self.dob)
        dob_input_screen_selector.ids.secure.text_color = [0,1,0,0.7]
        self.store.put('userInfo',name=self.username_text_data,dob = str(self.dob))
        self.username_changer()

    
    def navigation_draw(self):
        self.helper_string.get_screen('about').manager.current = "about"
    
    def username_changer(self):
        self.helper_string.get_screen('main').ids.title.title = self.store.get('userInfo')['name']
    

    def price(self):
        link = self.helper_string.get_screen('main').ids.Link.text
        if link.split() != []:
            self.price_finder(URL=link)
        else:
            
            self.helper_string.get_screen('main').manager.current = "main"
    


    def price_finder(self,URL):
        try:
            r = requests.get(URL,headers={"User-Agent":"Defined"})
            soup = BeautifulSoup(r.content,"html.parser")
            try:
                if 'amazon' in URL:
                    try:
                        price_one = soup.find(id="priceblock_dealprice")
                        price = price_one
                    except:
                        print("in ourprice")
                        price_two = soup.find(id = "priceblock_ourprice")
                        price = price_two
                elif 'flipkart' in URL:
                    try:
                        price = soup.find(class_ = '_1vC4OE _3qQ9m1')
                    except:
                        self.helper_string.get_screen('main').manager.current = "main"
            except:
                self.helper_string.get_screen('main').manager.current = "main"

            if price == None:
                self.helper_string.get_screen('main').manager.current = "main"
            else:
                current_price = price.get_text()
                self.helper_string.get_screen('result').ids.realPrice.text = current_price
                


        except:
            self.helper_string.get_screen('main').manager.current = "main"
        
    def setting_username_checker(self):
        username_check_false = True
        self.new_username = self.helper_string.get_screen('setting').ids.new_username.text
        try:
            int(self.new_username)
        except:
            
            username_check_false = False
        if username_check_false or self.new_username.split()==[]:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.username_dialoge = MDDialog(title = 'Invalid Username',text = 'Please Enter a valid Username',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.username_dialoge.open()
        else:
            self.username_text_data = self.new_username
            self.store.put('userInfo',name=self.username_text_data)
            self.username_changer()
            self.helper_string.get_screen('main').manager.current = "main"


    def change_edit_username(self):
        self.helper_string.get_screen('setting').ids.new_username.text = self.store.get('userInfo')['name']
    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('userInfo')['name'] != "":
                self.username_changer()
                self.helper_string.get_screen('main').manager.current = "main"
        except KeyError:
            self.helper_string.get_screen('firstwelcome').manager.current = 'firstwelcome'
AmazonApp().run()