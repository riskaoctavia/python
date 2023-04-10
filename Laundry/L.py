import tkinter as tk
from tkinter import ttk
import pyodbc

# Buat koneksi ke database
server = 'server_name'
database = 'database_name'
username = 'username'
password = 'password'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
cnxn = pyodbc.connect(connection_string)

# Fungsi untuk menampilkan data pelanggan
def show_customers():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    # Bersihkan tampilan
    for widget in data_frame.winfo_children():
        widget.destroy()

    # Tampilkan data pelanggan di tabel
    ttk.Label(data_frame, text="Data Pelanggan", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)
    ttk.Label(data_frame, text="ID").grid(row=1, column=0)
    ttk.Label(data_frame, text="Nama").grid(row=1, column=1)
    ttk.Label(data_frame, text="Alamat").grid(row=1, column=2)
    ttk.Label(data_frame, text="Telepon").grid(row=1, column=3)
    for i, row in enumerate(rows):
        ttk.Label(data_frame, text=row[0]).grid(row=i+2, column=0)
        ttk.Label(data_frame, text=row[1]).grid(row=i+2, column=1)
        ttk.Label(data_frame, text=row[2]).grid(row=i+2, column=2)
        ttk.Label(data_frame, text=row[3]).grid(row=i+2, column=3)

# Fungsi untuk menampilkan data cucian
def show_laundry():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM laundry")
    rows = cursor.fetchall()

    # Bersihkan tampilan
    for widget in data_frame.winfo_children():
        widget.destroy()

    # Tampilkan data cucian di tabel
    ttk.Label(data_frame, text="Data Cucian", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)
    ttk.Label(data_frame, text="ID").grid(row=1, column=0)
    ttk.Label(data_frame, text="Pelanggan").grid(row=1, column=1)
    ttk.Label(data_frame, text="Jenis").grid(row=1, column=2)
    ttk.Label(data_frame, text="Berat (kg)").grid(row=1, column=3)
    ttk.Label(data_frame, text="Harga").grid(row=1, column=4)
    for i, row in enumerate(rows):
        ttk.Label(data_frame, text=row[0]).grid(row=i+2, column=0)
        ttk.Label(data_frame, text=row[1]).grid(row=i+2, column=1)
        ttk.Label(data_frame, text=row[2]).grid(row=i+2, column=2)
        ttk.Label(data_frame, text=row[3]).grid(row=i+2, column=3)
        ttk.Label(data_frame, text=row[4]).grid(row=i+2, column=4)

# Fungsi untuk menampilkan form input data pelanggan
def show_customer_form():
    def save_customer():
        name = name_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        cursor = cnxn.cursor()
        cursor.execute
