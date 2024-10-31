import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class VirtualAssistant:
    def __init__(self, root, gif_path, size=(100, 100)):  # Adicionei o parâmetro `size`
        self.root = root
        self.root.overrideredirect(True)  # Remove a borda da janela
        self.root.geometry("+1660+740")   # Define a posição da janela no canto da tela
        self.root.wm_attributes("-transparentcolor", "white")  # Define fundo transparente
        self.root.wm_attributes("-topmost", True)  # Mantém a janela sempre no topo

        # Carrega o GIF animado e redimensiona os frames
        self.gif_image = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(self.fix_transparency(img).resize(size)) for img in ImageSequence.Iterator(self.gif_image)]

        # Exibe o primeiro frame do GIF
        self.avatar_label = tk.Label(self.root, bg="white")
        self.avatar_label.pack()

        # Inicializa o índice do frame atual
        self.current_frame = 0

        # Inicia a animação do GIF
        self.update_gif()

    def fix_transparency(self, img):
        """Corrige a transparência do GIF convertendo a imagem para RGBA se necessário."""
        img = img.convert("RGBA")
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        datas = img.getdata()

        newData = []
        for item in datas:
            # Troca o fundo transparente
            if item[3] == 0:  # Verifica a transparência (canal alfa)
                newData.append((255, 255, 255, 0))  # Cor branca com transparência total
            else:
                newData.append(item)
        img.putdata(newData)
        return img

    def update_gif(self):
        # Atualiza o frame do GIF no label
        frame = self.gif_frames[self.current_frame]
        self.avatar_label.config(image=frame)

        # Avança para o próximo frame
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)

        # Define o tempo de atualização (ex.: 30 milissegundos entre frames)
        self.root.after(30, self.update_gif)

if __name__ == "__main__":
    root = tk.Tk()
    # Passe o tamanho desejado do avatar (ex.: (100, 100) para redimensionar)
    app = VirtualAssistant(root, "kanna.gif", size=(300, 300))  # Ajuste o caminho do GIF e o tamanho aqui
    root.mainloop()
