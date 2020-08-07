code_helper = """
ScreenManager:
    WelcomeScreen:
    AndroidInfo:
    AssistantWelcome:
    UsernameScreen:
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
    MDLabel:
        text: 'User Info'
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
            root.manager.current = 'androidinfo'
            root.manager.transition.direction = 'right'

            

    MDIconButton:
        id : username_enter
        icon: "android"
        pos_hint: {'center_x':0.48,'center_y':0.069}
        # md_bg_color: app.theme_cls.primary_color
        user_font_size: "115sp"
        on_release :
            root.manager.current = 'firstwelcome'
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