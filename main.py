from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.selectioncontrol import MDSwitch
import webbrowser
import time
from datetime import date
import calendar
from kivy.uix.widget import Widget
from kivy.factory import Factory

# --- GLOBAL WINDOW SETTINGS ---
Window.clearcolor = (0.1, 0.1, 0.1, 1)  # हल्का काला बैकग्राउंड
Window.softinput_mode = "below_target"

KV_TOOLS = '''
# ================= GLOBAL STYLES & WIDGETS =================
<CustomSeparator@Widget>:
    size_hint_y: None
    height: dp(1)
    canvas:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            pos: self.pos
            size: self.size

# ================= TOOLS MENU SCREEN =================
<ToolsMenuScreen>:
    name: 'tools_menu'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.1, 0.1, 0.1, 1  # Global dark background
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "DK TOOLS"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: 1, 0.8, 0, 1
            halign: "center"
            size_hint_y: 0.1

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: "15dp"
                size_hint_y: None
                height: self.minimum_height
                padding: "10dp"

                MDFillRoundFlatButton:
                    text: "AGE CALCULATOR"
                    font_size: "24sp"
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "80dp"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 0, 0.5, 1, 1
                    on_release: root.manager.current = 'age_calc'

                MDFillRoundFlatButton:
                    text: "CASH DENOMINATION"
                    font_size: "24sp"
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "80dp"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 0, 0.7, 0, 1
                    on_release: root.manager.current = 'cash_counter'
                
                MDFillRoundFlatButton:
                    text: "INTEREST CALCULATOR"
                    font_size: "24sp"
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "80dp"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 0.6, 0.2, 0.8, 1
                    on_release: root.manager.current = 'interest_calc'

                MDFillRoundFlatButton:
                    text: "FARM (UP) CALCULATOR"
                    font_size: "24sp"
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "80dp"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 0.8, 0.4, 0, 1
                    on_release: root.manager.current = 'farm_calc'

        MDFillRoundFlatButton:
            text: "BACK TO HOME"
            font_size: "20sp"
            size_hint_x: 0.6
            pos_hint: {"center_x": 0.5}
            md_bg_color: 1, 0, 0, 1
            on_release: root.manager.current = 'main'

# ================= SCREEN 1: AGE CALCULATOR =================
<AgeCalculatorScreen>:
    name: 'age_calc'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.9, 0.9, 0.9, 1
        
        MDTopAppBar:
            title: "DK AGE CALCULATOR"
            anchor_title: "center"
            elevation: 2
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            md_bg_color: 0.4, 0.2, 0.6, 1
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            size_hint_y: None
            height: dp(30)
            md_bg_color: 0.4, 0.2, 0.6, 1
            padding: [0, 0, 0, dp(5)]
            MDLabel:
                text: "BY DK JAN SUVIDHA KENDRA"
                halign: "center"
                valign: "top"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0.8
                font_style: "Caption"
                bold: True

        MDFloatLayout:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(30)
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                size_hint_y: None
                height: self.minimum_height
                padding: dp(20)

                MDLabel:
                    text: "ENTER YOUR DOB"
                    halign: "center"
                    theme_text_color: "Secondary"
                    font_style: "H6"

                MDTextField:
                    id: dob_input
                    hint_text: "DD/MM/YYYY"
                    helper_text: "Example: 01/01/2000"
                    helper_text_mode: "persistent"
                    pos_hint: {"center_x": 0.5}
                    size_hint_x: 0.9
                    max_text_length: 10
                    font_size: dp(26)
                    multiline: False
                    on_text: root.on_text_change(self, self.text)

                MDCard:
                    size_hint: 0.95, None
                    height: dp(100)
                    pos_hint: {"center_x": 0.5}
                    elevation: 3
                    opacity: 0
                    id: result_card
                    orientation: "vertical"
                    padding: dp(15)
                    radius: [15]
                    md_bg_color: 0.95, 0.95, 1, 1
                    
                    MDLabel:
                        id: result_label
                        text: ""
                        halign: "center"
                        font_style: "H5"
                        theme_text_color: "Custom"
                        text_color: 0, 0.4, 0, 1
                        bold: True
                        pos_hint: {"center_y": 0.5}

            MDFillRoundFlatButton:
                text: "CALCULATE AGE"
                font_size: dp(20)
                pos_hint: {"center_x": 0.5, "y": 0.3}
                size_hint_x: 0.9
                size_hint_y: None
                height: dp(60)
                on_release: root.calculate_age()
                elevation: 10

# ================= SCREEN 2: CASH COUNTER =================
<NoteRow@MDBoxLayout>:
    orientation: 'horizontal'
    size_hint_y: None
    height: "55dp"
    padding: "5dp"
    spacing: "5dp"
    
    MDCard:
        size_hint_x: 0.25
        md_bg_color: 0.9, 1, 0.9, 1
        radius: [4]
        MDLabel:
            text: root.note_text
            halign: "center"
            valign: "center"
            bold: True
            theme_text_color: "Custom"
            text_color: 0, 0.5, 0, 1
    MDLabel:
        text: "X"
        size_hint_x: 0.05
        halign: "center"
    MDTextField:
        id: count_input
        hint_text: "0"
        mode: "rectangle"
        line_color_normal: 0.6, 0.6, 0.6, 1
        input_filter: "int"
        size_hint_x: 0.3
        halign: "center"
        font_size: "18sp"
        on_text: app.get_running_app().root.get_screen('cash_counter').update_total()
    MDLabel:
        text: "="
        size_hint_x: 0.05
        halign: "center"
    MDCard:
        size_hint_x: 0.35
        md_bg_color: 1, 1, 1, 1
        radius: [4]
        line_color: 0.8, 0.8, 0.8, 1
        MDLabel:
            id: total_label
            text: "0"
            halign: "center"
            valign: "center"
            bold: True
            font_size: "18sp"

<CashCounterScreen>:
    name: 'cash_counter'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.98, 0.98, 0.98, 1

        MDTopAppBar:
            title: "DK CASH COUNTER"
            anchor_title: "center"
            elevation: 2
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            md_bg_color: 0.4, 0.2, 0.6, 1
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            size_hint_y: None
            height: "25dp"
            md_bg_color: 0.5, 0.3, 0.7, 1
            MDLabel:
                text: "BY DK JAN SUVIDHA KENDRA"
                halign: "center"
                valign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "Caption"
                bold: True

        ScrollView:
            MDBoxLayout:
                id: container
                orientation: 'vertical'
                padding: "10dp"
                spacing: "2dp"
                size_hint_y: None
                height: self.minimum_height

        MDCard:
            size_hint_y: None
            height: "80dp"
            md_bg_color: 0.9, 0.95, 1, 1
            line_color: 0.4, 0.2, 0.6, 1
            line_width: 1.5
            radius: [15, 15, 0, 0]
            elevation: 10
            padding: "20dp"
            MDBoxLayout:
                MDLabel:
                    text: "GRAND TOTAL:"
                    halign: "left"
                    valign: "center"
                    font_style: "H6"
                    bold: True
                MDLabel:
                    id: grand_total_label
                    text: "Rs. 0"
                    halign: "right"
                    valign: "center"
                    color: 0.4, 0.2, 0.6, 1
                    font_style: "H5"
                    bold: True

# ================= SCREEN 3: INTEREST CALCULATOR =================
<InterestCalculatorScreen>:
    name: 'interest_calc'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "DK INTEREST CALCULATOR"
            anchor_title: "center"
            elevation: 2
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            md_bg_color: 0, 0.5, 1, 1
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            size_hint_y: None
            height: "25dp"
            md_bg_color: 1, 0, 0, 1
            MDLabel:
                text: "BY DK JAN SUVIDHA KENDRA"
                halign: "center"
                valign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "Caption"
                bold: True

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "15dp"
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    size_hint_y: None
                    height: "55dp"
                    padding: "15dp"
                    radius: [8]
                    elevation: 2
                    md_bg_color: 0.95, 0.95, 0.95, 1
                    MDBoxLayout:
                        orientation: 'horizontal'
                        spacing: "10dp"
                        MDLabel:
                            text: "Bank Mode (Yearly Rate)?"
                            valign: "center"
                            bold: True
                            theme_text_color: "Primary"
                            size_hint_x: 0.7
                        MDBoxLayout:
                            size_hint_x: 0.3
                            MDSwitch:
                                id: mode_switch
                                active: False
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDTextField:
                    id: principal_field
                    hint_text: "Principal Amount"
                    input_filter: "float"
                    mode: "rectangle"
                    icon_right: "currency-inr"

                MDTextField:
                    id: rate_field
                    hint_text: "Interest Rate (%)"
                    input_filter: "float"
                    mode: "rectangle"
                    icon_right: "percent"

                MDTextField:
                    id: time_field
                    hint_text: "Time (Months)"
                    input_filter: "float"
                    mode: "rectangle"
                    icon_right: "calendar-clock"

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: "15dp"
                    size_hint_y: None
                    height: "50dp"
                    MDFillRoundFlatButton:
                        text: "SIMPLE INTEREST"
                        font_size: "13sp"
                        size_hint_x: 0.5
                        on_release: root.calculate_interest('simple')
                    MDFillRoundFlatButton:
                        text: "COMPOUND INTEREST"
                        font_size: "13sp"
                        size_hint_x: 0.5
                        md_bg_color: 0, 0.7, 0, 1
                        on_release: root.calculate_interest('compound')

                MDCard:
                    orientation: "vertical"
                    size_hint_y: None
                    height: "150dp"
                    padding: "15dp"
                    spacing: "8dp"
                    radius: [8]
                    elevation: 2
                    line_color: (0, 0.5, 1, 1)
                    md_bg_color: 0.92, 0.96, 1, 1
                    MDLabel:
                        text: "RESULT"
                        halign: "center"
                        font_style: "H6"
                        bold: True
                    MDBoxLayout:
                        orientation: "horizontal"
                        MDLabel:
                            text: "Total Interest:"
                            bold: True
                        MDLabel:
                            id: interest_label
                            text: "Rs. 0"
                            halign: "right"
                            bold: True
                            color: 0, 0.6, 0, 1
                    MDBoxLayout:
                        orientation: "horizontal"
                        MDLabel:
                            text: "Total Amount:"
                            bold: True
                        MDLabel:
                            id: total_amount_label
                            text: "Rs. 0"
                            halign: "right"
                            bold: True
                            color: 1, 0, 0, 1

# ================= SCREEN 4: FARM CALCULATOR =================
<FarmCalculatorScreen>:
    name: 'farm_calc'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.95, 0.95, 0.95, 1

        MDTopAppBar:
            title: "DK FARM CALCULATOR (UP)"
            anchor_title: "center"
            elevation: 2
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            
        MDBoxLayout:
            size_hint_y: None
            height: dp(30)
            md_bg_color: app.theme_cls.primary_color
            padding: [0, 0, 0, dp(5)]
            MDLabel:
                text: "BY DK JAN SUVIDHA KENDRA"
                halign: "center"
                valign: "top"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0.8
                font_style: "Caption"
                bold: True

        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: "Zameen (Hectare me) Dalein"
                halign: "center"
                theme_text_color: "Primary"
                font_style: "H6"
                size_hint_y: None
                height: dp(30)

            MDTextField:
                id: hectare_input
                hint_text: "0.2530"
                helper_text: "Khatauni wala area likhein"
                helper_text_mode: "persistent"
                input_filter: "float"
                mode: "rectangle"
                halign: "center"
                font_size: dp(24)
                size_hint_x: 0.9
                pos_hint: {"center_x": 0.5}
                on_text: root.calculate_land(self.text)

            MDCard:
                size_hint: 0.95, None
                height: dp(180)
                pos_hint: {"center_x": 0.5}
                elevation: 3
                padding: dp(20)
                orientation: 'vertical'
                spacing: dp(10)
                radius: [10]
                md_bg_color: 1, 1, 1, 1

                MDLabel:
                    text: "Kul Zameen (Approx)"
                    halign: "center"
                    theme_text_color: "Secondary"
                    font_style: "Caption"

                MDBoxLayout:
                    orientation: 'horizontal'
                    MDLabel:
                        id: bigha_label
                        text: "0"
                        halign: "center"
                        font_style: "H4"
                        theme_text_color: "Custom"
                        text_color: 0, 0.6, 0, 1
                        bold: True
                    MDLabel:
                        text: "Bigha"
                        halign: "left"
                        valign: "bottom"
                        font_style: "Subtitle1"

                MDBoxLayout:
                    orientation: 'horizontal'
                    MDLabel:
                        id: biswa_label
                        text: "0"
                        halign: "center"
                        font_style: "H5"
                        bold: True
                    MDLabel:
                        text: "Biswa"
                        halign: "left"
                        valign: "bottom"
                        font_style: "Subtitle1"

                MDBoxLayout:
                    orientation: 'horizontal'
                    MDLabel:
                        id: dhur_label
                        text: "0"
                        halign: "center"
                        font_style: "H6"
                    MDLabel:
                        text: "Dhur"
                        halign: "left"
                        valign: "bottom"
                        font_style: "Subtitle1"

        Widget:
            size_hint_y: 1 

        MDLabel:
            text: "*Note: 1 Hectare = 3.95 Bigha (Approx)"
            halign: "center"
            theme_text_color: "Secondary"
            font_style: "Caption"
            size_hint_y: None
            height: dp(30)
'''

