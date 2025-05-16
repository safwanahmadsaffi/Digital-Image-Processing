import cv2
import matplotlib.pyplot as plt

# Read images
gray_image = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread('peppers.png')
color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for proper display

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(color_image)
plt.title('Color Image')
plt.axis('off')

plt.tight_layout()
plt.show()
# Save images 
cv2.imwrite('output_gray_image.png', gray_image)
cv2.imwrite('output_color_image.png', cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR))  # Convert RGB back to BGR for saving