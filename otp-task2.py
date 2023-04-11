#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import tkinter as tk

# Function to generate OTP and display it in the label
def generate_otp():
    otp = random.randint(100000, 999999)
    otp_label.config(text=f"Your OTP is: {otp}")

# Function to verify OTP
def verify_otp():
    user_otp = int(otp_entry.get())
    if user_otp == int(otp_label.cget("text").split()[-1]):
        result_label.config(text="OTP verification successful!")
    else:
        result_label.config(text="OTP verification failed.")

# Create a tkinter window
window = tk.Tk()
window.title("OTP Verification")

# Create a label to display OTP
otp_label = tk.Label(window, text="Click 'Generate OTP' to get your OTP.")
otp_label.pack(pady=10)

# Create a button to generate OTP
generate_button = tk.Button(window, text="Generate OTP", command=generate_otp)
generate_button.pack(pady=10)

# Create a label and entry for OTP verification
otp_verify_label = tk.Label(window, text="Enter the OTP you received:")
otp_verify_label.pack(pady=10)

otp_entry = tk.Entry(window)
otp_entry.pack(pady=10)

# Create a button to verify OTP
verify_button = tk.Button(window, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

# Create a label to display the result of OTP verification
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the tkinter event loop
window.mainloop()


# In[ ]:




