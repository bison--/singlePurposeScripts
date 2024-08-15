from tqdm import tqdm
from PIL import Image


def blend_colors(base_pixel, overlay_pixel, alpha=0.5):
    """
    Blends two colors using alpha transparency.

    Parameters:
    - base_pixel: (r, g, b) tuple for the base pixel color.
    - overlay_pixel: (r, g, b) tuple for the overlay pixel color.
    - alpha: float (0.0 to 1.0) transparency of the overlay color.

    Returns:
    - Blended color as an (r, g, b) tuple.
    """
    r_base, g_base, b_base = base_pixel
    r_overlay, g_overlay, b_overlay = overlay_pixel

    r_new = int((1 - alpha) * r_base + alpha * r_overlay)
    g_new = int((1 - alpha) * g_base + alpha * g_overlay)
    b_new = int((1 - alpha) * b_base + alpha * b_overlay)

    return r_new, g_new, b_new


def apply_color(image, color_to_apply):
    for y in range(image.height):
        for x in range(image.width):
            image.putpixel((x, y), blend_colors(image.getpixel((x, y)), color_to_apply))

    return image


image_block_size = 40

original_image = Image.open("temp/hypnotoad116.png")
rescaled_image = original_image.resize((image_block_size, image_block_size), resample=Image.BICUBIC)

target_image = Image.new(
    'RGB',
 (original_image.width * image_block_size, original_image.height * image_block_size),
 (255, 255, 255)
)

for y in tqdm(range(original_image.height)):
    for x in range(original_image.width):
        source_pixel = original_image.getpixel((x, y))

        temp = apply_color(rescaled_image.copy(), source_pixel)

        target_image.paste(temp, (x * image_block_size, y * image_block_size))

target_image.save("output/hypnotoad116_hypnotoad.png")
