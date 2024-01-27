import tkinter as tk
from tkinter import ttk, StringVar, END, messagebox
import pandas as pd

class HotelManagementHome:
    def _init_(self, root):
        self.root = root
        self.root.title("Hotel Management Home")
        self.root.geometry("600x500")
        self.root.config(bg="#f2f2f2")
        self.root.resizable(False, False)

        font1 = ("Arial", 20, "bold")

        self.title_label = tk.Label(self.root, text="Welcome to Hotel Management System", font=font1, bg="#f2f2f2", fg="#333")
        self.title_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.enter_button = tk.Button(self.root, text="Enter", font=("Arial", 14), command=self.open_management_app,
                                      bg="#CDAA7D", fg="#fff", cursor="hand2", width=10, borderwidth=3, relief=tk.RAISED)
        self.enter_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_management_app(self):
        self.root.destroy()
        app = tk.Tk()
        HotelManagementApp(app)
        app.mainloop()

class HotelManagement:
    def _init_(self, category, name, reservation, status):
        self.category = category
        self.name = name
        self.reservation = reservation
        self.status = status
        self.next = None

class HotelManagementList:
    def _init_(self):
        self.head = None

    def addEntry(self, entry):
        if not self.head:
            self.head = entry
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = entry

    def removeEntry(self, name):
        temp = self.head
        if temp and temp.name == name:
            self.head = temp.next
            return
        prev = None
        while temp and temp.name != name:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def updateEntry(self, new_category, new_reservation, new_status, name):
        temp = self.head
        while temp and temp.name != name:
            temp = temp.next
        if temp:
            temp.category = new_category
            temp.reservation = new_reservation
            temp.status = new_status

    def findEntry(self, name):
        temp = self.head
        while temp and temp.name != name:
            temp = temp.next
        return temp


