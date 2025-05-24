import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

#create main window
root = tk.Tk()
#enlarge gui window size
root.geometry("350x150")
root.title("CSV Column Zero Filter")

#function to show about info
def show_about():
    messagebox.showinfo("about", "CSV Column Zero Filter\nDeveloped by ODAT project.")

#function to process selected file
def process_file(file_path):
    try:
        #read the selected csv file
        df = pd.read_csv(file_path)

        #remove columns where all values except header are 0
        filtered_df = df.loc[:, ~(df.iloc[1:].eq(0).all())]

        #ask where to save filtered file
        save_path = filedialog.asksaveasfilename(
            title="Save Filtered CSV File",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )
        if save_path:
            #save filtered csv
            filtered_df.to_csv(save_path, index=False)
            messagebox.showinfo("success", f"filtered csv saved to: {save_path}")
        else:
            messagebox.showwarning("save cancelled", "no file was saved.")
    except Exception as e:
        #handle errors
        messagebox.showerror("error", f"an error occurred:\n{e}")

#function to select a file
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if file_path:
        process_file(file_path)

#create select file button
btn_select = tk.Button(root, text="Select CSV File", command=select_file)
btn_select.pack(pady=10)

#create about button
btn_about = tk.Button(root, text="About", command=show_about)
btn_about.pack(pady=5)

#start event loop
root.mainloop()
