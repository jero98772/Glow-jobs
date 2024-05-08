from PIL import Image, ImageDraw

# Create a new blank image with white background
width, height = 400, 300
image = Image.new("RGB", (width, height), "white")

# Draw a red rectangle
draw = ImageDraw.Draw(image)
rectangle = [(100, 100), (300, 200)]
draw.rectangle(rectangle, fill="red")

# Save the image
image.save("generated_image.png")

# Display the image
image.show()
