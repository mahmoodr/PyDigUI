# PyDigUI - A simple UI for the dig command line tool written in Python
# Author: Mahmood
# Email: mahmoodrm@gmail.com
# Version: 1.0
# GitHub: https://github.com/mahmoodr

import subprocess
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

def run_dig():
    domain = domain_entry.get()
    record_type = record_type_combobox.get()
    dns_server = dns_server_entry.get()
    additional_options = options_entry.get()
    
    if not domain:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a domain name.")
        return

    command = ["dig", domain, record_type]
    
    if dns_server:
        command.extend(["@", dns_server])
    
    if additional_options:
        command.extend(additional_options.split())
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("PyDigUI")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=('Helvetica', 12, 'bold'))
style.configure("TButton", font=('Helvetica', 12))
style.configure("TEntry", font=('Helvetica', 12))
style.configure("TCombobox", font=('Helvetica', 12))

# Create and grid the main frame
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create widgets
ttk.Label(mainframe, text="Domain:").grid(column=1, row=1, sticky=tk.W)
domain_entry = ttk.Entry(mainframe, width=25)
domain_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Record Type:").grid(column=1, row=2, sticky=tk.W)
record_type_combobox = ttk.Combobox(mainframe, values=["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT", "ANY"])
record_type_combobox.grid(column=2, row=2, sticky=(tk.W, tk.E))
record_type_combobox.set("A")

ttk.Label(mainframe, text="DNS Server (optional):").grid(column=1, row=3, sticky=tk.W)
dns_server_entry = ttk.Entry(mainframe, width=25)
dns_server_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Additional Options:").grid(column=1, row=4, sticky=tk.W)
options_entry = ttk.Entry(mainframe, width=25)
options_entry.grid(column=2, row=4, sticky=(tk.W, tk.E))
options_entry.insert(0, "+short")

run_button = ttk.Button(mainframe, text="Run Dig", command=run_dig)
run_button.grid(column=2, row=5, sticky=tk.W, pady=10)

output_label = ttk.Label(mainframe, text="Output:")
output_label.grid(column=1, row=6, sticky=tk.W)

output_text = scrolledtext.ScrolledText(mainframe, width=80, height=20, wrap=tk.WORD, font=('Courier New', 10))
output_text.grid(column=1, row=7, columnspan=2, sticky=(tk.W, tk.E))

# Configure column and row weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.rowconfigure(7, weight=1)

# Start the main loop
root.mainloop()
