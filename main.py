import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class VirtualAssistant:
    def __init__(self, root, gif_path, size=(100, 100)):
        self.root = root
        self.root.overrideredirect(True)  
        self.root.geometry("+1660+740")  
        self.root.wm_attributes("-transparentcolor", "white")  
        self.root.wm_attributes("-topmost", True)  

        self.gif_image = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(self.fix_transparency(img).resize(size)) for img in ImageSequence.Iterator(self.gif_image)]

        self.avatar_label = tk.Label(self.root, bg="white")
        self.avatar_label.pack()

        self.current_frame = 0

        self.update_gif()

    def fix_transparency(self, img):
        """Corrige a transparência do GIF convertendo a imagem para RGBA se necessário."""
        img = img.convert("RGBA")
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[3] == 0:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        return img

    def update_gif(self):
        frame = self.gif_frames[self.current_frame]
        self.avatar_label.config(image=frame)

        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)

        self.root.after(30, self.update_gif)

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualAssistant(root, "kanna.gif", size=(300, 300))
    root.mainloop()
