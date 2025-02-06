import cv2
import numpy as np
from skimage.measure import label, regionprops
from skimage.color import label2rgb
import matplotlib.pyplot as plt
import sys

input_img = sys.argv[1]

image=cv2.imread(input_img)

height, width, channels = image.shape
#print (height, width, channels)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Initial thresholding
_, binary2 = cv2.threshold(gray, 163,255, cv2.THRESH_BINARY)

# Use morphological open to remove small noise
kernel_open = np.ones((10, 18), np.uint8)
binary2 = cv2.morphologyEx(binary2, cv2.MORPH_OPEN, kernel_open)

# Apply morphological closing to merge split parts
kernel_close = np.ones((3, 5), np.uint8)
binary2 = cv2.morphologyEx(binary2, cv2.MORPH_CLOSE, kernel_close)


label_image = label(binary2)
image_label_overlay = label2rgb(label_image, image=image, bg_label=0)

# Get image dimensions and set up figure for visualization
height, width, _ = image.shape
#fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=72)
#ax.imshow(image_label_overlay)
object_counter = 1
for region in regionprops(label_image):
    if region.area > 500:
        # Get the bounding box coordinates
        minr, minc, maxr, maxc = region.bbox
        object_name = f'0716_Ob {object_counter}'
        object_counter += 1
        #rect = plt.Rectangle((minc, minr), maxc - minc, maxr - minr,
                             fill=False, edgecolor='red', linewidth=0.5)
        #ax.add_patch(rect)
        print(f'{object_name} area: {region.area}')
        #ax.text(minc, minr - 5, f'{object_name}: {region.area}', bbox=dict(facecolor='yellow', alpha=0.5), fontsize=8, color='black')
#ax.set_axis_off()
#plt.savefig('dete.op_0716.jpg', dpi=72, bbox_inches='tight', pad_inches=0)
#plt.show()
