import cv2
from matplotlib  import pyplot as plt
from scipy.spatial import distance
image_source = cv2.imread('retro.jpg')
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(image_source, cv2.COLOR_BGR2RGB))
    

colors_list = [
    (128, 128, 128),
    (192, 192, 192),
    (255, 255, 255),
    (128, 0, 128),
    (255, 0, 0),
    (255, 255, 0),
    (128, 128, 0),
    (0, 255, 0),
    (0, 128, 0),
    (0, 255, 255),
    (0, 128, 128),
    (0, 0, 255),
    (0, 0, 128),
    (255,184,65),
    (255,202,134),
    (237,118,14),
    (255,189,136),
    (255,130,67),
    (255,136,0),
    (181,184,177),
    (41,49,51),
    (78,87,84),
    (109,101,82),
    (165,165,165),
    (141,145,122),
    (76,81,74),
    (184,183,153),
    (220,220,220),
    (71,74,81),
    (120,71,40),
    (122,88,52),
    (144,103,59)
    

    ]
colors_list = [(i[2], i[1], i[0]) for i in colors_list]

def choose_closest(pixel, colors_list):
    dists = []
    for color in colors_list:
        dists.append(distance.euclidean(color, pixel))
    id_of_closed = dists.index(min(dists))
    return id_of_closed

def quantize_image(image_source, color_palette):
    image_quantized = image_source.copy()
    for i in range(image_source.shape[0]):
        for j in range(image_source.shape[1]):
            closeat_id_in_palette = choose_closest(image_quantized[i,j], color_palette)
            image_quantized[i,j] = color_palette[closeat_id_in_palette]
    return image_quantized
image_source = cv2.imread('retro.jpg')
orig_height, orig_width = image_source.shape[:2]
small_height, small_width = orig_height // 8, orig_width // 8
image_resized =  cv2.resize(image_source, (small_width, small_height), interpolation = cv2.INTER_LINEAR)
image_resized =  cv2.resize(image_resized, (small_width, small_height), interpolation = cv2.INTER_NEAREST)

image_result = quantize_image(image_resized, colors_list)

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(image_result, cv2.COLOR_BGR2RGB))
plt.show()