class HotelManagementApp:
    def _init_(self, root):
        self.entryList = HotelManagementList()
        self.load_data_from_csv()

        root.title("Hotel Management System")
        root.geometry("600x500")
        root.config(bg="#f2f2f2")
        root.resizable(False, False)

        font1 = ("Arial", 12)
        font2 = ("Arial", 20, "bold")

        Title_label = tk.Label(root, font=font2, text="HOTEL MANAGEMENT SYSTEM", fg="#333", bg="#f2f2f2")
        Title_label.place(x=90, y=20)

        category_label = tk.Label(root, font=font1, text="Category", fg="#333", bg="#f2f2f2")
        category_label.place(x=20, y=80)

        category_options = ["Studio", "Deluxe", "Presidential Suite", "Single", "Double", "Penthouse"]
        self.category_variable = StringVar()
        self.category_variable.set("Deluxe")
        category_menu = ttk.Combobox(root, font=font1, textvariable=self.category_variable, values=category_options, state="readonly")
        category_menu.place(x=130, y=80)

        name_label = tk.Label(root, font=font1, text="Name", fg="#333", bg="#f2f2f2")
        name_label.place(x=20, y=140)

        self.name_entry = tk.Entry(root, font=font1, fg="#333", bg="#fff", bd=2, width=22)
        self.name_entry.place(x=130, y=140)

        reservation_label = tk.Label(root, font=font1, text="Reservation", fg="#333", bg="#f2f2f2")
        reservation_label.place(x=20, y=260)

        reservation_options = ["1 Day", "2 Days", "3 Days", "4 Days", "5 Days", "6 Days", "1 Week", "Check Out Day"]
        self.reservation_variable = StringVar()
        self.reservation_variable.set("1 Day")
        reservation_menu = ttk.Combobox(root, font=font1, textvariable=self.reservation_variable, values=reservation_options, state="readonly")
        reservation_menu.place(x=130, y=260)

        status_label = tk.Label(root, font=font1, text="Status", fg="#333", bg="#f2f2f2")
        status_label.place(x=20, y=200)

        status_options = ["Check In", "Check Out"]
        self.status_variable = StringVar()
        self.status_variable.set("Check In")
        status_menu = ttk.Combobox(root, font=font1, textvariable=self.status_variable, values=status_options, state="readonly")
        status_menu.place(x=130, y=200)

        add_button = tk.Button(root, command=self.addEntry, font=font1, text="Add Entry", fg="#fff",
                               bg="#CDAA7D", cursor="hand2", width=18, borderwidth=3, relief=tk.RAISED)
        add_button.place(x=380, y=80)

        new_button = tk.Button(root, command=self.clearEntries, font=font1, text="Clear", fg="#fff",
                               bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=25, borderwidth=3)
        new_button.place(x=20, y=320)

        update_button = tk.Button(root, command=self.updateEntry, font=font1, text="Update Entry", fg="#fff",
                                  bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=18, borderwidth=3)
        update_button.place(x=380, y=200)

        delete_button = tk.Button(root, command=self.deleteSelectedEntry, font=font1, text="Delete Entry", fg="#fff",
                                  bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=18, borderwidth=3)
        delete_button.place(x=380, y=260)

        search_button = tk.Button(root, command=self.searchEntry, font=font1, text="Search Entry", fg="#fff",
                                  bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=25, borderwidth=3)
        search_button.place(x=310, y=320)

        view_all_button = tk.Button(root, command=self.view_all_entries, text="View All", font=font1,
                                    fg="#fff", bg="#CDAA7D", cursor="hand2", width=18, borderwidth=3, relief=tk.RAISED)
        view_all_button.place(x=380, y=140)


    def clearEntries(self):
        self.category_variable.set("Deluxe")
        self.name_entry.delete(0, END)
        self.reservation_variable.set("1 Day")
        self.status_variable.set("Check In")

    def addEntry(self):
        category = self.category_variable.get()
        name = self.name_entry.get()
        reservation = self.reservation_variable.get()
        status = self.status_variable.get()

        if not (category and name and reservation and status):
            messagebox.showerror("Error", "Enter all fields.")
        else:
            newEntry = HotelManagement(category, name, reservation, status)
            self.entryList.addEntry(newEntry)
            self.clearEntries()
            messagebox.showinfo("Success", "Entry data has been added.")
            self.save_data_to_csv()

    def deleteSelectedEntry(self):
        selected_item = self.entryList.findEntry(self.name_entry.get())
        if not selected_item:
            messagebox.showerror("Error", "Choose an Entry to delete.")
        else:
            EntryName = selected_item.name
            self.entryList.removeEntry(EntryName)
            self.clearEntries()
            messagebox.showinfo("Success", "Entry data has been deleted.")
            self.save_data_to_csv()

    def updateEntry(self):
        name_to_update = self.name_entry.get()
        if not name_to_update:
            messagebox.showerror("Error", "Enter a name to search for the entry.")
        else:
            selected_item = self.entryList.findEntry(name_to_update)
            if not selected_item:
                messagebox.showerror("Error", f"No entry found with the name: {name_to_update}.")
            else:
                self.category_variable.set(selected_item.category)
                self.name_entry.delete(0, END)
                self.name_entry.insert(0, selected_item.name)
                self.reservation_variable.set(selected_item.reservation)
                self.status_variable.set(selected_item.status)
                messagebox.showinfo("Success", f"Entry with the name '{name_to_update}' is ready for update.")
                self.save_data_to_csv()

    def searchEntry(self):
        name_to_search = self.name_entry.get()
        if not name_to_search:
            messagebox.showerror("Error", "Enter a name to search for the entry.")
        else:
            matching_entries = self.get_matching_entries(name_to_search)
            self.display_search_results(matching_entries, name_to_search)

    def get_matching_entries(self, name):
        matching_entries = []
        temp = self.entryList.head
        while temp:
            if temp.name.lower() == name.lower():
                matching_entries.append(temp)
            temp = temp.next
        return matching_entries

    def display_search_results(self, matching_entries, name_to_search):
        search_results_window = tk.Toplevel()
        search_results_window.title("Search Results")
        search_results_window.title("All Entries")
        search_results_window.geometry("600x500")
        search_results_window.config(bg="#f2f2f2")
        search_results_window.resizable(False, False)


        search_results_label = tk.Label(search_results_window, text=f"Search Results for '{name_to_search}'", font=("Arial", 16, "bold"))
        search_results_label.pack()

        if not matching_entries:
            no_results_label = tk.Label(search_results_window, text="No matching entries found.", font=("Arial", 12))
            no_results_label.pack()
        else:
            for entry in matching_entries:
                entry_label = tk.Label(search_results_window, text=f"{entry.category} - {entry.name} - {entry.reservation} - {entry.status}")
                entry_label.pack()

    def load_data_from_csv(self):
        try:
            df = pd.read_csv("hotel_data.csv")
            for index, row in df.iterrows():
                new_entry = HotelManagement(
                    row['Category'], row['Entry Name'], row['Reservation'], row['Status']
                )
                self.entryList.addEntry(new_entry)
        except FileNotFoundError:
            pass

    def save_data_to_csv(self):
        data = {
            'Category': [],
            'Entry Name': [],
            'Reservation': [],
            'Status': []
        }

        temp = self.entryList.head
        while temp:
            data['Category'].append(temp.category)
            data['Entry Name'].append(temp.name)
            data['Reservation'].append(temp.reservation)
            data['Status'].append(temp.status)
            temp = temp.next

        df = pd.DataFrame(data)
        df.to_csv("hotel_data.csv", index=False)

    def view_all_entries(self):
        view_all_window = tk.Toplevel()
        view_all_window.title("All Entries")
        view_all_window.geometry("600x500")
        view_all_window.config(bg="#f2f2f2")
        view_all_window.resizable(False, False)

        all_entries_label = tk.Label(view_all_window, text="All Entries", font=("Arial", 20, "bold"))
        all_entries_label.pack()

        entries = []
        temp = self.entryList.head
        while temp:
            entries.append(temp)
            temp = temp.next

        n = len(entries)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if entries[j].name < entries[min_index].name:
                    min_index = j
            entries[i], entries[min_index] = entries[min_index], entries[i]

        for entry in entries:
            entry_label = tk.Label(
                view_all_window,
                text=f"{entry.name.ljust(30)} {entry.category.ljust(30)} {entry.reservation.ljust(30)} {entry.status.ljust(30)}",
                anchor="w"  # Set anchor to left (west)
            )
            entry_label.pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    HotelManagementHome(root)
    root.mainloop()