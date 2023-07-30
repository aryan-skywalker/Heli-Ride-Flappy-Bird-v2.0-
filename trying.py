from wand.image import Image

# Read image using Image function
with Image(filename='images/back2.png') as img:

    # tinted image using tint() function
    img.tint(color="yellow", alpha="rgb(40 %, 60 %, 80 %)")
    img.save(filename="images/back2night.png")
