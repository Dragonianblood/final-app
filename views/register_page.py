import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req
from json import dumps

class RegisterPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.role = "Admin"
        self.name_var = tb.StringVar()
        self.nick_var = tb.StringVar()
        self.email_var = tb.StringVar()
        self.password_var1 = tb.StringVar()
        self.password_var2 = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=SECONDARY)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=DARK)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=LIGHT)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=5)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=LIGHT)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=5)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(side=BOTTOM, ipadx=34, ipady=0)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(side=TOP, ipadx=46, ipady=2)
        tb.Label(self.top3, text="Your food venture\n      starts here", bootstyle="inverse-primary", font=('Helvetica', 30)).pack(side=TOP, pady=30)
        self.top4 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top4.pack(side=TOP)
        tb.Label(self.top4, text="Name: ", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT)
        tb.Entry(self.top4, bootstyle=INFO, textvariable=self.name_var).pack(side=RIGHT,pady=10)
        self.top5 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top5.pack(side=TOP)
        tb.Label(self.top5, text="Nickname: ", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT)
        tb.Entry(self.top5, bootstyle=INFO, textvariable=self.nick_var).pack(side=RIGHT,pady=10)
        self.bottom4 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom4.pack(side=TOP, ipadx=91, ipady=0)
        tb.Button(self.bottom4, text="Back",command=self.app.main_page, bootstyle=DANGER).pack(side=LEFT, ipadx=20,ipady=3, padx=25, pady=10)
        tb.Button(self.bottom4, text="Submit", bootstyle=SUCCESS,command=self.register).pack(side=RIGHT, ipadx=12,ipady=3, padx=25, pady=10)
        self.bottom6 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom6.pack(side=TOP)
        tb.Label(self.bottom6, text="Email: ", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT)
        tb.Entry(self.bottom6, bootstyle=INFO, textvariable=self.email_var).pack(side=RIGHT,pady=10)
        self.bottom5 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom5.pack(side=TOP)
        tb.Label(self.bottom5, text="Password: ", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT)
        tb.Entry(self.bottom5, bootstyle=INFO, textvariable=self.password_var1, show="*").pack(side=LEFT,pady=10)
        self.bottom7 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom7.pack(side=TOP)
        tb.Label(self.bottom7, text="retype Password: ", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT)
        tb.Entry(self.bottom7, bootstyle=INFO, textvariable=self.password_var2, show="*").pack(side=LEFT,pady=10)

    def register(self):
        if self.password_var1.get() == self.password_var2.get():
            auth = req.post(f"{self.app.url}users", data=dumps({"alt_name": self.nick_var.get(),
                                                                "id": 3,
                                                              "email": self.email_var.get(),
                                                              "name": self.name_var.get(),
                                                              "password": self.password_var1.get(),
                                                              "role": "Admin"})).json()
            if auth is None:
                self.create_toast("Account Created", "Welcome to Food Online")
                auth = req.post(f"{self.app.url}token", data={"username": self.email_var.get(),
                                                                  "password": self.password_var1.get()}).json()
                self.app.token = {"access_token": auth["access_token"], "token_type": "bearer"}
                self.app.authenticated = TRUE
                self.app.email = self.email_var.get()
                self.password_var1.set("")
                self.app.user_page()
            else:
                self.create_toast("401 Error", "Bad Credentials")
        else:
            self.create_toast("401 Error", "Passwords Dont Match")
