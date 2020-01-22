import tkinter as tk
from decimal import Decimal
# Account
capital = 1000.00
risk = 0.02

def calculate_result():
    global risk
    global risk_string
    global capital
    global lot_size_string
    global tp_string

    if entry3.get() != risk_string.get():
        risk = entry3.get()
    buy = entry4.get()
    sl = entry5.get()
    if not buy or not sl:
        return None
    elif buy.find('.') <0 or sl.find('.') <0:
        return None

    decimals_buy = len(buy.split('.')[1])
    decimals_sl = len(sl.split('.')[1])
    decimal_points = max(decimals_buy,decimals_sl)

    buy_pips = int(float(buy)*float(Decimal(1).shift(decimal_points)))
    sl_pips = int(float(sl)*float(Decimal(1).shift(decimal_points)))
    pips = abs(buy_pips-sl_pips)
    if not sl_pips:
        return None

    # Lot size
    lot_size = capital * risk / (pips * 10)
    lot_size = round(lot_size,2)
    
    lot_size_string.set(str(lot_size))
    label = tk.Label(main_frame, textvariable = lot_size_string,font=('helvetica',13))
    label.place(x=130,y=250)

    # TP
    tp_pips = buy_pips*2 - sl_pips
    tp = float(tp_pips) / float(Decimal(1).shift(decimal_points))

    tp_string.set(str(tp))
    label2 = tk.Label(main_frame, textvariable = tp_string, font=('helvetica',13))
    label2.place(x=210,y=190)


def clear_entry(event):
    event.widget.delete(0,"end")
    return None
def press_enter(event):
    calculate_result()
    return None
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350+500+250")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH,expand=1)

label1 = tk.Label(main_frame,text="Capital:",font=('helvetica',13))
label1.place(x=70,y=50)
label11= tk.Label(main_frame,text=capital,font=('helvetica',13),fg='grey')
label11.place(x=150,y=50)

label2 = tk.Label(main_frame,text="Trade Calculator",font=('helvetica',20,'bold'),pady=10)
label2.pack(fill=tk.X)

label3 = tk.Label(main_frame,text="risk:",font=('helvetica',13))
label3.place(x=95,y=80)
risk_string = tk.StringVar(main_frame, value=str(int(risk*100))+'%')
entry3= tk.Entry(main_frame,text=risk_string,font=('helvetica',13),fg='grey',width=3)
entry3.bind("<Button-1>",clear_entry)
entry3.place(x=150,y=80)

label4 = tk.Label(main_frame,text='BUY:',font=('helvetica',13))
label5 = tk.Label(main_frame,text='SL:',font=('helvetica',13))
label6 = tk.Label(main_frame,text='TP:',font=('helvetica',13))

label4.place(x=45,y=150)
label5.place(x=58,y=190)
label6.place(x=178,y=190)

entry4 = tk.Entry(main_frame,width=10)
entry4.place(x=90,y=150)
entry4.bind("<Button-1>",clear_entry)
entry4.bind("<Tab>",focus_next_widget)
entry4.bind("<Return>", press_enter)
entry4.focus_set()
entry5 = tk.Entry(main_frame,width=10)
entry5.place(x=90,y=190)
entry5.bind("<Button-1>",clear_entry)
entry5.bind("<Tab>",focus_next_widget)
entry5.bind("<Return>", press_enter)

tp_string = tk.StringVar()
lot_size_string = tk.StringVar()
button = tk.Button(main_frame,command=calculate_result,text='=',bg='green',fg='white',padx=20,pady=20)
button.place(x=215,y=250)
button.bind("<Return>", press_enter)

label7 = tk.Label(main_frame,text='Lot size:',font=('helvetica',13))
label7.place(x=45,y=250)


root.mainloop()
