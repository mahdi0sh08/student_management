import tkinter as tk


class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Student Management System')
        self.geometry('500x800')
        self.create_widgets()


    def create_widgets(self):
        #lable
        lbl_id = tk.Label(self,text='meli code:')
        lbl_id.grid(row=0,column=0,padx=10,pady=10)

        lbl_first_name = tk.Label(self, text='first name:')
        lbl_first_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='last name:')
        lbl_last_name.grid(row=2, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text='age')
        lbl_age.grid(row=3, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text='email:')
        lbl_email.grid(row=4, column=0, padx=10, pady=10)


if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
