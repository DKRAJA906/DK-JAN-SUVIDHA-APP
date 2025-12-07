from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import webbrowser
import time

# बैकग्राउंड कलर (डार्क ग्रे)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

# --- ग्लोबल वेरिएबल (लॉगिन नंबर स्टोर करने के लिए) ---
current_user_mobile = ""

# --- स्क्रीन 1: लॉगिन पेज (Login Page) ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        layout.add_widget(Label(size_hint_y=0.2))
        
        title = Label(
            text="DK JAN SUVIDHA KENDRA",
            font_size=60,
            bold=True,
            color=(1, 0.8, 0, 1),
            size_hint_y=None, height=100
        )
        layout.add_widget(title)
        
        sub_title = Label(
            text="Login to Continue",
            font_size=40,
            color=(1, 1, 1, 1),
            size_hint_y=None, height=60
        )
        layout.add_widget(sub_title)

        self.mobile_input = TextInput(
            hint_text="Enter Mobile Number",
            multiline=False,
            input_filter='int',
            font_size=40,
            size_hint_y=None, height=100,
            padding_y=[25, 0],
            halign='center'
        )
        layout.add_widget(self.mobile_input)

        self.error_label = Label(
            text="",
            color=(1, 0, 0, 1),
            font_size=30,
            size_hint_y=None, height=50
        )
        layout.add_widget(self.error_label)

        login_btn = Button(
            text="LOGIN",
            font_size=40,
            bold=True,
            background_color=(0, 0.6, 0, 1),
            size_hint_y=None, height=120
        )
        login_btn.bind(on_press=self.check_login)
        layout.add_widget(login_btn)
        
        layout.add_widget(Label(size_hint_y=0.3))
        
        self.add_widget(layout)

    def check_login(self, instance):
        global current_user_mobile
        mobile = self.mobile_input.text
        
        if len(mobile) == 10:
            self.error_label.text = ""
            current_user_mobile = mobile  # नंबर सेव करें
            
            # मेन स्क्रीन को अपडेट करें
            main_screen = self.manager.get_screen('main')
            main_screen.update_footer_info()
            
            self.manager.current = 'main'
            self.manager.transition.direction = 'left'
        else:
            self.error_label.text = "Please enter a valid 10-digit number!"

