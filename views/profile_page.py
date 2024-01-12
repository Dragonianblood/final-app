import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req

class ProfilePage(View):
    def __init__(self, app):
        super().__init__(app)
        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=INFO)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=DARK)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=LIGHT)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=10, pady=50)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=LIGHT)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=10, pady=50)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(expand=True, ipadx=116, ipady=25)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(expand=True, ipadx=11, ipady=15 )
        self.name = tb.Label(self.top3, text=f"Name: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.name.pack(side=TOP, pady=10)
        self.nick = tb.Label(self.top3, text=f"Nickname: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.nick.pack(side=TOP, pady=10)
        self.email = tb.Label(self.top3, text=f"Email: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.email.pack(side=TOP, pady=10)

        self.bottom4 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom4.pack(expand=True, ipadx=56, ipady=0)
        tb.Button(self.bottom4, text="Back",command=self.app.user_page, bootstyle=DANGER).pack(expand=True,ipady=3, pady=10, ipadx=20)
