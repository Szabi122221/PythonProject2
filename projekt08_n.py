import tkinter as tk
from tkinter import messagebox
import projekt08
import csv
import sqlite3

class KockaDobasMentes(projekt08.KockaDobas):
    def __init__(self, master):
        super().__init__(master)

        self.mentes_txt = tk.Button(master, text="Mentés txt fájlba", command=self.mentes_txtbe)
        self.mentes_txt.grid(row=3, column=0, pady=10)

        self.sql = tk.Button(master, text="Mentés csv fájlba", command=self.mentes_csvbe)
        self.sql.grid(row=3, column=3, pady=10)

        self.mentes_csv = tk.Button(master, text="Mentés sql adatbázisba", command=self.mentes_sql)
        self.mentes_csv.grid(row=3, column=1, pady=10)

    def mentes_sql(self):
        try:
            conn = sqlite3.connect("mentes.db")
            db = conn.cursor()
            db.execute("CREATE TABLE IF NOT EXISTS mentes (dobasok INT, egy INT, ketto INT, harom INT, negy INT, ot INT, hat INT)")
            db.execute("INSERT INTO mentes VALUES (?, ?, ?, ?, ?, ?, ?)", (self.dobasok_szama,
                                                                                        self.eredmenyek[1],
                                                                                        self.eredmenyek[2],
                                                                                        self.eredmenyek[3],
                                                                                        self.eredmenyek[4],
                                                                                        self.eredmenyek[5],
                                                                                        self.eredmenyek[6]))

            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Hiba", "Nem sikerült az SQL-be a mentés!")

    def mentes_csvbe(self):
        fajlnev = "mentes.csv"
        try:
            with open(fajlnev, mode="a", newline="" , encoding="UTF-8") as csvfajl:
                writer = csv.writer(csvfajl)
                writer.writerow([self.dobasok_szama] + [self.eredmenyek[i] for i in range(1, 7)])
                messagebox.showinfo("Mentés", "Sikeres mentés!")
        except:
             messagebox.showerror("Hiba", "Nem sikerült a mentés!")

    def mentes_txtbe(self):
        sor = f"{self.dobasok_szama}, {self.eredmenyek[1]}, {self.eredmenyek[2]}, {self.eredmenyek[3]}, {self.eredmenyek[4]}, {self.eredmenyek[5]}, {self.eredmenyek[6]}\n"
        try:
            with open("mentes.txt", "a", encoding="UTF-8") as fajl:
                fajl.write(sor)
            messagebox.showinfo("Mentés", "Sikeres mentés!")
        except:             
            messagebox.showerror("Hiba", "Nem sikerült a mentés!")


if __name__ == "__main__":
    root = tk.Tk()
    app = KockaDobasMentes(root)
    root.mainloop()
