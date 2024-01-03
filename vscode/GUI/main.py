# import os
# from customtkinter import *
# import shutil

# app = CTk()
# app.geometry("400x400")
# app.title("File Organizer")


# path_entry = CTkEntry(app, font=("Inter-semibold", 30, "bold"), width=300)
# path_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

# def organize():
    
#     path = path_entry.get()
   
#     if path:
#         files = os.listdir(path)
#         for file in files:
#             name, extension = os.path.splitext(file)
#             extension = extension[1:]
#             if not extension:  
#                 continue
#             folder_path = os.path.join(path, extension)
#             if not os.path.exists(folder_path):
#                 os.makedirs(folder_path)
#             shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

# CTkLabel(
#     app,
#     text="File Organizer",
#     font=("Inter-SemiBold", 35),
# ).place(relx=0.5, rely=0.1, anchor=CENTER)

# organize_btn = CTkButton(
#     app,
#     text="Organize",
#     font=("Inter-SemiBold", 30),
#     width=200,
#     height=80,
#     command=organize,
# )
# organize_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

# app.resizable(False, False)
# app.mainloop()


# GUI
