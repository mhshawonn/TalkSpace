


#Creted by Shawon


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(781, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(781, 613))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QScrollBar:vertical {              \n"
"       border: 1px solid #999999;\n"
"        background:white;\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 164, 141, 135), stop:0.732955 rgba(128, 194, 194, 203));\n"
"        min-height: 0px;\n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    \n"
"/*-------------------------Horizontal------------------------*/\n"
"QScrollBar:horizontal {              \n"
"       border: 1px solid #999999;\n"
"        background:white;\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 164, 141, 135), stop:0.732955 rgba(128, 194, 194, 203));\n"
"        min-height: 0px;\n"
"    }\n"
"    QScrollBar::add-line:horizontal {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SlidingMenu = QtWidgets.QFrame(self.centralwidget)
        self.SlidingMenu.setEnabled(True)
        self.SlidingMenu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.SlidingMenu.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"border:None")
        self.SlidingMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SlidingMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SlidingMenu.setObjectName("SlidingMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SlidingMenu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_layout_side = QtWidgets.QGridLayout()
        self.Button_layout_side.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Button_layout_side.setContentsMargins(-1, 0, 0, 0)
        self.Button_layout_side.setHorizontalSpacing(6)
        self.Button_layout_side.setVerticalSpacing(170)
        self.Button_layout_side.setObjectName("Button_layout_side")
        self.UserLayout = QtWidgets.QVBoxLayout()
        self.UserLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.UserLayout.setContentsMargins(51, 0, 51, 9)
        self.UserLayout.setSpacing(7)
        self.UserLayout.setObjectName("UserLayout")
        self.UserIcon = QtWidgets.QLabel(self.SlidingMenu)
        self.UserIcon.setMaximumSize(QtCore.QSize(100, 100))
        self.UserIcon.setStyleSheet("color:white;")
        self.UserIcon.setText("")
        self.UserIcon.setPixmap(QtGui.QPixmap(":/Icons/824-8246267_time-left-user-icon-round-png.png"))
        self.UserIcon.setScaledContents(True)
        self.UserIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.UserIcon.setObjectName("UserIcon")
        self.UserLayout.addWidget(self.UserIcon, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserNickname = QtWidgets.QLabel(self.SlidingMenu)
        self.UserNickname.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(85)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserNickname.sizePolicy().hasHeightForWidth())
        self.UserNickname.setSizePolicy(sizePolicy)
        self.UserNickname.setMinimumSize(QtCore.QSize(0, 0))
        self.UserNickname.setMaximumSize(QtCore.QSize(200, 20))
        self.UserNickname.setBaseSize(QtCore.QSize(0, 4))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.UserNickname.setFont(font)
        self.UserNickname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UserNickname.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.UserNickname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.UserNickname.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.UserNickname.setLineWidth(2)
        self.UserNickname.setScaledContents(True)
        self.UserNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.UserNickname.setWordWrap(False)
        self.UserNickname.setIndent(0)
        self.UserNickname.setObjectName("UserNickname")
        self.UserLayout.addWidget(self.UserNickname, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Button_layout_side.addLayout(self.UserLayout, 1, 0, 1, 1)
        self.Hamburger = QtWidgets.QPushButton(self.SlidingMenu)
        self.Hamburger.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hamburger.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(38, 38, 38);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(53, 53, 53);\n"
"\n"
"}")
        self.Hamburger.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/white-menu-icon-12.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Hamburger.setIcon(icon)
        self.Hamburger.setIconSize(QtCore.QSize(64, 64))
        self.Hamburger.setObjectName("Hamburger")
        self.Button_layout_side.addWidget(self.Hamburger, 0, 0, 1, 1)
        self.Settings_button = QtWidgets.QPushButton(self.SlidingMenu)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Settings_button.setFont(font)
        self.Settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settings_button.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"padding-left:72px;\n"
"height:50px;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:5px;\n"
"    background-color: rgb(38, 38, 38);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/setting-icon-png-18.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings_button.setIcon(icon1)
        self.Settings_button.setIconSize(QtCore.QSize(32, 32))
        self.Settings_button.setFlat(True)
        self.Settings_button.setObjectName("Settings_button")
        self.Button_layout_side.addWidget(self.Settings_button, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.Button_layout_side)
        self.horizontalLayout.addWidget(self.SlidingMenu)
        self.MainChat = QtWidgets.QWidget(self.centralwidget)
        self.MainChat.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"background-color: rgb(35, 35, 35);")
        self.MainChat.setObjectName("MainChat")
        self.gridLayout = QtWidgets.QGridLayout(self.MainChat)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.Send_Button = QtWidgets.QPushButton(self.MainChat)
        self.Send_Button.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Send_Button.setFont(font)
        self.Send_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Send_Button.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"   border:none;\n"