class NoteRow(MDBoxLayout):
    note_text = StringProperty()
    value = NumericProperty()

class CustomSeparator(Widget):
    pass

class ToolsMenuScreen(Screen):
    pass

class AgeCalculatorScreen(Screen):
    def on_enter(self):
        self.ids.dob_input.text = ""
        self.ids.result_label.text = ""
        self.ids.result_card.opacity = 0
        # last_length को रीसेट करें और लूप से बचने के लिए फ्लैग सेट करें
        self.last_length = 0
        self._updating = False

    def go_back(self):
        self.manager.current = 'tools_menu'
        self.manager.transition.direction = 'right'

    def on_text_change(self, instance, new_text):
        # अगर टेक्स्ट अपडेट हो रहा है तो इस फंक्शन को दोबारा न चलाएं
        if getattr(self, '_updating', False):
            return

        last_length = getattr(self, 'last_length', 0)
        
        # केवल तभी फॉर्मेट करें जब यूजर टाइप कर रहा हो (बैकस्पेस नहीं)
        if len(new_text) > last_length:
            clean = new_text.replace('/', '')
            
            if len(clean) > 8:
                clean = clean[:8]
            
            formatted = ''
            if len(clean) > 4:
                formatted = f"{clean[:2]}/{clean[2:4]}/{clean[4:]}"
            elif len(clean) > 2:
                formatted = f"{clean[:2]}/{clean[2:]}"
            else:
                formatted = clean
            
            if formatted != new_text:
                # अपडेट करने से पहले फ्लैग को True सेट करें
                self._updating = True
                instance.text = formatted
                # कर्सर को टेक्स्ट के अंत में ले जाएं
                Clock.schedule_once(lambda dt: setattr(instance, 'cursor', (len(instance.text), 0)))
                # अपडेट के बाद फ्लैग को False पर रीसेट करें
                self._updating = False
        
        self.last_length = len(instance.text)

    def calculate_age(self):
        try:
            d, m, y = map(int, self.ids.dob_input.text.split('/'))
            birth_date = date(y, m, d)
            today = date.today()
            
            age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            if today.month >= birth_date.month:
                months = today.month - birth_date.month
            else:
                months = 12 + today.month - birth_date.month
            
            if today.day >= birth_date.day:
                days = today.day - birth_date.day
            else:
                last_month = today.month - 1 if today.month > 1 else 12
                last_year = today.year if last_month != 12 else today.year - 1
                days_in_last_month = calendar.monthrange(last_year, last_month)[1]
                days = days_in_last_month - birth_date.day + today.day
                if months == 0:
                    months = 11
                    age_years -= 1
                else:
                    months -= 1

            self.ids.result_label.text = f"{age_years} Years, {months} Months, {days} Days"
            self.ids.result_card.opacity = 1
        except:
            self.ids.result_label.text = "Invalid Date!"
            self.ids.result_card.opacity = 1

