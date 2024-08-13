import tkinter as tk
import video_library as lib
import font_manager as fonts

class UpdateVideos:
    def __init__(self, window):
        # Set modern colors similar to Facebook's color scheme
        self.bg_color = "#4267B2"  # Light background color
        self.fg_color = "#1C1E21"  # Dark text color
        self.button_color = "#1877F2"  # Facebook blue
        self.button_hover_color = "#365899"  # Darker blue for hover

        window.geometry("500x200")
        window.title("Update Videos")
        window.configure(bg=self.bg_color)

        # Label and entry field for video number
        self.video_number_label = tk.Label(window, text="Enter Video Number:", bg=self.bg_color, fg=self.fg_color,
                                          font=("Helvetica", 11))
        self.video_number_label.grid(row=0, column=0, padx=10, pady=10)

        self.video_number_entry = tk.Entry(window, width=5, font=("Helvetica", 11), bg="#E9EBEE", fg=self.fg_color, borderwidth=0)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and entry field for new rating
        self.new_rating_label = tk.Label(window, text="Enter New Rating:", bg=self.bg_color, fg=self.fg_color,
                                         font=("Helvetica", 11))
        self.new_rating_label.grid(row=1, column=0, padx=10, pady=10)

        self.new_rating_entry = tk.Entry(window, width=5, font=("Helvetica", 11), bg="#E9EBEE", fg=self.fg_color, borderwidth=0)
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=10)

        # Update button
        self.update_button = tk.Button(window, text="Update Video", command=self.update_video,
                                       bg=self.button_color, fg="#FFFFFF", font=("Helvetica", 11, "bold"),
                                       relief="flat", height=2, width=18, borderwidth=0)
        self.update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.update_button.bind("<Enter>", lambda e: self.on_button_hover(self.update_button))
        self.update_button.bind("<Leave>", lambda e: self.on_button_leave(self.update_button))

        # Status label
        self.status_label = tk.Label(window, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 10))
        self.status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Text box to display the status
        self.status_text = tk.Text(window, height=5, width=40, bg="#E9EBEE", fg=self.fg_color, font=("Helvetica", 11))
        self.status_text.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

    def update_video(self):
        # Get the video number and new rating from the input fields
        video_number = self.video_number_entry.get()
        new_rating = self.new_rating_entry.get()

        # Check if the video number is valid
        video_name = lib.get_name(video_number)
        if video_name is not None:
            # Update the video rating
            lib.set_rating(video_number, new_rating)
            play_count = lib.get_play_count(video_number)
            message = f"Video Name: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
            self.status_text.delete("1.0", tk.END)
            self.status_text.insert(tk.END, message)
        else:
            self.status_text.delete("1.0", tk.END)
            self.status_text.insert(tk.END, f"Video {video_number} not found.")

        # Clear the input fields
        self.video_number_entry.delete(0, tk.END)
        self.new_rating_entry.delete(0, tk.END)

    def on_button_hover(self, button):
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateVideos(window)
    window.mainloop()
