import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req
from json import dumps


class OrdersPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.page: list = []
        self.orders: list = []
        self.create_widgets()

    def create_widgets(self):
        self.pending_address = tb.StringVar()
        self.top1 = tb.Frame(self.frame, bootstyle=INFO)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=DARK)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=LIGHT)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=10, pady=50)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=LIGHT)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=10, pady=50)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(expand=True, ipadx=116)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(expand=True, ipadx=11, ipady=15)
        tb.Label(self.top3, text=f"", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=TOP, pady=1)
        self.order = tb.Label(self.top3, text=f"Order: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.order.pack(side=TOP, pady=10)
        self.amount = tb.Label(self.top3, text=f"Amount Paid: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.amount.pack(side=TOP, pady=10)
        self.top5 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top5.pack(ipadx=0, ipady=0)
        self.address = tb.Label(self.top5, text=f"Address: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.address.pack(expand=True, side=LEFT, pady=10)
        self.create_new_address = tb.Entry(self.top5, bootstyle=INFO, textvariable=self.pending_address)
        self.confirm_new_address = tb.Button(self.top5, text="Confirm", bootstyle=SUCCESS, command=self.confirm_new_address)
        self.date = tb.Label(self.top3, text=f"Purchased on: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.date.pack(side=TOP, pady=10)
        self.top4 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top4.pack(fill=X, ipady=0)
        self.prev_page = tb.Button(self.top4, text="Back", command=self.proceed_to_prev_page, bootstyle=INFO)
        self.prev_page.pack(side=LEFT, ipady=3, pady=15, padx=10, ipadx=17)
        self.next_page = tb.Button(self.top4, text="Next", command=self.proceed_to_next_page, bootstyle=INFO)
        self.next_page.pack(side=RIGHT, ipady=3, pady=15, padx=10, ipadx=20)

        self.bottom4 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom4.pack(expand=True, ipadx=56, ipady=0)
        tb.Button(self.bottom4, text="Back", command=self.app.user_page, bootstyle=DANGER).pack(expand=True,
                                                                                                side=LEFT,
                                                                                                ipady=3,
                                                                                                pady=10,
                                                                                                ipadx=17)
        tb.Button(self.bottom4, text="Edit", command=self.edit_address, bootstyle=SUCCESS).pack(
            expand=True, side=LEFT, ipady=3, pady=10, ipadx=20)
        tb.Button(self.bottom4, text="Delete", command=self.delete_order, bootstyle=DANGER).pack(
            expand=True, side=LEFT, ipady=3, pady=10, ipadx=10)

    def proceed_to_next_page(self):
        self.page[0] += 1
        order = self.orders[self.page[0]]
        self.order.configure(text=f'Order: {order["order"]}')
        self.amount.configure(text=f'Amount Paid: {order["amount_paid"]}$')
        self.address.configure(text=f'Address: {order["address"]}')
        self.date.configure(text=f'Purchased on: {order["ordered_on"][str(order["ordered_on"]).index("T")+1:-10]}')
        if self.page[0] == self.page[1]:
            self.next_page.configure(bootstyle=SECONDARY, state=["disable"])
        if self.page[0] > 0:
            self.prev_page.configure(bootstyle=INFO, state=["!disable"])

    def proceed_to_prev_page(self):
        self.page[0] -= 1
        order = self.orders[self.page[0]]
        self.order.configure(text=f'Order: {order["order"]}')
        self.amount.configure(text=f'Amount Paid: {order["amount_paid"]}$')
        self.address.configure(text=f'Address: {order["address"]}')
        self.date.configure(text=f'Purchased on: {order["ordered_on"][str(order["ordered_on"]).index("T")+1:-10]}')
        if self.page[0] == 0:
            self.prev_page.configure(bootstyle=SECONDARY, state=["disable"])
        if self.page[0] < self.page[1]:
            self.next_page.configure(bootstyle=INFO, state=["!disable"])

    def delete_order(self):
        req.delete(f'{self.app.url}items/{self.orders[self.page[0]]["id"]}',
                     headers={'Content-Type': 'application/json','Authorization': f'Bearer {self.app.token["access_token"]}'})
        self.orders = req.get(f'{self.app.url}items?auth={self.app.token["access_token"]}',
                          headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                   'Content-Type': 'application/json'}).json()
        if len(self.orders) == 0:
            self.app.user_page()
            self.create_toast("401 Error", "No Orders Found")
        if self.page[0] != 0:
            self.proceed_to_prev_page()
        else:
            self.page[0] -= 1
            self.proceed_to_next_page()
        self.page[1] -= 1

    def edit_address(self):
        self.address.configure(text=f'Address: ')
        self.create_new_address.pack(expand=True, side=LEFT)
        self.confirm_new_address.pack(expand=True, side=LEFT, padx=10)

    def confirm_new_address(self):
        self.address.configure(text=f'Address: {self.pending_address.get()}')
        self.create_new_address.pack_forget()
        self.confirm_new_address.pack_forget()
        order = self.orders[self.page[0]-1]
        print(order)
        req.put(f'{self.app.url}items/{order["id"]}',
                     headers={'Content-Type': 'application/json','Authorization': f'Bearer {self.app.token["access_token"]}'},
                     data=dumps({"address": self.pending_address.get(),"amount_paid": order['amount_paid'],"nice_rating": order['nice_rating'],"order": order["order"]}))