class CashCounterScreen(Screen):
    def on_enter(self):
        self.ids.container.clear_widgets()
        self.notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        self.row_widgets = []
        for note in self.notes:
            row = NoteRow(note_text=f"Rs. {note}", value=note)
            self.row_widgets.append(row)
            self.ids.container.add_widget(row)
            self.ids.container.add_widget(Factory.CustomSeparator())

    def go_back(self):
        self.manager.current = 'tools_menu'
        self.manager.transition.direction = 'right'

    def update_total(self):
        grand = 0
        for row in self.row_widgets:
            try:
                count = int(row.ids.count_input.text)
                sub = count * row.value
                row.ids.total_label.text = str(sub)
                grand += sub
            except: pass
        self.ids.grand_total_label.text = f"Rs. {grand}"

class InterestCalculatorScreen(Screen):
    def go_back(self):
        self.manager.current = 'tools_menu'
        self.manager.transition.direction = 'right'

    def calculate_interest(self, type):
        try:
            p = float(self.ids.principal_field.text)
            r = float(self.ids.rate_field.text)
            t = float(self.ids.time_field.text)
            
            is_bank_mode = self.ids.mode_switch.active
            effective_rate = r / 12 if is_bank_mode else r
            
            interest = 0
            if type == 'simple':
                interest = (p * effective_rate * t) / 100
            elif type == 'compound':
                amount = p * (pow((1 + effective_rate / 100), t))
                interest = amount - p
            
            total = p + interest
            self.ids.interest_label.text = f"Rs. {interest:,.2f}"
            self.ids.total_amount_label.text = f"Rs. {total:,.2f}"
        except ValueError:
            self.ids.interest_label.text = "Error"
            self.ids.total_amount_label.text = "Error"

