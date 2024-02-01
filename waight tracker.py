import tkinter as tk
from tkinter import simpledialog, messagebox

class WeightTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Weight Tracker")

        self.names = []
        self.weights_first_day = []
        self.weights_last_day = []

        # Task 1: Entry Screen (Main Screen)
        self.task1_frame = tk.Frame(master)
        tk.Button(self.task1_frame, text="Enter Pupils Data", command=self.task1).pack()
        self.task1_frame.pack()

        # Task 2: Entry Screen
        self.task2_frame = tk.Frame(master)

        # Task 3: Results Screen
        self.task3_frame = tk.Frame(master)

    def task1(self):
        self.task1_frame.pack_forget()  # Hide Task 1 screen
        tk.Label(self.task2_frame, text="Enter Pupil Information on the First Day:").pack()
        self.collect_entries(self.names, self.weights_first_day, task=1)
        tk.Button(self.task2_frame, text="Weights End Term", command=self.task2).pack()
        self.task2_frame.pack()  # Show Task 2 screen

    def task2(self):
        self.task2_frame.pack_forget()  # Hide Task 2 screen
        tk.Label(self.task2_frame, text="Enter New Weights at End of Term:").pack()
        self.collect_entries(self.names, self.weights_last_day, task=2)
        tk.Button(self.task3_frame, text="Calculate Result", command=self.calculate_result).pack()
        self.task3_frame.pack()  # Show Task 3 screen

    def calculate_result(self):
        self.task3_frame.pack_forget()  # Hide Task 3 screen

        # Calculate differences
        congrats_msgs = []
        shame_msgs = []
        msg = []

        for i in range(len(self.names)):
            diff = self.weights_last_day[i] - self.weights_first_day[i]
            status = "Fallen" if diff < -2.5 else "Risen" if diff > 2.5 else "No significant change"

            result_str = f"{self.names[i]}: Difference - {diff:.2f}kg, Status - {status}"

            if abs(diff) >= 2.5:
                if diff >= 2.5:
                    shame_msgs.append(f"{self.names[i]} has gained "+str(diff)+"kg. Shame!")
                elif diff <= -2.5:
                    congrats_msgs.append(f"{self.names[i]} has lost "+str(diff)+"kg. Congratulations!")
            else:
                msg.append(f"{self.names[i]} has weight difference of  "+str(diff)+"kg. no significant change!")

        # Display congratulatory and shaming messages
        message = "\n".join(congrats_msgs + shame_msgs + msg)

        messagebox.showinfo("Results", message)
        self.master.destroy()

    def collect_entries(self, items, weights, task=None):
        entry_frame = tk.Frame(self.master)
        entry_frame.pack()

        for _ in range(30):
            while True:
                try:
                    if task == 1:
                        name = simpledialog.askstring("Input", "Enter Pupil Name:")
                        if name is None:  # User clicked Cancel
                            break

                        if name in items:
                            tk.messagebox.showwarning("Duplicate Name", "Pupil name must be unique.")
                            continue
                        weight = float(tk.simpledialog.askstring("Input", f"Enter {name}'s weight on the first day:"))
                        if weight < 0:
                            raise ValueError("Weight cannot be negative.")

                        items.append(name)
                        weights.append(weight)
                        break
                    if task == 2:
                        name=items[_]
                        weight = float(tk.simpledialog.askstring("Input", f"Enter {name}'s new weight:"))
                        if weight < 0:
                            raise ValueError("Weight cannot be negative.")
                        weights.append(weight)
                        break
                except ValueError as e:
                    tk.messagebox.showerror("Error", f"Invalid input for {name}: {e}")
                    continue

def main():
    root = tk.Tk()
    app = WeightTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
