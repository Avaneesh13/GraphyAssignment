from math import ceil

from PIL import Image
from celery.decorators import task
from moviepy import editor


@task(name="process_image")
def optimize_image(image_path):
    with Image.open(image_path) as image:
        image_x, image_y = image.size
        if image_x > 600 or image_y > 1200:
            diff_x = image_x - 600
            diff_y = image_y - 1200
            if diff_x > diff_y:
                divisor = image_x / 600
            else:
                divisor = image_x / 1200
            image = image.resize((ceil(image_x / divisor), ceil(image_y / divisor)), Image.ANTIALIAS)
            image.save(image_path)


@task(name="process_video")
def optimize_video(video_path):
    with editor.VideoFileClip(video_path) as video:
        if video.h > 480 or video.w > 640:
            diff_h = video.h - 480
            diff_w = video.w - 640
            if diff_h > diff_w:
                video_resized = video.resize(height=480)
            else:
                video_resized = video.resize(width=640)
            video_resized.write_videofile(video_path)
