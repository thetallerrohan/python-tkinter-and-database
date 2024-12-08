from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import messagebox

def bill():
    # Ensure all fields are filled in
    if a.get() == "" or b.get() == "" or c.get() == "" or e.get() == "" or i.get() == "" or f.get() == "" or j.get() == "" or g.get() == "" or k.get() == "" or h.get() == "" or I.get() == "":
        messagebox.showerror("Error", "Please fill in all details.")
    else:
        # Create PDF with the name provided by the customer
        pdf = a.get() + ".pdf"
        c11 = canvas.Canvas(pdf)
        
        # Add customer details to the PDF
        c11.drawString(50, 800, "Customer Name: " + a.get())
        c11.drawString(50, 780, "Mobile Number: " + b.get())
        c11.drawString(50, 760, "Email: " + c.get())
        
        # Football orders
        c11.drawString(50, 740, "Jabulani - Quantity: " + e.get() + "   Price: " + i.get())
        c11.drawString(50, 720, "La Liga - Quantity: " + f.get() + "   Price: " + j.get())
        c11.drawString(50, 700, "PL - Quantity: " + g.get() + "   Price: " + k.get())
        c11.drawString(50, 680, "League 1 - Quantity: " + h.get() + "   Price: " + I.get())
        
        # Add the total price to the PDF
        c11.drawString(50, 660, "Total: " + total.get())
        
        # Save the PDF file
        c11.save()

def totall():
    # Get the quantities and prices for each item, ensure they're integers, and calculate the total.
    try:
        # Get input values
        jabulani_qty = int(e.get())
        jabulani_price = float(i.get())
        la_liga_qty = int(f.get())
        la_liga_price = float(j.get())
        pl_qty = int(g.get())
        pl_price = float(k.get())
        league1_qty = int(h.get())
        league1_price = float(I.get())

        # Calculate total cost
        total_cost = (jabulani_qty * jabulani_price) + (la_liga_qty * la_liga_price) + \
                     (pl_qty * pl_price) + (league1_qty * league1_price)

        # Update total Entry widget with the result
        total.delete(0, END)  # Clear any previous value
        total.insert(0, f"{total_cost:.2f}")  # Set the calculated total with 2 decimal places

    except ValueError:
        # Handle case where user doesn't input a valid number
        messagebox.showerror("Input Error", "Please enter valid numbers for quantities and prices.")
        total.delete(0, END)
        total.insert(0, "0.00")  # Reset total value to 0.00 if there's an error

# Setting up the Tkinter window
root = Tk()
root.title("Football Order")

# Customer details
l1 = Label(root, text="Name")
l1.grid(row=0, column=0)
a = Entry(root)
a.grid(row=0, column=1)

l2 = Label(root, text="Email")
l2.grid(row=1, column=0)
b = Entry(root)
b.grid(row=1, column=1)

l3 = Label(root, text="Phone Number")
l3.grid(row=2, column=0)
c = Entry(root)
c.grid(row=2, column=1)

l4 = Label(root, text="Type of Football")
l4.grid(row=3, column=0)
d = Entry(root)
d.grid(row=3, column=1)

# Football items and their quantities and prices
l5 = Label(root, text="Jabulani")
l5.grid(row=4, column=0)
e = Entry(root)
e.grid(row=4, column=1)
i = Entry(root)
i.grid(row=4, column=2)

l6 = Label(root, text="La Liga")
l6.grid(row=5, column=0)
f = Entry(root)
f.grid(row=5, column=1)
j = Entry(root)
j.grid(row=5, column=2)

l7 = Label(root, text="PL")
l7.grid(row=6, column=0)
g = Entry(root)
g.grid(row=6, column=1)
k = Entry(root)
k.grid(row=6, column=2)

l8 = Label(root, text="League 1")
l8.grid(row=7, column=0)
h = Entry(root)
h.grid(row=7, column=1)
I = Entry(root)
I.grid(row=7, column=2)

# Buttons for Total and Generate Bill
b1 = Button(root, text="Calculate Total", command=totall)
b1.grid(row=8, column=0)

# Total Entry widget to show calculated total
total = Entry(root)
total.grid(row=8, column=1)
total.insert(0, "0.00")  # Initialize with 0.00

b2 = Button(root, text="Generate Bill", command=bill)
b2.grid(row=9, column=0)

root.mainloop()