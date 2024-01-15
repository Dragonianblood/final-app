import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req

from requests.auth import HTTPBasicAuth

class UserPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.email_var = tb.StringVar()
        self.password_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=WARNING)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=DARK)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=LIGHT)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=5)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=LIGHT)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=5)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(side=BOTTOM, ipadx=81, ipady=0)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(side=TOP, ipadx=75, ipady=0)
        tb.Label(self.top3, text="", bootstyle="inverse-primary").pack(side=TOP, ipadx=1,ipady=1, padx=10, pady=2)
        tb.Button(self.top3, text="Food Delivery",command=self.app.delivery_page, bootstyle=SUCCESS).pack(side=TOP, ipadx=50,ipady=10, pady=20)
        tb.Button(self.top3, text="My Orders",command=self.orders, bootstyle=INFO).pack(side=TOP, ipadx=60,ipady=10, pady=20)
        tb.Button(self.bottom3, text="Account Details",command=self.profile, bootstyle=INFO).pack(side=TOP, ipadx=40,ipady=10, padx=10, pady=20)
        tb.Button(self.bottom3, text="Logout Account",command=self.app.logout, bootstyle=DANGER).pack(side=TOP, ipadx=40,ipady=10, padx=10, pady=20)
        tb.Label(self.bottom3, text="", bootstyle="inverse-primary").pack(side=TOP, ipadx=1,ipady=1, padx=10, pady=2)

    def profile(self):
        profile = req.get(f'{self.app.url}users/me?auth={self.app.token["access_token"]}',
                          headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                   'Content-Type': 'application/json'}).json()
        self.app.views.get('profile_page').name.configure(text=f'Name: {profile["name"]}')
        self.app.views.get('profile_page').nick.configure(text=f'Nickname: {profile["alt_name"]}')
        self.app.views.get('profile_page').email.configure(text=f'Email: {profile["email"]}')
        self.app.profile_page()
    def orders(self):
        items = req.get(f'{self.app.url}items?auth={self.app.token["access_token"]}',
                          headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                   'Content-Type': 'application/json'}).json()
        self.app.views.get('user_orders').page = [0, len(items)-1]
        self.app.views.get('user_orders').orders = items
        if len(items) != 0:
            self.app.views.get('user_orders').order.configure(text=f'Order: {items[0]["order"]}')
            self.app.views.get('user_orders').amount.configure(text=f'Amount Paid: {items[0]["amount_paid"]}')
            self.app.views.get('user_orders').address.configure(text=f'Address: {items[0]["address"]}')
            self.app.views.get('user_orders').date.configure(text=f'Purchased on: {items[0]["ordered_on"][str(items[0]["ordered_on"]).index("T")+1:-10]}')
            self.app.views.get('user_orders').prev_page.configure(bootstyle=SECONDARY, state=["disable"])
            if len(items) > 1:
                self.app.views.get('user_orders').next_page.configure(bootstyle=INFO, state=["!disable"])
            else:
                self.app.views.get('user_orders').next_page.configure(bootstyle=SECONDARY, state=["disable"])
            self.app.user_orders()
        else:
            self.create_toast("401 Error", "No Orders Found")


