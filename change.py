from PIL import Image, ImageEnhance

def enhance_pic(image_path):
    image = Image.open(f"{image_path}")

    if image.mode != "RGB":
        image = image.convert("RGB")

    brightness_factor = 1.5 
    enhancer_b = ImageEnhance.Brightness(image)
    bright_img = enhancer_b.enhance(brightness_factor)

    contrast_factor = 1
    enhancer_c = ImageEnhance.Contrast(bright_img)
    final_img = enhancer_c.enhance(contrast_factor)

    final_img.save("pics/result_pillow.png")