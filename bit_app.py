from tkinter import *
from tkinter import ttk
import requests
import random
import time


COIN_DELTA_API = 'https://koinex.in/api/ticker'

def web_stat() :
    req = 0
    try :
        req = requests.get(COIN_DELTA_API).status_code
    except Exception:
        pass
    boo = req == 200
    if boo :
        print("Website is online")
    else:
        print("Network / KOINEX error. Site is not reachable")
        quit(1)

web_stat()

def getCoinRate():
    r = requests.get(COIN_DELTA_API)
    url = r.json()
    BTC_PRICE = dict(url['prices'])
    # ETH_PRICE = dict(url['prices'])
    # LTC_PRICE = dict(url['prices'])
    # XRP_PRICE = dict(url['prices'])
    # BCH_PRICE = dict(url['prices'])
    AJV_PRICE = random.randint(200,400)
    # return BTC_PRICE, ETH_PRICE, LTC_PRICE, XRP_PRICE, BCH_PRICE, AJV_PRICE
    return BTC_PRICE, AJV_PRICE

class Application:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Crypto Base");
        self.frame = Frame(parent);
        # self.frame.grid(padx=15, pady=15)
        self.buildHeader()
        self.mainScren_cont()
        self.logo()
        self.frame.pack()
        self.refreshBu()


    def buildHeader(self):
        self.frame_header = Frame(self.frame)
        self.l1 = ttk.Label(self.frame_header, text="CRYPTO MARKET", font=('Helvetica', 12, 'bold'))
        self.l1.pack()
        # self.label_time = tk.Label(self.frame_header, text=self.model.time)
        # self.label_time.pack()
        self.frame_header.grid(row=0, columnspan=3, sticky=(W,E))

    def mainScren_cont(self):
        self.main_frame = Frame(self.frame)
        # self.BTC, self.ETH, self.LTC, self.XRP, self.BCH, self.AJV = getCoinRate();
        self.BTC, self.AJV = getCoinRate()
        self.btc_text = "BTC : ₹" + str(self.BTC['BTC'])
        self.eth_text = "ETH : ₹" + str(self.BTC['ETH'])
        self.ltc_text = "LTC : ₹" + str(self.BTC['LTC'])
        self.xrp_text = "XRP : ₹" + str(self.BTC['XRP'])
        self.bch_text = "BCH : ₹" + str(self.BTC['BCH'])
        self.rand_text = "AJV : ₹" + str(self.AJV)
        self.l3 = ttk.Label(self.main_frame, text=self.btc_text).grid(row=3, column=1, pady=5, sticky=W)
        self.l4 = ttk.Label(self.main_frame, text=self.eth_text).grid(row=4, column=1, pady=5, sticky=W)
        self.l5 = ttk.Label(self.main_frame, text=self.ltc_text).grid(row=5, column=1, pady=5, sticky=W)
        self.l6 = ttk.Label(self.main_frame, text=self.xrp_text).grid(row=6, column=1, pady=5, sticky=W)
        self.l7 = ttk.Label(self.main_frame, text=self.bch_text).grid(row=7, column=1, pady=5, sticky=W)
        self.ra = ttk.Label(self.main_frame, text=self.rand_text).grid(row=8, column=1, pady=5, sticky=W)
        self.main_frame.grid(padx=10, pady=10)


    def logo(self):
        self.logo_frame = Frame(self.frame)
        self.img = PhotoImage(file='C:/Users/ajaydhas/Downloads/bitmacd/bitmacd/logo.gif')
        self.l2 = Label(self.logo_frame, image=self.img); self.l2.image = self.img; self.l2.grid()
        # self.l2.pack();
        self.logo_frame.grid(row=1, column=2, rowspan=5, padx=10, pady=10)

    def refresh(self):
        self.ref.state(['disabled'])
        print("Updating")
        web_stat()
        self.BTC, self.AJV = getCoinRate()
        self.btc_text = "BTC : ₹" + str(self.BTC['BTC'])
        self.eth_text = "ETH : ₹" + str(self.BTC['ETH'])
        self.ltc_text = "LTC : ₹" + str(self.BTC['LTC'])
        self.xrp_text = "XRP : ₹" + str(self.BTC['XRP'])
        self.bch_text = "BCH : ₹" + str(self.BTC['BCH'])
        self.rand_text = "AJV : ₹" + str(self.AJV)
        self.l3 = ttk.Label(self.main_frame, text=self.btc_text).grid(row=3, column=1, pady=5, sticky=W)
        self.l4 = ttk.Label(self.main_frame, text=self.eth_text).grid(row=4, column=1, pady=5, sticky=W)
        self.l5 = ttk.Label(self.main_frame, text=self.ltc_text).grid(row=5, column=1, pady=5, sticky=W)
        self.l6 = ttk.Label(self.main_frame, text=self.xrp_text).grid(row=6, column=1, pady=5, sticky=W)
        self.l7 = ttk.Label(self.main_frame, text=self.bch_text).grid(row=7, column=1, pady=5, sticky=W)
        self.ra = ttk.Label(self.main_frame, text=self.rand_text).grid(row=8, column=1, pady=5, sticky=W)
        self.ref.state(['!disabled'])


    def refreshBu(self):
        self.bottom_Frame = Frame(self.frame)
        self.ref = ttk.Button(self.bottom_Frame, text="Refresh", command=self.refresh)
        self.ref.pack()
        self.bottom_Frame.grid(row=9, columnspan=3, sticky=(W,E), pady=5, padx=5,)



if __name__ == "__main__":
    root = Tk();
    a = Application(root)
    # root.after(1000, a.refresh())
    root.iconbitmap('C:/Users/ajaydhas/Downloads/bitmacd/png/a.png')
    root.mainloop()