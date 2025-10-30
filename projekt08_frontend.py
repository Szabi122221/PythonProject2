import projekt08_n
import tkinter as tk
from tkinter import messagebox
import requests

def adatkeres():
    try:
        valasz = requests.get("http://127.0.0.1:5000/api/data", timeout=3)
        valasz.raise_for_status()
        adat = valasz.json()
        cimke.config(text=adat["uzenet"])
        app.dobasok_szama_bemenet.set(adat["uzenet"])

    except:
        messagebox.showerror("Hiba", "Nem sikerült a kapcsolat!")

root = tk.Tk()
app = projekt08_n.KockaDobasMentes(root)

api_gomb = tk.Button(root, text="Lekérés", command=adatkeres)
api_gomb.grid(column=0, row=4, pady=10)

cimke = tk.Label(root, text="...")
cimke.grid(column=1, row=4, pady=10)

root.mainloop()