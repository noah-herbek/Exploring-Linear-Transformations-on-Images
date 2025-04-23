import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def image_transform(image, a, b, c, d):

    image_np = np.array(image)
    height, width, channels = image_np.shape
    center_x, center_y = width / 2, height / 2
    transformed_image = np.zeros_like(image_np)
    
    linear_transform = np.array([[a, b], [c, d]])  # Create matrix from inputs
    
    for y in range(height):
        for x in range(width):
            # Translate to origin and apply transform
            translated = np.array([x - center_x, -(y - center_y)])
            transformed = linear_transform @ translated
            
            # Translate back and round
            new_x = int(round(transformed[0] + center_x))
            new_y = int(round(-transformed[1] + center_y))
            
            # Copy pixel if within bounds
            if 0 <= new_x < width and 0 <= new_y < height:
                transformed_image[new_y, new_x] = image_np[y, x]
    
    return transformed_image

def showimage(wantedimage):
    plt.imshow(Image.fromarray(wantedimage))
    plt.show()


# Setup
image0 = Image.open("spencer.jpg")
image0_np = np.array(image0)
print(f'The dimension of the image_np is {image0_np.shape}')

"""
#Linear Transformation 1
image1 = image_transform(image0, 1/2, 0, 0, 1/2)
showimage(image1)


#Linear Transformation 2
image2 = image_transform(image0, -3/5, 4/5, 4/5, 3/5)
showimage(image2)


#Linear Transformation 3
image3 = image_transform(image0, 3/5, -4/5, -4/5, -3/5)
showimage(image3)


#Linear Transformation 4
image1 = image_transform(image1, -3/5, 4/5, 4/5, 3/5)
showimage(image1)


#Linear Transformation 5
image3 = image_transform(image3, 3/5, -4/5, -4/5, -3/5)
showimage(image3)
"""
#Linear Transformation 6
image4 = image_transform(image0, 0, 1, 0.5, 1)
showimage(image4)
