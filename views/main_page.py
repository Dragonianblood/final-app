import ttkbootstrap as tb
from K import *
from views.helper import View

class MainPage(View):
    def __init__(self, app):
        super().__init__(app)

        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=INFO)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=DARK)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=LIGHT)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=5)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=LIGHT)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=5)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(side=BOTTOM, ipadx=37, ipady=25)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(side=TOP, ipadx=131, ipady=15)
        tb.Label(self.top3, text="Food Online", bootstyle="inverse-primary", font=('Helvetica', 30)).pack(side=TOP, pady=60)
        tb.Label(self.top3, text="A convenient way of ordering", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=TOP)
        tb.Label(self.top3, text="food straight to your door", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=TOP)
        tb.Button(self.bottom3, text="Register", command=self.app.register_page, bootstyle=SUCCESS).pack(side=BOTTOM, ipadx=30, ipady=5, pady=40)
        tb.Button(self.bottom3, text="Login", command=self.app.login_page, bootstyle=INFO).pack(side=BOTTOM, ipadx=39,ipady=5)

    # def login(self):
    #     # Your authentication would need to be implemented here
    #     email = self.email_var.get()
    #     password = self.password_var.get()
    #
    #     if email == "admin" and password == "password":
    #         self.app.authenticated = TRUE
    #         self.app.token = {"access_token": "string", "token_type": "bearer"}
    #         self.app.email = email
    #         self.password_var.set("")
    #         self.app.show_tasks_view()
    #     else:
    #         self.create_toast("401 Error", "Bad Credentials")
