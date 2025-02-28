import re
import string
import tkinter as tk
from tkinter import messagebox, ttk

def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special_chars": bool(re.search(r"[!@#$%^&*(),.\":{}|<>]", password))
    }

    strength_score = sum(criteria.values())

    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Include at least one lowercase letter.")
    if not criteria["digits"]:
        feedback.append("Include at least one number.")
    if not criteria["special_chars"]:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    strength_levels = {
        1: ("Very Weak", "#FF0000"),
        2: ("Weak", "#FF4500"),
        3: ("Moderate", "#FFD700"),
        4: ("Strong", "#32CD32"),
        5: ("Very Strong", "#008000"),
    }

    return {
        "strength": strength_levels.get(strength_score, ("Very Weak", "#FF0000")),
        "feedback": feedback if feedback else ["Your password is strong!"]
    }

def toggle_password():
    if entry_password.cget('show') == "*":
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

def check_password():
    password = entry_password.get()
    result = check_password_strength(password)
    
    strength_label.config(text=f"Strength: {result['strength'][0]}", fg=result['strength'][1])
    feedback_text.set("\n".join(result["feedback"]))

def exit_application():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(pady=5)

entry_password = tk.Entry(entry_frame, width=30, show="*", font=("Arial", 12))
entry_password.pack(side=tk.LEFT)

toggle_button = tk.Button(entry_frame, text="Show/Hide", command=toggle_password)
toggle_button.pack(side=tk.RIGHT)

check_button = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_password)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12), bg="#f0f0f0")
strength_label.pack(pady=5)

feedback_text = tk.StringVar()
feedback_label = tk.Label(root, textvariable=feedback_text, font=("Arial", 10), bg="#f0f0f0", wraplength=350)
feedback_label.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=exit_application)
exit_button.pack(pady=10)

root.mainloop()
