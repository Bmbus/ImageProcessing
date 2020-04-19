from PIL import Image

# GET IMAGE AND ITS DATA
img_url = "input.jpg"
img = Image.open(img_url)
img.convert("RGB")
pixels = img.load()
width, height = img.size



def process():
    # SET PIXELS TO GREYSCALE, EXCEPT THE YELLOW ONES
    yellow_pixels = []
    for x in range(width):
       for y in range(height):
           r,g,b = pixels[x, y]
           # SEARCH FOR YELLOW COLORS
           if r>=200 and g >= 135 and b<140:
               yellow_pixels.append({"color": (r,g,b), "size": (x,y)})
                
    greyscale_img = img.convert("1")
    new_img = Image.new("RGB", greyscale_img.size)
    new_img.paste(greyscale_img)
 
    for data in yellow_pixels:
        new_img.putpixel(data["size"], data["color"])
   
    new_img.save("output.jpg")
    new_img.show()

if __name__ == "__main__":
    process()