class FarmCalculatorScreen(Screen):
    def go_back(self):
        self.manager.current = 'tools_menu'
        self.manager.transition.direction = 'right'

    def calculate_land(self, text):
        bigha_lbl = self.ids.bigha_label
        biswa_lbl = self.ids.biswa_label
        dhur_lbl = self.ids.dhur_label

        if not text:
            bigha_lbl.text = "0"; biswa_lbl.text = "0"; dhur_lbl.text = "0"
            return

        try:
            hectare = float(text)
            total_bigha = (hectare * 10000) / 2530
            bigha = int(total_bigha)
            remaining_part = total_bigha - bigha
            total_biswa = remaining_part * 20
            biswa = int(total_biswa)
            remaining_biswa = total_biswa - biswa
            dhur = int(remaining_biswa * 20)

            bigha_lbl.text = str(bigha)
            biswa_lbl.text = str(biswa)
            dhur_lbl.text = str(dhur)
        except ValueError:
            pass

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.1, 0.1, 0.1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(size_hint_y=0.2))
        layout.add_widget(Label(text="DK JAN SUVIDHA KENDRA", font_size=60, bold=True, color=(1, 0.8, 0, 1), size_hint_y=None, height=100))
        layout.add_widget(Label(text="Login to Continue", font_size=40, color=(1, 1, 1, 1), size_hint_y=None, height=60))
        self.mobile_input = TextInput(hint_text="Enter Mobile Number", multiline=False, input_filter='int', font_size=40, size_hint_y=None, height=100, padding_y=[25, 0], halign='center')
        layout.add_widget(self.mobile_input)
        self.error_label = Label(text="", color=(1, 0, 0, 1), font_size=30, size_hint_y=None, height=50)
        layout.add_widget(self.error_label)
        login_btn = Button(text="LOGIN", font_size=40, bold=True, background_color=(0, 0.6, 0, 1), size_hint_y=None, height=120)
        login_btn.bind(on_press=self.check_login)
        layout.add_widget(login_btn)
        layout.add_widget(Label(size_hint_y=0.3))
        self.add_widget(layout)

    def check_login(self, instance):
        if len(self.mobile_input.text) == 10:
            self.manager.get_screen('main').update_footer_info(self.mobile_input.text)
            self.manager.current = 'main'
            self.manager.transition.direction = 'left'
        else:
            self.error_label.text = "Please enter valid 10-digit number!"

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        
        header = BoxLayout(orientation='vertical', size_hint=(1, 0.16), padding=5)
        with header.canvas.before:
            Color(0, 0, 0.6, 1); self.h_rect = Rectangle(size=header.size, pos=header.pos)
        header.bind(size=self._update_rect, pos=self._update_rect)
        
        self.time_lbl = Label(text="", font_size=35, bold=True, size_hint=(1, 0.25), halign='right')
        Clock.schedule_interval(lambda dt: setattr(self.time_lbl, 'text', time.strftime("%d-%b-%Y %I:%M %p")), 1)
        header.add_widget(self.time_lbl)
        header.add_widget(Label(text="DK JAN SUVIDHA KENDRA", font_size=80, bold=True, color=(1, 0.8, 0, 1), size_hint=(1, 0.5)))
        header.add_widget(Label(text="ADDRESS: RANI KHEDA CHUARAHA", font_size=45, size_hint=(1, 0.25)))
        root.add_widget(header)

        scroll = ScrollView(size_hint=(1, 0.76))
        layout = GridLayout(cols=1, spacing=15, size_hint_y=None, padding=20)
        layout.bind(minimum_height=layout.setter('height'))

        tools_btn = Button(text="TOOLS (Calculators)", size_hint_y=None, height=150, font_size=60, bold=True, background_color=(1, 0.5, 0, 1))
        tools_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'tools_menu'))
        layout.add_widget(tools_btn)

        services = {"Aadhaar Card Services": "https://uidai.gov.in",
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
            btn = Button(text=name, size_hint_y=None, height=130, font_size=60, italic=True, bold=True, background_color=(0, 0.6, 0.6, 1))
            btn.bind(on_press=lambda x, l=link: webbrowser.open(l))
            layout.add_widget(btn)

        scroll.add_widget(layout)
        root.add_widget(scroll)

        footer = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), padding=5)
        with footer.canvas.before:
            Color(0, 0.5, 0, 1); self.f_rect = Rectangle(size=footer.size, pos=footer.pos)
        footer.bind(size=self._update_f_rect, pos=self._update_f_rect)
        
        footer.add_widget(Label(text="Contact: 8318736819", font_size=28, bold=True, size_hint_x=0.4))
        self.user_lbl = Label(text="Login: ...", font_size=28, bold=True, color=(1,1,0,1), size_hint_x=0.35)
        footer.add_widget(self.user_lbl)
        
        logout = Button(text="LOGOUT", font_size=25, bold=True, background_color=(1,0,0,1), size_hint_x=0.15)
        logout.bind(on_press=lambda x: setattr(self.manager, 'current', 'login'))
        footer.add_widget(logout)
        root.add_widget(footer)
        self.add_widget(root)

    def _update_rect(self, instance, value): self.h_rect.pos = instance.pos; self.h_rect.size = instance.size
    def _update_f_rect(self, instance, value): self.f_rect.pos = instance.pos; self.f_rect.size = instance.size
    def update_footer_info(self, mobile): self.user_lbl.text = f"Login: {mobile}"

class DKIntegratedApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_string(KV_TOOLS)
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ToolsMenuScreen(name='tools_menu'))
        sm.add_widget(AgeCalculatorScreen(name='age_calc'))
        sm.add_widget(CashCounterScreen(name='cash_counter'))
        
        sm.add_widget(InterestCalculatorScreen(name='interest_calc'))
        sm.add_widget(FarmCalculatorScreen(name='farm_calc'))
        
        return sm

if __name__ == '__main__':
    DKIntegratedApp().run()