import os
import random

from celery import shared_task
from django.conf import settings
from PIL import Image



@shared_task
def generate_random_image(post_id: int):
    """
    Generate a random image and save it to the specified path.

    Args:
        post_id (int): The id of the post to generate (width, height).
    """
    width, height = random.randint(100, 1000), random.randint(100, 1000)

    # Create a new image with random pixel values
    image = Image.new("RGB", (width, height))

    # Generate random pixel values
    random_pixels = [
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(width * height)
    ]

    # Update the image with the random pixel values
    image.putdata(random_pixels)

    image_path = os.path.join(
        settings.MEDIA_ROOT, "post_media", str(post_id), "random_image.png"
    )

    # Create the directory for the image if it doesn't exist
    image_dir = os.path.dirname(image_path)
    os.makedirs(image_dir, exist_ok=True)

    # Save the image
    image.save(image_path)
    from blogapp.blog.services.post import post_update
    post_update(pk=post_id, data={"thumbnail": image_path})
    return image_path
