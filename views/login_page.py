import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req

class LoginPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.email_var = tb.StringVar()
        self.password_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=SUCCESS)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=DARK)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=LIGHT)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=5)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=LIGHT)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=5)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(side=BOTTOM, ipadx=34, ipady=45)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(side=TOP, ipadx=114, ipady=2)
        tb.Label(self.top3, text="Welcome back", bootstyle="inverse-primary", font=('Helvetica', 30)).pack(side=TOP, pady=40)
        tb.Label(self.top3, text="Please log into your account", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=TOP)
        tb.Label(self.top3, text="Email", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=BOTTOM)
        self.search_bar = tb.Entry(self.bottom3, bootstyle=INFO, textvariable=self.email_var).pack(side=TOP,pady=10)
        self.bottom4 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom4.pack(side=TOP, ipadx=56, ipady=0)
        tb.Button(self.bottom4, text="Back",command=self.app.main_page, bootstyle=DANGER).pack(side=LEFT, ipadx=20,ipady=3, padx=25, pady=10)
        tb.Button(self.bottom4, text="Submit", bootstyle=SUCCESS,command=self.login).pack(side=RIGHT, ipadx=12,ipady=3, padx=25, pady=10)
        self.search_bar = tb.Entry(self.bottom3, bootstyle=INFO, textvariable=self.password_var, show="*").pack(side=BOTTOM,pady=10)
        tb.Label(self.bottom3, text="Password", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=BOTTOM)

    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()
        auth = req.post(f"{self.app.url}token", data={"username": email,
                                                                  "password": password}).json()

        try:
            self.app.token = {"access_token": auth["access_token"], "token_type": "bearer"}
            self.app.authenticated = TRUE
            self.app.email = email
            self.password_var.set("")
            self.app.user_page()
        except:
            self.create_toast("401 Error", "Bad Credentials")
