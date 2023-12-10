


from PIL import Image, ImageDraw
import sys
from flask import Flask, render_template, url_for
from moviepy.editor import *
import random

# imgdraw
seq = []

for _ in range(100):
    img = Image.new('RGB', (500, 300), (125, 125, 125))
    draw = ImageDraw.Draw(img)

    x1 = random.randint(1, 200)
    y1 = random.randint(1, 100)
    x2 = random.randint(251, 497)
    y2 = random.randint(150, 298)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


    draw.rectangle(
    (x1, y1, x2, y2),
    fill=(r, g, b),
    outline=(0, 0, 0))

    img.save(f"static/img{_}.png")
    seq.append(f"static/img{_}.png")

clip = ImageSequenceClip(seq, fps = 10)

clip.write_videofile("static/new_filename.mp4")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

