from flask import Flask, request
import threading
import tkinter as tk
from tkinter import scrolledtext

app = Flask(__name__)
orders = []

# GUI
root = tk.Tk()
root.title("Rimini Kebab Orders")
root.geometry("400x500")
txt = scrolledtext.ScrolledText(root)
txt.pack(expand=True, fill='both')

def update_gui():
    txt.delete('1.0', tk.END)
    for idx, order in enumerate(orders, 1):
        txt.insert(tk.END, f"{idx}. {order['orderNumber']} - {', '.join(order['items'])}\n")
    root.after(1000, update_gui)

update_gui()

# Flask server
@app.route('/order', methods=['POST'])
def receive_order():
    order = request.json
    orders.append(order)
    print("New order:", order)
    return {"status": "ok"}

def run_flask():
    app.run(port=5000)

# Run Flask in a separate thread
threading.Thread(target=run_flask, daemon=True).start()
root.mainloop()
