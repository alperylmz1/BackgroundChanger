import matplotlib.pyplot as plt
import imageio

from src.remover.bg_remover import Remover

if __name__ == "__main__":
    bgremover = Remover(r"C:\Users\alper\Desktop\proj_bg\BackgroundChanger\imgs\dw.jpg")
    plt.imshow(bgremover.image_wo_background())
    plt.show()