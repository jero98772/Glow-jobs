import random
from PIL import Image, ImageDraw

def generate_random_image(width, height, num_figures):
    # Create a new blank image with random background color
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    image = Image.new("RGB", (width, height), background_color)
    
    # Draw random figures
    draw = ImageDraw.Draw(image)
    for _ in range(num_figures):
        figure_type = random.choice(["rectangle", "circle", "ellipse"])
        figure_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if figure_type == "rectangle":
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            try:
                draw.rectangle([x1, y1, x2, y2], fill=figure_color)
            except:
                try:
                    draw.rectangle([x2, y2, x1, y1], fill=figure_color)
                except:
                    pass
        elif figure_type == "circle":
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(5, min(width, height) // 4)
            try:
                draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=figure_color)
            except:
                try:
                    radius = random.randint(5, min(width, height) // 4)
                    draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=figure_color)
                except:
                    pass
        elif figure_type == "ellipse":
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            try:
                draw.ellipse([x1, y1, x2, y2], fill=figure_color)
            except:
                try:
                    draw.ellipse([x2, y2, x1, y1], fill=figure_color)
                except:
                    pass

    return image

# Generate a random image with specified width, height, and number of figures
width, height = 800, 600
num_figures = 10
random_image = generate_random_image(width, height, num_figures)

# Save the image
random_image.save("random_image.png")

# Display the image
random_image.show()
