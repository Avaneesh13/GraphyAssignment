from math import ceil

from PIL import Image
from celery.decorators import task
from django.conf import settings
from moviepy import editor


@task(name="process_image")
def optimize_image(image_path):
    with Image.open(settings.MEDIA_ROOT + "/" + image_path) as image:
        image_x, image_y = image.size
        if image_x > 1600 or image_y > 1600:
            divisor = max(image_x, image_y) / 1600
            image = image.resize((ceil(image_x / divisor), ceil(image_y / divisor)), Image.ANTIALIAS)
            image.save(settings.MEDIA_ROOT + "/" + image_path)


@task(name="process_video")
def optimize_video(video_path):
    with editor.VideoFileClip(settings.MEDIA_ROOT + "/" + video_path) as video:
        print(video.h, video.w)
        if video.h > 480 or video.w > 640:
            diff_h = video.h - 480
            diff_w = video.w - 640
            if diff_h > diff_w:
                video_resized = video.resize(height=480)
            else:
                video_resized = video.resize(width=640)
            video_resized.write_videofile(settings.MEDIA_ROOT + "/" + video_path)
