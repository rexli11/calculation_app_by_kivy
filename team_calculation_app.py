from re import MULTILINE
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import webbrowser
from kivy.config import Config
from kivy.core.window import Window
Config.set('kivy', 'system', 'keyboard_mode')  # 控制手機系統與鍵盤

# 版本號碼
version = "1.0.3"

# 導入字體
LabelBase.register(
    # 系統字形
    name='Roboto',
    # 更換的字形
    fn_regular='NotoSansCJKtc-Regular.otf')

# 清除背景色
Window.clearcolor = (244, 221, 53, 1)


# 按鈕設定
class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 字體對齊、字形大小、背景色
        self.halign = 'center'
        self.font_size = self.width / 2
        self.background_color = '#00E3E3'


# 文字輸入框設定
class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 字體對齊、禁止多行輸入、背景色
        self.halign = 'center'
        self.multiline = False
        self.background_color = '#CCEEFF'


class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 調整字體大小、顏色與對齊處
        self.halign = 'center'
        self.font_size = self.width / 2
        self.color = '#000000'


class MyLabel_tip(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 調整字體大小、顏色與對齊處
        self.halign = 'center'
        self.font_size = self.width / 2
        self.color = '#000000'


def webLink(instance):
    # 連結的網址
    webbrowser.open("https://github.com/rexli11")


# App主體
class TscrtBounsIntroduction(App):
    def build(self):
        # 設定主要面板布局
        self.window = GridLayout()
        # 設定欄位數
        self.window.cols = 1
        self.window.size_hint = (0.8, 1)
        # 間隔
        self.window.spacing = 10
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # 頂部的Button連結
        self.top_right = Button(
            background_normal="link_one.png",
            background_down="link_two.png",
            size_hint=(1, 0.1)
        )
        self.top_right.bind(on_press=webLink)
        self.window.add_widget(self.top_right)

        # 輸出位置
        self.outputresult = Label(
            text="Out put result \n 結果輸出處",
            font_size="55",  # 原始為60
            color='#000000',
            size_hint=(1, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        self.window.add_widget(self.outputresult)
        # 調用滾動
        self.create_scrollview()

        return self.window

    # 建立滾動處
    def create_scrollview(self):
        # 主要布局
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.layout.spacing = 20
        self.layout.bind(minimum_height=self.layout.setter("height"))

        # 橫向布局_0
        self.hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.hori.spacing = 10

        # 橫向布局_0
        self.one_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.one_hori.spacing = 10

        # 橫向布局_2
        self.two_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.two_hori.spacing = 10

        # 橫向布局_3
        self.three_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.three_hori.spacing = 10

        # 橫向布局_4
        self.four_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.four_hori.spacing = 10

        # 橫向布局_5
        self.five_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.five_hori.spacing = 10

        # 橫向布局_6
        self.six_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.six_hori.spacing = 10

        # 橫向布局_7
        self.seven_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.seven_hori.spacing = 10

        # 橫向布局_8
        self.eight_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.eight_hori.spacing = 10

        # 橫向布局_9
        self.nine_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.nine_hori.spacing = 10

        # 橫向布局_10
        self.ten_hori = BoxLayout(orientation="horizontal", size_hint_y=None)
        # self.hori.bind(minimum_height=self.layout.setter("height"))
        self.ten_hori.spacing = 10

        # =============================================================
        # 起始設定
        # 原始layout
        self.one_label = MyLabel(
            text="選擇入會方案",
            size_hint=(1, None),
        )
        self.layout.add_widget(self.one_label)

        # -----------------------------------------------
        # boxlayout
        self.one_button = MyButton(
            text="A方案",
            size_hint=(0.2, None))
        self.one_button.bind(on_press=self.one_info)
        self.hori.add_widget(self.one_button)

        self.two_button = MyButton(
            text="B方案",
            size_hint=(0.2, None))
        self.two_button.bind(on_press=self.two_info)
        self.hori.add_widget(self.two_button)

        self.three_button = MyButton(
            text="C方案",
            size_hint=(0.2, None))
        self.three_button.bind(on_press=self.three_info)
        self.hori.add_widget(self.three_button)

        self.four_button = MyButton(
            text="D方案",
            size_hint=(0.2, None))
        self.four_button.bind(on_press=self.four_info)
        self.hori.add_widget(self.four_button)

        # 添加回原始layout
        self.layout.add_widget(self.hori)

        # =============================================================
        # referral_bonus(first bouns)設定
        self.partner = MyLabel(
            text="獎金A計算",
            size_hint=(1, None)
        )
        self.layout.add_widget(self.partner)

        '''添加至one_hori'''
        self.one_life_button = MyButton(text="A方案",
                                        size_hint=(0.2, None))
        self.one_life_button.bind(on_press=self.one_referral_bouns)
        self.one_hori.add_widget(self.one_life_button)

        self.two_life_button = MyButton(text="B方案",
                                        size_hint=(0.2, None))
        self.two_life_button.bind(on_press=self.two_referral_bouns)
        self.one_hori.add_widget(self.two_life_button)

        self.three_life_button = MyButton(text="C方案",
                                          size_hint=(0.2, None))
        self.three_life_button.bind(on_press=self.three_referral_bouns)
        self.one_hori.add_widget(self.three_life_button)

        self.four_life_button = MyButton(text="D方案",
                                         size_hint=(0.2, None))
        self.four_life_button.bind(on_press=self.four_referral_bouns)
        self.one_hori.add_widget(self.four_life_button)

        # 添加回原始layout
        self.layout.add_widget(self.one_hori)

        # =============================================================
        # second bouns
        # 提示框
        self.second_bouns_label = MyLabel(
            text="獎金B計算",
            size_hint=(1, None)
        )
        self.layout.add_widget(self.second_bouns_label)

        '''two_hori'''
        # 大邊輸入框
        self.mach_big = MyLabel_tip(
            text="左邊業績",
            size_hint=(0.6, None)
        )
        self.two_hori.add_widget(self.mach_big)
        # PV輸入
        self.enterBig = MyTextInput(
            text="0"
        )
        self.two_hori.add_widget(self.enterBig)
        # 添加回原始layout
        self.layout.add_widget(self.two_hori)

        '''three_hori'''
        # 小邊輸入框
        self.mach_small = MyLabel_tip(
            text="右邊業績",
            size_hint=(0.6, None)
        )
        self.three_hori.add_widget(self.mach_small)
        # PV輸入
        self.enterSmall = MyTextInput(
            text="0"
        )
        self.three_hori.add_widget(self.enterSmall)
        self.layout.add_widget(self.three_hori)
        # 呼叫
        self.button = MyButton(text="計算B獎金",
                               size_hint=(0.2, None))
        self.button.bind(on_press=self.mach_bouns)
        self.layout.add_widget(self.button)

        # =============================================================
        # third_bouns
        self.third_bound_label = MyLabel(
            text="獎金C計算",
            size_hint=(1, None)
        )
        # 第一代收入
        self.one = MyLabel_tip(
            text="第一代收入",
            size_hint=(0.6, None)
        )
        self.four_hori.add_widget(self.one)
        self.oneIncome = MyTextInput(
            text="0"
        )
        self.four_hori.add_widget(self.oneIncome)
        self.layout.add_widget(self.four_hori)

        # 第二代收入
        self.two = MyLabel_tip(
            text="第二代收入",
            size_hint=(0.6, None)
        )
        self.five_hori.add_widget(self.two)
        self.twoIncome = MyTextInput(
            text="0")
        self.five_hori.add_widget(self.twoIncome)
        self.layout.add_widget(self.five_hori)

        # 第三代收入
        self.three = MyLabel_tip(
            text="第三代收入",
            size_hint=(0.6, None)
        )
        self.six_hori.add_widget(self.three)
        self.threeIncome = MyTextInput(
            text="0")
        self.six_hori.add_widget(self.threeIncome)
        self.layout.add_widget(self.six_hori)

        # 第四代收入
        self.four = MyLabel_tip(
            text="第四代收入",
            size_hint=(0.6, None)
        )
        self.seven_hori.add_widget(self.four)
        self.fourIncome = MyTextInput(
            text="0")
        self.seven_hori.add_widget(self.fourIncome)
        self.layout.add_widget(self.seven_hori)

        # 第五代收入
        self.five = MyLabel_tip(
            text="第五代收入",
            size_hint=(0.6, None)
        )
        self.eight_hori.add_widget(self.five)
        self.fiveIncome = MyTextInput(
            text="0")
        self.eight_hori.add_widget(self.fiveIncome)
        self.layout.add_widget(self.eight_hori)

        # 呼叫
        self.button = MyButton(text="計算C獎金",
                               size_hint=(0.2, None))
        self.button.bind(on_press=self.equal_bouns)
        self.layout.add_widget(self.button)

        # =============================================================
        # four bouns
        self.fout_bouns_label = MyLabel(
            text="計算D獎金",
            size_hint=(1, None)
        )
        # 人數輸入
        self.organizeLabel = MyLabel_tip(
            text="團隊人數",
            size_hint=(0.6, None)
        )
        self.nine_hori.add_widget(self.organizeLabel)
        # 輸入框
        self.organizeNum = MyTextInput(
            text="0")
        self.nine_hori.add_widget(self.organizeNum)
        self.layout.add_widget(self.nine_hori)

        # 呼叫
        self.button = MyButton(text="計算D獎金",
                               size_hint=(0.2, None))
        self.button.bind(on_press=self.people_bouns)
        self.layout.add_widget(self.button)

        # =============================================================
        self.button = MyButton(text="計算所有獎金",
                               size_hint=(0.2, None))
        self.button.bind(on_press=self.all_bouns)
        self.layout.add_widget(self.button)
        # =============================================================

        # 增加的空格
        for i in range(10):
            self.test = Label(
                size_hint=(0.2, None)
            )
            self.layout.add_widget(self.test)

        # =============================================================
        # 導入滾動函式
        scrollview = ScrollView(size=(Window.width, Window.height))
        scrollview.add_widget(self.layout)
        self.window.add_widget(scrollview)

    # =============================================================
    # 獎金計算函式
    # =============================================================
    # 初始位階比例
    def one_info(self, *args):
        self.level_text = self.one_button.text[0]
        if self.level_text == "A":
            # 對等獎金比例
            self.equal_percent = "5"
            # 領的代數
            self.gengr = "1"
            # 見點獎金人數
            self.max_people = "10"
            # 顯示於levelOutput
            self.outputresult.text = "您的初始階級 : XX級 \n" + "獎金A比例 : 1% \n" + \
                "獎金B比例 : 1% \n" + "代數領" + "1~2代最多" + self.max_people + \
                "人 \n" + "獎金C : 領" + self.gengr + "代 共15% \n"
        else:
            pass

        return self.equal_percent, self.gengr, self.max_people, self.level_text

    def two_info(self, *args):
        self.level_text = self.two_button.text[0]
        if self.level_text == "B":
            self.equal_percent = "10"
            self.gengr = "2"
            self.max_people = "20"
            self.outputresult.text = "您的初始階級 : XX級 \n" + "獎金A比例 : 2% \n" + \
                "獎金B比例 : 2% \n" + "代數領" + "2~3代最多" + self.max_people + \
                "人 \n" + "獎金C : 領" + self.gengr + "代 共25% \n" + "無設定費，無入會費"
        else:
            pass

        return self.equal_percent, self.gengr, self.max_people, self.level_text

    def three_info(self, *args):
        self.level_text = self.three_button.text[0]
        if self.level_text == "C":
            self.equal_percent = "15"
            self.gengr = "3"
            self.max_people = "30"
            self.outputresult.text = "您的初始階級 : XX級 \n" + "獎金A比例 : 3% \n" + \
                "獎金B比例 : 3% \n" + "代數領" + "3~4代最多" + self.max_people + \
                "人 \n" + "獎金C : 領" + self.gengr + "代 共30% \n" + "無設定費，無入會費"
        else:
            pass

        return self.equal_percent, self.gengr, self.max_people, self.level_text

    def four_info(self, *args):
        self.level_text = self.four_button.text[0]
        if self.level_text == "D":
            self.equal_percent = "20"
            self.gengr = "5"
            self.max_people = "40"
            self.outputresult.text = "您的初始階級 : XX級 \n" + "獎金A比例 : 4% \n" + \
                "獎金B比例 : 4% \n" + "代數領" + "4~5代最多" + self.max_people + \
                "人 \n" + "獎金C : 領" + self.gengr + "代 共40% \n" + "無設定費，無入會費"
        else:
            pass

        return self.equal_percent, self.gengr, self.max_people, self.level_text

    # ----------------------------------------------------------
    # 第一獎金 - 獎金A
    def one_referral_bouns(self, *args):
        partner_text = self.one_life_button.text[0]
        self.referral = 20 / 100
        if partner_text == "A":
            self.bouns_calculation = "%.0f" % ((100 * 1) * self.referral)
            self.bouns_output = str(self.bouns_calculation)
            self.outputresult.text = self.bouns_output
            self.outputresult.text = "獎金A為\n" + "新台幣$" + self.bouns_output + "元整"
        else:
            pass

        return self.bouns_calculation

    def two_referral_bouns(self, *args):
        partner_text = self.two_life_button.text[0]
        self.referral = 20 / 100
        if partner_text == "B":
            self.bouns_calculation = "%.0f" % ((300 * 2) * self.referral)
            self.bouns_output = str(self.bouns_calculation)
            self.outputresult.text = self.bouns_output
            self.outputresult.text = "獎金A為\n" + "新台幣$" + self.bouns_output + "元整"
        else:
            pass

        return self.bouns_calculation

    def three_referral_bouns(self, *args):
        partner_text = self.three_life_button.text[0]
        self.referral = 20 / 100
        if partner_text == "C":
            self.bouns_calculation = "%.0f" % ((700 * 3) * self.referral)
            self.bouns_output = str(self.bouns_calculation)
            self.outputresult.text = self.bouns_output
            self.outputresult.text = "獎金A為\n" + "新台幣$" + self.bouns_output + "元整"
        else:
            pass

        return self.bouns_calculation

    def four_referral_bouns(self, *args):
        partner_text = self.four_life_button.text[0]
        self.referral = 20 / 100

        if partner_text == "D":
            self.bouns_calculation = "%.0f" % ((1200 * 4) * self.referral)
            self.bouns_output = str(self.bouns_calculation)
            self.outputresult.text = self.bouns_output
            self.outputresult.text = "獎金A為\n" + "新台幣$" + self.bouns_output + "元整"
        else:
            pass

        return self.bouns_calculation

    # ----------------------------------------------------------
    # 第二獎金 - 獎金B
    def mach_bouns(self, *args):
        try:
            # 大小邊業績
            self.big_side = int(self.enterBig.text)
            self.small_side = int(self.enterSmall.text)

            # 比例判斷由起始階級
            mach_level = self.level_text

            # 比例判斷
            if mach_level == "A":
                self.mach = 1
            elif mach_level == "B":
                self.mach = 2
            elif mach_level == "C":
                self.mach = 3
            elif mach_level == "D":
                self.mach = 4
            elif mach_level == "0":
                self.mach = 0
            else:
                pass

            # 大小邊相減
            self.remaining_performance = self.big_side - self.small_side
            # 相減後剩餘
            self.reserve = self.remaining_performance
            # 獎金計算
            self.mach_cauculation = "%.0f" % (
                ((self.small_side * self.mach) / 100) * 10)
            # 本次獎金B
            self.mach_cauculation_pv = "%.0f" % (
                ((self.small_side * self.mach) / 100))
            # 獎金總計
            self.machTotal = self.mach_cauculation

            # 輸出
            self.outputresult.text = ("本周獎金B : " + self.mach_cauculation_pv + "PV \n" + "本周獎金 : 新台幣$" + str(
                self.machTotal) + "元整 \n" + "本周保留 : " + str(self.reserve) + "PV \n\n" + "必須左右各一位直推\n" + "大邊業績可持續保留")

            return self.machTotal, self.big_side, self.small_side, self.reserve
        except:
            self.machTotal = 0
            self.outputresult.text = "請輸入左邊與右邊業績"
            return self.machTotal

    # ----------------------------------------------------------
    # 第三獎金 - 獎金C
    def equal_bouns(self, level_text, *args):
        try:
            equal_level = self.level_text
            # 獎金比例
            self.equal = int(self.equal_percent)
            # 領的代數
            self.gen = self.gengr
            # 計算獎金
            self.oneIn = int(self.oneIncome.text)
            self.twoIn = int(self.twoIncome.text)
            self.threeIn = int(self.threeIncome.text)
            self.fourIn = int(self.fourIncome.text)
            self.fiveIn = int(self.fiveIncome.text)

            # 增加位階判斷
            if equal_level == "A":
                # 領取總數，型態數字
                self.total_money = self.oneIn + self.twoIn + \
                    self.threeIn + self.fourIn + self.fiveIn
                self.total_money = str(self.total_money)
                # 獎金計算
                self.total = self.oneIn  # 型態數字
                # 獎金C
                self.total_bouns = int((self.equal / 100) * self.total)  # 浮點數
                self.outputresult.text = "周領獎金C : 新台幣$" + \
                    str(self.total_bouns) + "元整 \n" + "代數共領取 : " + \
                    self.gen + "代 \n" + "團隊總收入 : " + self.total_money + "元整"
            elif equal_level == "B":
                # 領取總數，型態數字
                self.total_money = self.oneIn + self.twoIn + \
                    self.threeIn + self.fourIn + self.fiveIn
                self.total_money = str(self.total_money)
                # 獎金計算
                self.total = self.oneIn + self.twoIn  # 型態數字
                # 獎金C
                self.total_bouns = int((self.equal / 100) * self.total)  # 浮點數
                self.outputresult.text = "周領獎金C : 新台幣$" + \
                    str(self.total_bouns) + "元整 \n" + "代數共領取 : " + \
                    self.gen + "代 \n" + "團隊總收入 : " + self.total_money + "元整"
            elif equal_level == "C":
                # 領取總數，型態數字
                self.total_money = self.oneIn + self.twoIn + \
                    self.threeIn + self.fourIn + self.fiveIn
                self.total_money = str(self.total_money)
                # 獎金計算
                self.total = self.oneIn + self.twoIn + self.threeIn  # 型態數字
                # 獎金C
                self.total_bouns = int((self.equal / 100) * self.total)  # 浮點數
                self.outputresult.text = "周領獎金C : 新台幣$" + \
                    str(self.total_bouns) + "元整 \n" + "代數共領取 : " + \
                    self.gen + "代 \n" + "團隊總收入 : " + self.total_money + "元整"
            elif equal_level == "D":
                # 領取總數，型態數字
                self.total_money = self.oneIn + self.twoIn + \
                    self.threeIn + self.fourIn + self.fiveIn
                self.total_money = str(self.total_money)
                # 獎金計算
                self.total = self.oneIn + self.twoIn + \
                    self.threeIn + self.fourIn + self.fiveIn  # 型態數字
                # 獎金C
                self.total_bouns = int((self.equal / 100) * self.total)  # 浮點數
                self.outputresult.text = "周領獎金C : 新台幣$" + \
                    str(self.total_bouns) + "元整 \n" + "代數共領取 : " + \
                    self.gen + "代 \n" + "團隊總收入 : " + self.total_money + "元整"
            else:
                pass

            return self.total_bouns, self.oneIn, self.twoIn, self.threeIn, self.fourIn, self.fiveIn
        except:
            self.total_bouns = 0
            self.outputresult.text = "請輸入五代內團隊收入(單位 - 元)"
            return self.total_bouns

    # ----------------------------------------------------------
    # 第四獎金 - 獎金D
    def people_bouns(self, *args):
        try:
            # 輸入值
            self.people_levels = self.level_text
            # 實際人數
            self.actual_num = int(self.organizeNum.text)
            # 限制最大人數
            self.limit_num = int(self.max_people)
            # 起算人數
            self.comp_limit = 20

            if self.people_levels == "A":
                # 實際人數是否大於限制人數與起算人數
                if self.actual_num > self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.limit_num
                elif self.actual_num < self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.actual_num
                elif self.actual_num < self.limit_num and self.actual_num < self.comp_limit:
                    self.caucul_num = 0
            elif self.people_levels == "B":
                if self.actual_num > self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.limit_num
                elif self.actual_num < self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.actual_num
                elif self.actual_num < self.limit_num and self.actual_num < self.comp_limit:
                    self.caucul_num = 0
            elif self.people_levels == "C":
                if self.actual_num > self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.limit_num
                elif self.actual_num < self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.actual_num
                elif self.actual_num < self.limit_num and self.actual_num < self.comp_limit:
                    self.caucul_num = 0
            elif self.people_levels == "D":
                if self.actual_num > self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.limit_num
                elif self.actual_num < self.limit_num and self.actual_num > self.comp_limit:
                    self.caucul_num = self.actual_num
                elif self.actual_num < self.limit_num and self.actual_num < self.comp_limit:
                    self.caucul_num = 0
            else:
                pass

            # 計算獎金D
            self.point_bouns = self.caucul_num * 30
            # 輸出
            self.outputresult.text = "團隊人數為 : " + str(self.actual_num) + "人 \n" + "獎金計算人數 : " + str(
                self.caucul_num) + "人 \n" + "獎金D為 : 新台幣$" + str(self.point_bouns) + "元"

            return self.point_bouns, self.caucul_num
        except:
            self.outputresult.text = "輸入錯誤，請設定初始階級"

    # ----------------------------------------------------------
    # 計算所有獎金
    def all_bouns(self, *args):
        # 獎金A判斷
        try:
            if self.bouns_output == str(self.bouns_calculation):
                self.bouns_calculation = self.bouns_calculation
            else:
                pass
        except:
            self.bouns_calculation = str("0")

        # 獎金B判斷
        if (self.enterBig.text == "0" and self.enterSmall.text == "0"):
            self.machTotal = str("0")
        else:
            self.machTotal = self.machTotal

        # 獎金C判斷
        if (self.oneIncome.text == "0" and self.twoIncome.text == "0" and self.threeIncome.text == "0" and self.fourIncome.text == "0" and self.fiveIncome.text == "0"):
            self.total_bouns = str("0")
        else:
            pass
        self.total_bouns = self.total_bouns

        # 獎金D判斷
        if self.organizeNum.text == "0":
            self.point_bouns = str("0")
        else:
            self.point_bouns = self.point_bouns

        # 獎金加總
        self.calculation_bouns = (int(self.bouns_calculation) + int(
            self.machTotal) + int(self.total_bouns) + int(self.point_bouns))
        # 輸出
        self.outputresult.text = ("獎金A為 : " + str(self.bouns_calculation) + "元整 \n" + "獎金B為 : " + str(self.machTotal) + "元整 \n" + "獎金C為 : " + str(
            self.total_bouns) + "元整 \n" + "獎金D為 : " + str(self.point_bouns) + "元整 \n\n" + "所有獎金共 : 新台幣$" + str(self.calculation_bouns) + "元整")

        return self.calculation_bouns

    # ----------------------------------------------------------
# 執行
if __name__ == "__main__":
    TscrtBounsIntroduction().run()
