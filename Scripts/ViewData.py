import matplotlib.pyplot as plt
import cv2

CLASSES = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', 'Nothing'
]

DATA_PATH = 'OWN'

IMAGE_NAME = input('Image Name - ')

plt.figure(figsize=(40, 30))
plt.rcParams.update({'font.size': 32})
for i in range(0, 27):
    plt.subplot(7, 7, i+1)
    plt.xticks([])
    plt.yticks([])
    path = f"{DATA_PATH}/{CLASSES[i]}/{CLASSES[i]}0.jpg"
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xlabel(CLASSES[i])

plt.savefig(f'{IMAGE_NAME}.png')
