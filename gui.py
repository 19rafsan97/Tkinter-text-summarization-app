import tkinter as tk
from news_fetcher import fetch_news
from summarizer import summarize_news

def launch_gui():
    root = tk.Tk()
    root.title("AI News Summarizer")

    text_box = tk.Text(root, wrap="word", width=80, height=25)
    text_box.pack(pady=10)

    def show_news():
        news = fetch_news()
        summaries = summarize_news(news[:5])
        text_box.delete(1.0, tk.END)
        for i, s in enumerate(summaries, 1):
            text_box.insert(tk.END, f"{i}. {s}\n\n")

    button = tk.Button(root, text="Get Today’s News", command=show_news)
    button.pack()

    root.mainloop()
