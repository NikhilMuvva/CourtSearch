import tkinter as tk
from tkinter import filedialog, messagebox
import csv

def read_csv(file_path):
    cases = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            cases.append(row)
    return cases

def search_case(cases, case_name):
    for case in cases:
        if case_name in case['name'].lower():
            return case
    return None

def search_case_ui():
    global cases
    case_name = case_name_var.get().strip().lower()
    if not case_name:
        messagebox.showwarning("Warning", "Please enter a case name.")
        return
    
    result = search_case(cases, case_name)
    
    if result:
        result_text.set(
            f"Case Name: {result['name']}\n"
            f"Decision: {result['decision.case.disposition']}\n"
            f"Winning Party: {result['decision.winning party']}\n"
            f"LEXIS Citation: {result['citation.lexis']}\n"
        )
    else:
        result_text.set("Case not found.")

def load_csv():
    global cases
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if file_path:
        cases = read_csv(file_path)
        messagebox.showinfo("Info", "CSV file loaded successfully.")
    else:
        messagebox.showwarning("Warning", "No file selected.")

# Initialize the main window
root = tk.Tk()
root.title("Supreme Court Case Search")

tk.Button(root, text="Load CSV File", command=load_csv).pack(pady=10)

tk.Label(root, text="Enter Case Name (lowercase):").pack()
case_name_var = tk.StringVar()
case_name_entry = tk.Entry(root, textvariable=case_name_var, width=50)
case_name_entry.pack(pady=5)

tk.Button(root, text="Search", command=search_case_ui).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify=tk.LEFT).pack(pady=10)

# Start the GUI event loop
root.mainloop()
