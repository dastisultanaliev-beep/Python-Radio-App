
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Python Quiz App")
app.geometry("390x700")


question = ctk.CTkLabel(
    app,
    text="Which Python data type is immutable?",
    font=("Arial", 15, "bold"),
    wraplength=340
)
question.pack(pady=20)


answer_var = ctk.StringVar(value="")

options = ["list", "dict", "tuple", "set"]

for option in options:
    rb = ctk.CTkRadioButton(
        app,
        text=option,
        variable=answer_var,
        value=option
    )
    rb.pack(anchor="w", padx=80, pady=5)


result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 15)
)
result_label.pack()


question2 = ctk.CTkLabel(
    app,
    text="Which Python data type does not allow duplicate values?",
    font=("Arial", 15, "bold"),
    wraplength=340
)
question2.pack(pady=20)


answer_var2 = ctk.StringVar(value="")

options2 = ["list", "dict", "tuple", "set"]

for option2 in options2:
    rb = ctk.CTkRadioButton(
        app,
        text=option2,
        variable=answer_var2,
        value=option2
    )
    rb.pack(anchor="w", padx=80, pady=5)


result_label2 = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 15)
)
result_label2.pack(pady=20)


def check_answer():
    choice = answer_var.get()

    if choice == "":
        result_label.configure(
            text="Please select an answer!"
        )
    elif choice == "tuple":
        result_label.configure(
            text="Correct! A tuple is immutable."
        )
    else:
        result_label.configure(
            text=f"Incorrect! {choice} is mutable."
        )

    choice2 = answer_var2.get()

    if choice2 == "":
        result_label2.configure(
            text="Please select an answer!"
        )
    elif choice2 == "set":
        result_label2.configure(
            text="Correct! A set does not allow duplicates."
        )
    else:
        result_label2.configure(
            text=f"Incorrect! {choice2} allows duplicate values or keys."
        )


check_button = ctk.CTkButton(
    app,
    text="Check Answers",
    command=check_answer
)
check_button.pack(pady=15)


app.mainloop()
