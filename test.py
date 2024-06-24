from PIL import Image

# Open an image file
image = Image.open('image.png')

rgb_image = image.convert('RGB')

# Define the area to convert (coordinates of the rectangle)
x1, y1, x2, y2 = 0, 400, 2568, 2100
# x1, y1, x2, y2 = 0, 0, 2568, 200

# Crop the image to the specified area
# cropped_image = rgb_image.crop((x1, y1, x2, y2))

# Display the cropped image

# Define the color to convert (RGB values)
# old_color = [(255, 229, 153), (255, 255, 0)]  # Red color
old_color = [(255, 229, 153), (255, 255, 0)]  # Red color
# old_color = [(43, 120, 0), (43, 120, 228)]  # Red color
new_color = (255, 50, 0)  # Green color

for x in range(x1, x2):
    for y in range(y1, y2):
        pixel = rgb_image.getpixel((x, y))
        if pixel in old_color:
            rgb_image.putpixel((x, y), new_color)

# Display the image with color conversion
rgb_image.show()
rgb_image.save('result_image.jpg')