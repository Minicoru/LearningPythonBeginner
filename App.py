import customtkinter as customtkinter
import tkinter as tk
from tkinter import *

class AppController:
    def __init__(self):
        self.data_file = 'data.json'
        self.mongo_client = None
        self.show_login_screen()

    def show_login_screen(self):
        login_screen = tk.Tk()

        # Give the window a title
        login_screen.title("Login Screen")

        # Set window size and position
        login_screen.geometry('400x200+100+100')

        # Create all the widgets
        user_label = tk.Label(login_screen, text="Username:")
        user_label.grid(row=0, column=0)
        user_entry = tk.Entry(login_screen)
        user_entry.grid(row=0, column=1)

        pass_label = tk.Label(login_screen, text="Password:")
        pass_label.grid(row=1, column=0)
        pass_entry = tk.Entry(login_screen, show="*")
        pass_entry.grid(row=1, column=1)

        # Create a login button
        login_btn = tk.Button(login_screen, text="Login", command=lambda: self.show_main_screen(self))
        login_btn.grid(row=2, columnspan=2)

    def show_user_profile_screen(self):

    def show_main_screen(self):
        window = tk.Tk()
        window.title("Main Screen")
        window.geometry("400x400")

        # creating frame
        frame = Frame(window)
        frame.pack()

        # creating label
        label = Label(frame, text="Welcome to the Main Screen")
        label.pack()

        # creating buttons
        button1 = Button(frame, text="User Profile", width=15, command=lambda: self.show_main_screen(self))
        button1.pack()

        button2 = Button(frame, text="Settings", width=15, command=lambda: self.show_main_screen(self))
        button2.pack()

        button3 = Button(frame, text="Activities", width=15, command=lambda: self.show_main_screen(self))
        button3.pack()

    def show_config_screen(self):

    def save_data(self):

    def load_data(self):

    def connect_to_mongo(self):

    def disconnect_from_mongo(self):


app = AppController()
