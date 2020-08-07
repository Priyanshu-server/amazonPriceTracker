code_helper = """
ScreenManager:
    WelcomeScreen:
    AndroidInfo:
    AssistantWelcome:
    UsernameScreen:
    UsernameHelper:
    dobscreen:
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
    MDProgressBar:
        value: 15
        id: progress
        pos_hint: {'center_y':0.02}
        type: "indeterminate"
    MDFloatingActionButton:
        id : welcome_skip
        icon: "arrow-right"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.25}
        on_press: app.tap_target_stop()
        user_font_size: "50sp"
        on_release :
            root.manager.current = 'androidinfo'
            root.manager.transition.direction = 'left'

<AndroidInfo>:
    name: 'androidinfo'
    MDIconButton:
        id : android_info
        icon: "android"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: app.android_info_targerview_stop()
        user_font_size: "80sp"
        on_release :
            root.manager.current = 'assistantwelcome'
            root.manager.transition.direction = 'left'
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.1}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "35sp"
        on_release :
            root.manager.current = 'firstwelcome'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id : username_enter 
        icon: "arrow-right"
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'


<AssistantWelcome>:
    name: 'assistantwelcome'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDBackdrop:
        header: ''
        radius: 35
        id: backdrop
        title:'Hello!! I am your assistant'
        left_action_items: [['menu-open',lambda x: self.open()]]
        right_action_items: [['android',lambda x: self.open()]]
        # background_color: [0,1,0,0.7]
        specific_text_color: app.theme_cls.primary_color

        MDBackdropBackLayer:
            
            FloatLayout:
                orientation: 'vertical'
                MDLabel:
                    text:'android'
                    halign:'center'
                    font_style: 'H2'
                MDIconButton:
                    icon: 'android'
                    pos_hint: {'center_x':0.5,'center_y':0.65}
                    user_font_size: "120sp"

        MDBackdropFrontLayer:
            
            
            BoxLayout:
                orientation:'vertical'
                FloatLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x':0.94,'center_y':0.15}
                        user_font_size: "47sp"
                        on_release:
                            root.manager.current = 'usernamescreen'
                            root.manager.transition.direction = 'right'
            FloatLayout:
                orientation:'vertical'
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "350dp", "180dp"
                    pos_hint: {"center_x": .01, "center_y": .6}

                    MDLabel:
                        text: "Info"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        font_style: 'H5'
                        height: self.texture_size[1]

                    MDSeparator:
                        height: "1dp"

                    MDLabel:
                        text: "I am your assistant you can use me anytime by clicking on me, if you want to see me then click on the left-top menu bar"
                    MDSeparator:
                        height: "1dp"

                    MDRectangleFlatButton:
                        pos_hint:{'center_x':0.45}
                        text:'more'
                        on_release : Snackbar(text="Hi!! How are you doing??").show()
<UsernameScreen>:
    name: 'usernamescreen'
    MDLabel:
        text: 'User Info'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H4'
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.1}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "35sp"
        on_release :
            root.manager.current = 'firstwelcome'
            root.manager.transition.direction = 'right'

            

    MDIconButton:
        id : username_enter
        icon: "android"
        pos_hint: {'center_x':0.48,'center_y':0.069}
        # md_bg_color: app.theme_cls.primary_color
        user_font_size: "115sp"
        on_release :
            root.manager.current = 'usernamehelper'
            root.manager.transition.direction = 'right'
    
    MDTextField:
        hint_text: "Enter Username"
        color_mode: 'custom'
        line_color_normal: app.theme_cls.primary_color
        line_color_focus: 0,0.5,0,1
        helper_text: "Required"
        helper_text_mode: "on_error"
        # mode: "rectangle"
        icon_right: 'account'
        icon_right_color: 0,0.5,0,0.9
        pos_hint: {'center_x':0.5,'center_y':0.7}
        required: True
        size_hint: (0.8,0.1)


    MDChip:
        label: 'Help'
        color: 0,0.5,0,0.7
        icon: 'help'
        pos_hint: {'center_x':0.14,'center_y':0.4}
        callback: app.help_chip
    
    MDFloatingActionButton:
        id : username_enter 
        icon: "arrow-right"
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'dobinput'
    
    
    MDProgressBar:
        value: 45
        pos_hint: {'center_y':0.02}



<UsernameHelper>:
    name: 'usernamehelper'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDBackdrop:
        header: ''
        radius: 30
        id: backdrop
        title:'Hello!! I am your assistant'
        left_action_items: [['menu-open',lambda x: self.open()]]
        right_action_items: [['android',lambda x: self.open()]]
        # background_color: [0,1,0,0.7]
        specific_text_color: app.theme_cls.primary_color

        MDBackdropBackLayer:
            FloatLayout:
                orientation: 'vertical'
                MDLabel:
                    text:'android'
                    halign:'center'
                    font_style: 'H2'
                MDIconButton:
                    icon: 'android'
                    pos_hint: {'center_x':0.5,'center_y':0.65}
                    user_font_size: "120sp"

        MDBackdropFrontLayer:
            BoxLayout:
                orientation:'vertical'
                FloatLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x':0.94,'center_y':0.15}
                        user_font_size: "47sp"
                        on_release :
                            root.manager.current = 'usernamescreen'
                            root.manager.transition.direction = 'right'
                        
            FloatLayout:
                orientation:'vertical'
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "300dp", "150dp"
                    pos_hint: {"center_x": .05, "center_y": .6}

                    MDLabel:
                        text: "Username"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        font_style: 'H5'
                        height: self.texture_size[1]

                    MDSeparator:
                        height: "1dp"

                    MDLabel:
                        text: "Username is must so we can intract with you"
                    MDSeparator:
                        height: "1dp"

                    MDRectangleFlatButton:
                        pos_hint:{'center_x':0.45}
                        text:'more'
                        on_release : Snackbar(text="You can change your username later").show()


<dobscreen>:
    name:'dobinput'
    MDLabel:
        text: 'Hello World'
    
    MDRectangleFlatButton:
        id : dob
        text: 'Date Of Birth'   
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: "40sp"
        on_release : app.show_date_picker()
    
    MDIconButton:
        id : username_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.1}
        user_font_size: "40sp"
        on_release:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'
    
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
            root.manager.current = 'dobinput'
            root.manager.transition.direction = 'right'

    

"""