"background-color: None;\n"
"}\n"
"QPushButton:pressed {\n"
"border-radius:25px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 164, 141, 135), stop:0.732955 rgba(128, 194, 194, 203));\n"
"\n"
"}\n"
"")
        self.Send_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/content+send+icon-1320087227200139227.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Send_Button.setIcon(icon2)
        self.Send_Button.setIconSize(QtCore.QSize(50, 50))
        self.Send_Button.setDefault(False)
        self.Send_Button.setFlat(False)
        self.Send_Button.setObjectName("Send_Button")
        self.gridLayout.addWidget(self.Send_Button, 1, 3, 1, 1)
        self.EmojiPane = QtWidgets.QTabWidget(self.MainChat)
        self.EmojiPane.setMinimumSize(QtCore.QSize(0, 0))
        self.EmojiPane.setMaximumSize(QtCore.QSize(0, 16777215))
        self.EmojiPane.setStyleSheet("QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"  \n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #fdf6e3;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #fdf6e3);\n"
"}\n"
"\n"
"\n"
"QScrollArea{\n"
"border:none;\n"
"}\n"
"")
        self.EmojiPane.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.EmojiPane.setIconSize(QtCore.QSize(17, 16))
        self.EmojiPane.setUsesScrollButtons(False)
        self.EmojiPane.setObjectName("EmojiPane")
        self.Smiles = QtWidgets.QWidget()
        self.Smiles.setEnabled(True)
        self.Smiles.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 37, 32, 135), stop:0.732955 rgba(128, 194, 194, 203));\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: None; /* make the default button prominent */\n"
