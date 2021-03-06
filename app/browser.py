# code from https://www.geeksforgeeks.org/creating-a-tabbed-browser-using-pyqt5/
#Code modified by Azlan Chenlong
# importing required libraries

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtPrintSupport import *
from PyQt6 import QtNetwork
from Ignite import flame
import os
import sys
import subprocess


core = flame()
# main window
class MainWindow(QMainWindow):
# constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Set Up Proxy
        proxy =  QtNetwork.QNetworkProxy()
        proxy.setType(QtNetwork.QNetworkProxy.ProxyType.HttpProxy)
        proxy.setHostName("localhost")
        proxy.setPort(8088)
        QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

        #Check Cache for url
        global url
        try:
            cache = open("IgniteBrowserCache.txt","r")
            url = cache.read()
            cache.close()
            del cache
        except FileNotFoundError:
            url = "None"
            pass

        #reset cache file
        cache = open("IgniteBrowserCache.txt","w")
        cache.write("None")
        cache.close()
        del cache

        # creating a tab widget
        self.tabs = QTabWidget()

        # making document mode true
        self.tabs.setDocumentMode(True)

        # adding action when double clicked
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        # adding action when tab is changed
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # making tabs closeable
        self.tabs.setTabsClosable(True)

        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        # making tabs as central widget
        self.setCentralWidget(self.tabs)

        # creating a status bar
        self.status = QStatusBar()

        # setting status bar to the main window
        self.setStatusBar(self.status)

        # creating a tool bar for navigation
        navtb = QToolBar("Navigation")

        # adding tool bar tot he main window
        self.addToolBar(navtb)

        # creating back action
        back_btn = QAction("Back", self)

        # setting status tip
        back_btn.setStatusTip("Back to previous page")

        # adding action to back button
        # making current tab to go back
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        # adding this to the navigation tool bar
        navtb.addAction(back_btn)

        # similarly adding next button
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        # similarly adding reload button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        # creating home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")

        # adding action to home button
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        
        # Create new Tab action for ease of access
        newtab_btn = QAction("New Tab", self)
        newtab_btn.setStatusTip("Create a new tab, double click in the tab space to do the same")
        newtab_btn.triggered.connect(self.new_tab)
        navtb.addAction(newtab_btn)

        # adding a separator
        navtb.addSeparator()

        # creating a line edit widget for URL
        self.urlbar = QLineEdit()

        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding line edit to tool bar
        navtb.addWidget(self.urlbar)

        # similarly adding stop action
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        #check if new url sent
        if url == "None":
            url = 'https://www.google.com'
            
        # creating first tab
        self.add_new_tab(QUrl(url), 'Homepage')

        # showing all the components
        self.show()

        # setting window title
        self.setWindowTitle("Ignite Browser")
    def new_tab(self):
        self.add_new_tab()

    # method for adding new tab
    def add_new_tab(self, qurl = None, label ="Blank"):

        # if url is blank
        if qurl is None:
                # creating a google url or sent url
                qurl = QUrl('https://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

        # setting url to browser
        browser.setUrl(qurl)


        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser = browser:
                                                        self.update_urlbar(qurl, browser))

        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                                                self.tabs.setTabText(i, browser.page().title()))

    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
                # creating a new tab
                self.add_new_tab()

    # when tab is changed
    def current_tab_changed(self, i):

        # get the curl
        qurl = self.tabs.currentWidget().url()

        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())

        # update the title
        self.update_title(self.tabs.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabs.count() < 2:
                # do nothing
                return

        # else remove the tab
        page = self.tabs.widget(i)
        self.tabs.removeTab(i)
        page.deleteLater()

    # method for updating the title
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
                # do nothing
                return

        # get the page title
        title = self.tabs.currentWidget().page().title()

        # set the window title
        self.setWindowTitle("% s - Ignite Browser" % title)

    # action to go to home
    def navigate_home(self):

        # go to google
        self.tabs.currentWidget().setUrl(QUrl("https://www.google.com"))

    # method for navigate to url
    def navigate_to_url(self):

        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())

        # if scheme is blank
        if q.scheme() == "":
                # set scheme
                q.setScheme("http")

        # set the url
        self.tabs.currentWidget().setUrl(q)

    # method to update the url
    def update_urlbar(self, q, browser = None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():

                return

        # set text to the url bar
        self.urlbar.setText(q.toString())

        # set cursor position
        self.urlbar.setCursorPosition(0)

# creating a PyQt6 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Ignite Browser")

# creating MainWindow object
window = MainWindow()

# loop
pid1 = subprocess.Popen([sys.executable, "temp.pyw"])#starts the proxy
app.exec()
