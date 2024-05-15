import tkinter as tk
from students import Person
import tkinter.messagebox as messagebox
from db import Database
from ttkbootstrap import Treeview


class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Student Management System')
        self.geometry('400x600')
        self.create_widgets()
        self.database = Database()


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



        #entry fields

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.grid(row=1, column=1, padx=10, pady=10)

        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.grid(row=2, column=1, padx=10, pady=10)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=4, column=1, padx=10, pady=10)



        #button
        btn_add = tk.Button(self, text='add student', command=self.add_student)
        btn_add.grid(row=5, column=0, padx=10, pady=10)

        btn_edit = tk.Button(self, text='edit student', command=self.edit_student)
        btn_edit.grid(row=5, column=1, padx=10, pady=10)

        btn_view = tk.Button(self, text='view student', command=self.view_student)
        btn_view.grid(row=6, column=0, padx=10, pady=10)

        btn_delete = tk.Button(self, text='delet student', command=self.del_student)
        btn_delete.grid(row=6, column=1, padx=10, pady=10)

        btn_clear = tk.Button(self, text='clear student', command=self.clear_entries)
        btn_clear.grid(row=7, column=0, padx=10, pady=10)
    def add_student(self):
        meli = self.entry_id.get()
        first_name =self.entry_first_name.get()
        last_name =self.entry_last_name.get()
        age =self.entry_age.get()
        email = self.entry_email.get()

        if meli and first_name and last_name and email:
            per1 = Person(meli,first_name,last_name,age,email)
            ##messagebox.showinfo('success','student added successfully!')
            self.database.add_student(per1)

            self.clear_entries()

        else:
            messagebox.showwarning('error','please fill in all the fields')


    def edit_student(self):
        pass

    def view_student(self):
        view_window = tk.Toplevel(self)
        view_window.title("view Students")

        #label
        title_label = tk.Label(view_window, text="ALL Students",font=("Arial",16))
        title_label.pack(pady=18)

        #treeview
        student_grid=Treeview(view_window,columns=("meli","first_name","last_name","age","email"),
                              show="headings")
        student_grid.heading("meli",text="Meli code")
        student_grid.heading("first_name", text="First name")
        student_grid.heading("last_name", text="Last Name")
        student_grid.heading("age", text="Age")
        student_grid.heading("email", text="Email")
        student_grid['show'] = 'headings'

        
        #fetch
        students =self.database.get_all_students()

        for student in students:
            student_grid.insert("",tk.END,values=student)

        student_grid.pack(fill=tk.BOTH, expand=True)



    def del_student(self):
        pass

    def clear_entries(self):
        self.entry_id.delete(0,tk.END)
        self.entry_first_name.delete(0,tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
