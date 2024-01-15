import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req
from json import dumps


class DeliveryPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.address = tb.StringVar()
        self.amount = tb.IntVar()
        self.item = tb.StringVar()

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
        self.top3.pack(side=BOTTOM, ipadx=37, ipady=25)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(side=TOP, ipadx=70, ipady=15)
        tb.Label(self.top3, text="", bootstyle="inverse-primary").pack(side=TOP, ipadx=1, ipady=1, padx=10, pady=2)
        tb.Label(self.top3, text="Menu", bootstyle="inverse-primary", font=('Helvetica', 30)).pack(side=TOP, pady=10)
        self.top4 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top4.pack(side=TOP, pady=10)
        tb.Button(self.top4, text="7$ - Burger", command=self.order_burger, bootstyle=INFO).pack(side=LEFT,
                                                                                          ipady=6,
                                                                                          ipadx=20,
                                                                                          padx=29, pady=10)
        tb.Button(self.top4, text="4$ - Coffee", command=self.order_coffee, bootstyle=INFO).pack(side=RIGHT,
                                                                                          ipady=6,
                                                                                          ipadx=20,
                                                                                          padx=29, pady=10)

        self.bottom5 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom5.pack(expand=True, ipadx=5, ipady=0)
        tb.Label(self.bottom5, text="Address:", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT,
                                                                                                          pady=10)
        tb.Entry(self.bottom5, bootstyle=INFO, textvariable=self.address).pack(side=RIGHT, pady=10)
        self.bottom4 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom4.pack(expand=True, ipadx=56, ipady=0)
        tb.Button(self.bottom4, text="Back", command=self.app.user_page, bootstyle=DANGER).pack(expand=True, ipady=6,
                                                                                                ipadx=80, pady=10)

    def order_burger(self):
        if len(self.address.get()) > 0:
            req.post(f'{self.app.url}items',
                     headers={'Content-Type': 'application/json','Authorization': f'Bearer {self.app.token["access_token"]}'},
                     data=dumps({"address": self.address.get(),"amount_paid": 7,"nice_rating": 1,"order": "Burger"}))
            self.create_toast("Successfully Ordered", "Paid 7$ for a Burger")
        else:
            self.create_toast("401 Error", "Invalid Address")
    def order_coffee(self):
        if len(self.address.get()) > 5:
            req.post(f'{self.app.url}items',
                     headers={'Content-Type': 'application/json','Authorization': f'Bearer {self.app.token["access_token"]}'},
                     data=dumps({"address": self.address.get(),"amount_paid": 4,"nice_rating": 1,"order": "Coffee"}))

            self.create_toast("Successfully Ordered", "Paid 4$ for a Coffee")
        else:
            self.create_toast("401 Error", "Invalid Address")
