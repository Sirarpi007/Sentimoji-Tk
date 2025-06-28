
from textblob import TextBlob
from tkinter import Tk, Label, Entry, Button, Frame

def analyze_sentiment():
    text = entry.get()
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        emoji = "😊 Positive"
        color = "#90EE90"
    elif sentiment < 0:
        emoji = "😞 Negative"
        color = "#FFCCCB"
    else:
        emoji = "😐 Neutral"
        color = "#D3D3D3"

    result_label.config(text=emoji, bg=color)
    root.configure(bg=color)
    root.attributes("-fullscreen", True)

def reset():
    entry.delete(0, 'end')
    result_label.config(text="", bg="white")
    root.configure(bg="white")

root = Tk()
root.title("Sentiment Analyzer")
root.geometry("600x400")
root.configure(bg="white")

title_label = Label(root, text="Sentiment Analyzer", font=("Arial", 24, "bold"), bg="white")
title_label.pack(pady=10)

frame = Frame(root, bg="white")
frame.pack(pady=20)


label = Label(frame, text="Input text:", font=("Arial", 14), bg="white")
label.grid(row=0, column=0, padx=5, pady=5)
entry = Entry(frame, width=40, font=("Arial", 14))
entry.grid(row=0, column=1, padx=5, pady=5)


button_frame = Frame(root, bg="white")
button_frame.pack(pady=10)

analyze_button = Button(button_frame, text="Analyze", font=("Arial", 12), command=analyze_sentiment, bg="#4CAF50", fg="white", width=10)
analyze_button.grid(row=0, column=0, padx=5, pady=5)
reset_button = Button(button_frame, text="Reset", font=("Arial", 12), command=reset, bg="#FF6347", fg="white", width=10)
reset_button.grid(row=0, column=1, padx=5, pady=5)
result_label = Label(root, text="", font=("Arial", 80), bg="white", width=10, height=2)
result_label.pack(pady=20)


root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

root.mainloop()
