# Importing necessary libraries
import requests
import json
from tkinter import *
# Setting up authentication credentials
auth_user = 'my_username'
auth_pass = 'my_password'
# Defining window parameters
window = Tk()
window.title("URL Verbose Executor")
window.geometry('450x250')
# Defining labels for the window
lbl_url = Label(window, text="URL:")
lbl_headers = Label(window, text="Headers:")
lbl_body = Label(window, text="Body:")
lbl_response = Label(window, text="Response:")
# Defining input fields for the window
txt_url = Entry(window, width=50)
txt_headers = Entry(window, width=50)
txt_body = Entry(window, width=50)
txt_response = Text(window, width=50, height=10)
# Defining Button to execute request
btn_exec = Button(window, text="Execute", command = lambda: execute_request(txt_url.get(), txt_headers.get(), txt_body.get(), txt_response))
# Placing all elements in the window
lbl_url.grid(column=0, row=0)
txt_url.grid(column=1, row=0)
lbl_headers.grid(column=0, row=1)
txt_headers.grid(column=1, row=1)
lbl_body.grid(column=0, row=2)
txt_body.grid(column=1, row=2)
lbl_response.grid(column=0, row=3)
txt_response.grid(column=1, row=3)
btn_exec.grid(column=1, row=4)
# Defining function to execute request and load response in the text area
def execute_request(url, headers, body, response_field):
    try:
        response = requests.post(url, headers=json.loads(headers), data=json.loads(body), auth=(auth_user, auth_pass))
        response_field.delete('1.0', END)
        response_field.insert(INSERT, response.text)
    except Exception as e:
        response_field.delete('1.0', END)
        response_field.insert(INSERT, 'Error: ' + str(e))


# Executing the window
window.mainloop()