# --- स्क्रीन 2: मेन ऐप (Main Service Page) ---
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        root = BoxLayout(orientation='vertical')
        
        # --- HEADER ---
        header_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.16), padding=[5,5,5,5])
        
        with header_layout.canvas.before:
            Color(0, 0, 0.6, 1)
            self.header_rect = Rectangle(pos=header_layout.pos, size=header_layout.size)
        header_layout.bind(pos=self.update_header_rect, size=self.update_header_rect)

        # 1. Time
        self.time_label = Label(
            text="", font_size=35, bold=True, color=(1, 1, 1, 1),
            size_hint=(1, 0.25), halign='right', valign='middle',
            text_size=(Window.width - 20, None)
        )
        Clock.schedule_interval(self.update_time, 1)
        header_layout.add_widget(self.time_label)

        # 2. Name
        name_label = Label(
            text="DK JAN SUVIDHA KENDRA", font_size=80, bold=True, 
            color=(1, 0.8, 0, 1), size_hint=(1, 0.50)
        )
        header_layout.add_widget(name_label)
        
        # 3. Address
        address_label = Label(
            text="ADDRESS: RANI KHEDA CHUARAHA", font_size=45, 
            color=(1, 1, 1, 1), size_hint=(1, 0.25)
        )
        header_layout.add_widget(address_label)
        
        root.add_widget(header_layout)
        
        # --- SERVICES ---
        scroll = ScrollView(size_hint=(1, 0.76)) # थोड़ा स्पेस कम किया ताकि फुटर बड़ा हो सके
        layout = GridLayout(cols=1, spacing=15, size_hint_y=None, padding=20)
        layout.bind(minimum_height=layout.setter('height'))
        
        services = {
            "Aadhaar Card Services": "https://uidai.gov.in",
            "PAN Card Apply": "https://www.onlineservices.nsdl.com",
            "Ration Card": "https://fcs.up.gov.in/",
            "PM Kisan Samman Nidhi": "https://pmkisan.gov.in",
            "Photo Resize":"https://www.reduceimages.com/" ,
            "Pdf Master":"https://www.ilovepdf.com/pdf_to_jpg",
            "E-Shram Card": "https://eshram.gov.in",
            "Ayushman Bharat Card": "https://pmjay.gov.in",
            "Voter card": "https://voters.eci.gov.in",
            "Khatuani ki nakal": "https://upbhulekh.gov.in",
            "Money Transfer": "https://www.npci.org.in",
            "Electricity Bill": "https://www.uppcl.org",
            "Rail/Flight Ticket": "https://www.irctc.co.in",
            "E district": "https://edistrict.up.gov.in",
            "Scholarship Form": "https://scholarship.up.gov.in",
            "Udyam Aadhar (MSME)": "https://udyamregistration.gov.in",
            "Farmer Rajistry": "https://upfr.agristack.gov.in/farmer-registry-up/#/",
            "Driving License": "https://parivahan.gov.in",
            "Old Age Pension": "https://sspy-up.gov.in",
            "Passport Seva": "https://www.passportindia.gov.in",
            "Sarkari Result": "https://www.sarkariresult.com",
            "DigiLocker": "https://www.digilocker.gov.in",
            "CCC / O Level Form": "https://student.nielit.gov.in",
            "Jeevan Pramaan": "https://jeevanpramaan.gov.in"
        }
        
        for name, link in services.items():
            btn = Button(
                text=name, size_hint_y=None, height=130, font_size=60,
                italic=True, bold=True, background_color=(0, 0.6, 0.6, 1)
            )
            btn.bind(on_press=lambda x, l=link: webbrowser.open(l) if l != "None" else None)
            layout.add_widget(btn)
            
        scroll.add_widget(layout)
        root.add_widget(scroll)
        
        # --- UPDATED FOOTER ---
        footer_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), padding=5, spacing=10)
        
        # फुटर का बैकग्राउंड (हरा)
        with footer_layout.canvas.before:
            Color(0, 0.5, 0, 1)
            self.footer_rect = Rectangle(pos=footer_layout.pos, size=footer_layout.size)
        footer_layout.bind(pos=self.update_footer_bg, size=self.update_footer_bg)

        # 1. Contact Number (Left Side) - 40% जगह लेगा
        self.contact_label = Label(
            text="Contact: 8318736819",
            font_size=28, bold=True, color=(1, 1, 1, 1),
            halign='left', valign='middle', size_hint_x=0.4
        )
        self.contact_label.bind(size=self.align_text_left)
        footer_layout.add_widget(self.contact_label)

        # 2. User Mobile (Right Side Text) - 35% जगह लेगा
        self.user_info_label = Label(
            text="Login: ...",
            font_size=28, bold=True, color=(1, 1, 0, 1), # पीला रंग ताकि अलग दिखे
            halign='right', valign='middle', size_hint_x=0.35
        )
        self.user_info_label.bind(size=self.align_text_right)
        footer_layout.add_widget(self.user_info_label)

        # 3. LOGOUT BUTTON (Red) - 25% जगह लेगा
        logout_btn = Button(
            text="LOGOUT",
            font_size=25, 
            bold=True,
            background_color=(1, 0, 0, 1), # लाल रंग
            color=(1, 1, 1, 1),
            size_hint_x=0.15
        )
        logout_btn.bind(on_press=self.logout)
        footer_layout.add_widget(logout_btn)
        
        root.add_widget(footer_layout)
        
        self.add_widget(root)

    def update_header_rect(self, instance, value):
        self.header_rect.pos = instance.pos
        self.header_rect.size = instance.size
        self.time_label.text_size = (instance.width - 20, None)

    def update_footer_bg(self, instance, value):
        self.footer_rect.pos = instance.pos
        self.footer_rect.size = instance.size

    def align_text_left(self, instance, value):
        instance.text_size = (instance.width, instance.height)

    def align_text_right(self, instance, value):
        instance.text_size = (instance.width, instance.height)

    def update_time(self, *args):
        current_time = time.strftime("%d-%b-%Y  %I:%M %p") 
        self.time_label.text = current_time
    
    def update_footer_info(self):
        global current_user_mobile
        self.user_info_label.text = f"Login: {current_user_mobile}"

    def logout(self, instance):
        global current_user_mobile
        current_user_mobile = "" # नंबर हटाएं
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

# --- Main App Class ---
class DKApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    DKApp().run()