"}\n"
"\n"
"")
        self.Smiles.setObjectName("Smiles")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Smiles)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollSmiles = QtWidgets.QScrollArea(self.Smiles)
        self.scrollSmiles.setStyleSheet("")
        self.scrollSmiles.setWidgetResizable(True)
        self.scrollSmiles.setObjectName("scrollSmiles")
        self.Emo_Smiles = QtWidgets.QWidget()
        self.Emo_Smiles.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Smiles.setStyleSheet("QScrollBar:vertical {              \n"
"       border: 1px solid #999999;\n"
"        background:white;\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }")
        self.Emo_Smiles.setObjectName("Emo_Smiles")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Emo_Smiles)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollSmiles.setWidget(self.Emo_Smiles)
        self.verticalLayout_2.addWidget(self.scrollSmiles)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Emojis/EmojiUnclicked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Smiles, icon3, "")
        self.Animals = QtWidgets.QWidget()
        self.Animals.setStyleSheet("")
        self.Animals.setObjectName("Animals")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Animals)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollAnimals = QtWidgets.QScrollArea(self.Animals)
        self.scrollAnimals.setWidgetResizable(True)
        self.scrollAnimals.setObjectName("scrollAnimals")
        self.Emo_Animals = QtWidgets.QWidget()
        self.Emo_Animals.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Animals.setObjectName("Emo_Animals")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Emo_Animals)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollAnimals.setWidget(self.Emo_Animals)
        self.verticalLayout_3.addWidget(self.scrollAnimals)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Emojis/Bear_Tab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Animals, icon4, "")
        self.Food = QtWidgets.QWidget()
        self.Food.setObjectName("Food")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Food)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ScrollFood = QtWidgets.QScrollArea(self.Food)
        self.ScrollFood.setWidgetResizable(True)
        self.ScrollFood.setObjectName("ScrollFood")
        self.Emo_Food = QtWidgets.QWidget()
        self.Emo_Food.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Food.setObjectName("Emo_Food")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Emo_Food)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ScrollFood.setWidget(self.Emo_Food)
        self.verticalLayout_4.addWidget(self.ScrollFood)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Emojis/burger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Food, icon5, "")
        self.Activity = QtWidgets.QWidget()
        self.Activity.setObjectName("Activity")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Activity)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollActivity = QtWidgets.QScrollArea(self.Activity)
        self.scrollActivity.setWidgetResizable(True)
        self.scrollActivity.setObjectName("scrollActivity")
        self.Emo_Activity = QtWidgets.QWidget()
        self.Emo_Activity.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Activity.setObjectName("Emo_Activity")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Emo_Activity)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollActivity.setWidget(self.Emo_Activity)
        self.verticalLayout_5.addWidget(self.scrollActivity)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Emojis/football.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Activity, icon6, "")
        self.Travel = QtWidgets.QWidget()
        self.Travel.setObjectName("Travel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Travel)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollTravel = QtWidgets.QScrollArea(self.Travel)
        self.scrollTravel.setWidgetResizable(True)
        self.scrollTravel.setObjectName("scrollTravel")
        self.Emo_Travel = QtWidgets.QWidget()
        self.Emo_Travel.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Travel.setObjectName("Emo_Travel")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Emo_Travel)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollTravel.setWidget(self.Emo_Travel)
        self.verticalLayout_6.addWidget(self.scrollTravel)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Emojis/building.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Travel, icon7, "")
        self.Objects = QtWidgets.QWidget()
        self.Objects.setObjectName("Objects")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Objects)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollObjects = QtWidgets.QScrollArea(self.Objects)
        self.scrollObjects.setWidgetResizable(True)
        self.scrollObjects.setObjectName("scrollObjects")
        self.Emo_Objects = QtWidgets.QWidget()
        self.Emo_Objects.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Objects.setObjectName("Emo_Objects")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Emo_Objects)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollObjects.setWidget(self.Emo_Objects)
        self.verticalLayout_7.addWidget(self.scrollObjects)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Emojis/light_bulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Objects, icon8, "")
        self.Symbols = QtWidgets.QWidget()
        self.Symbols.setObjectName("Symbols")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Symbols)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollSymbols = QtWidgets.QScrollArea(self.Symbols)
        self.scrollSymbols.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollSymbols.setWidgetResizable(True)
        self.scrollSymbols.setObjectName("scrollSymbols")
        self.Emo_Symbols = QtWidgets.QWidget()
        self.Emo_Symbols.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Symbols.setObjectName("Emo_Symbols")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Emo_Symbols)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollSymbols.setWidget(self.Emo_Symbols)
        self.verticalLayout_8.addWidget(self.scrollSymbols)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Emojis/symbols.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Symbols, icon9, "")
        self.Flag = QtWidgets.QWidget()
        self.Flag.setObjectName("Flag")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Flag)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollFlag = QtWidgets.QScrollArea(self.Flag)
        self.scrollFlag.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollFlag.setWidgetResizable(True)
        self.scrollFlag.setObjectName("scrollFlag")
        self.Emo_Flag = QtWidgets.QWidget()
        self.Emo_Flag.setGeometry(QtCore.QRect(0, 0, 18, 505))
        self.Emo_Flag.setObjectName("Emo_Flag")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.Emo_Flag)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollFlag.setWidget(self.Emo_Flag)
        self.verticalLayout_9.addWidget(self.scrollFlag)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Emojis/flag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmojiPane.addTab(self.Flag, icon10, "")
        self.gridLayout.addWidget(self.EmojiPane, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.emojiButton = QtWidgets.QPushButton(self.MainChat)
        self.emojiButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.emojiButton.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"   border:none;\n"
"background-color: None;\n"
"height:35px\n"
"}\n"
"QPushButton:hover {\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.emojiButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Emojis/EmojiUnclicked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(":/Emojis/EmojiClicked.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon11.addPixmap(QtGui.QPixmap(":/Emojis/EmojiClicked.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.emojiButton.setIcon(icon11)
        self.emojiButton.setIconSize(QtCore.QSize(32, 50))
        self.emojiButton.setCheckable(True)
        self.emojiButton.setChecked(False)
        self.emojiButton.setFlat(False)
        self.emojiButton.setObjectName("emojiButton")
        self.gridLayout.addWidget(self.emojiButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.textEdit = QtWidgets.QTextEdit(self.MainChat)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(102, 102, 102);\n"
"color: white;\n"
"border-radius:20px;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 2, 1, 1)
        self.messagesView = QtWidgets.QListView(self.MainChat)
        self.messagesView.setMinimumSize(QtCore.QSize(0, 1))
        self.messagesView.setStyleSheet("border:none;")
        self.messagesView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.messagesView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messagesView.setResizeMode(QtWidgets.QListView.Adjust)
        self.messagesView.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.messagesView.setObjectName("messagesView")
        self.gridLayout.addWidget(self.messagesView, 0, 2, 1, 2)
        self.attachButton = QtWidgets.QPushButton(self.MainChat)
        self.attachButton.setStyleSheet("QPushButton {\n"
" color: #FFFFFF;\n"
"  border:none;\n"
"background-color: None;\n"
"height:50px;\n"
"width:50px;\n"
"}\n"
"QPushButton:pressed {\n"
"border-radius:25px;\n"
"    background-color: rgb(49, 49, 49);\n"
"}\n"
"")
        self.attachButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icons/attachItem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attachButton.setIcon(icon12)
        self.attachButton.setIconSize(QtCore.QSize(32, 32))
        self.attachButton.setFlat(True)
        self.attachButton.setObjectName("attachButton")
        self.gridLayout.addWidget(self.attachButton, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.MainChat)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.EmojiPane.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client Server Chat "))
        self.UserNickname.setText(_translate("MainWindow", "UserName"))
        self.Settings_button.setText(_translate("MainWindow", "Settings"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Poppins\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:20px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.getTextStyles = self.textEdit.toHtml()
import Icons_Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
