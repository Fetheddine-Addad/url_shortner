import pyshorteners
import customtkinter as ctk

def shorten_url():
    shortner = pyshorteners.Shortener()
    shortened_url = shortner.tinyurl.short(url_entry.get())
    url_output.delete(1.0, 'end')
    url_output.insert('end', shortened_url)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(url_output.get("1.0", 'end-1c'))
    messagebox("Success", "URL Copied to clipboard")

def messagebox(title, message):
    toplevel = ctk.CTkToplevel(root)
    toplevel.geometry("300x100")   
    toplevel.attributes('-topmost', 'true')
    toplevel.title(title)
    ctk.CTkLabel(toplevel, text=message).pack(padx=10, pady=10)
    ctk.CTkButton(toplevel, text="OK", command=toplevel.destroy, width=10, fg_color="blue").pack(padx=10, pady=10)
    toplevel.focus()

root = ctk.CTk()
root.geometry("400x200")

url_label = ctk.CTkLabel(root, text="Enter URL:")
url_entry = ctk.CTkEntry(root, width=150)
shorten_button = ctk.CTkButton(root, text="Shorten URL", command=shorten_url)
url_output = ctk.CTkTextbox(root, height=1, width=150)
copy_button = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard)



url_label.grid(row=1, column=0,padx=10,pady=20)
url_entry.grid(row=1, column=1,padx=10)
shorten_button.grid(row=1, column=2)
url_output.grid(row=3, column=1,pady=20)
copy_button.grid(row=3, column=2)

root.mainloop()