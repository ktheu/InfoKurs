import tkinter as tk

class Vorhang:
    def __init__(self, root, transparency=0.5):
        self.root = root
        self.root.title("Vorhang")
        self.root.attributes("-topmost", True)  # Fenster immer oben
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")  # Bildschirmbreite und 300px Höhe
        self.is_dragging = False
        
        # Transparenz einstellen
        self.root.attributes("-alpha", transparency)  # Transparenz auf 50%

        # Canvas für den Vorhang
        self.canvas = tk.Canvas(self.root, bg='grey', height=900, width=self.root.winfo_screenwidth())
        self.canvas.pack()

        # Ereignisse für das Verschieben des Vorhangs
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_click(self, event):
        self.is_dragging = True
        self.click_y = event.y

    def on_drag(self, event):
        if self.is_dragging:
            new_y = event.y - self.click_y
            if new_y < 0: new_y = 0
            if new_y > self.root.winfo_screenheight() - 50: new_y = self.root.winfo_screenheight() - 50
            self.root.geometry(f"{self.root.winfo_screenwidth()}x{new_y+300}+0+0")

    def on_release(self, event):
        self.is_dragging = False

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    vorhang = Vorhang(root, transparency=0.90)  # 50% Transparenz
    vorhang.run()
