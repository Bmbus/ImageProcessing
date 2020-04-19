from PIL import Image

img_url = "input.jpg"
img = Image.open(img_url)
img.convert("RGB")
pixels = img.load()
width, height = img.size

def process():
    yellow_pixels = []
    for x in range(width):
       for y in range(height):
           r,g,b = pixels[x, y]
           # SEARCH FOR YELLOW COLORS
           pixel = img.getpixel((x,y))
           #print(pixel)
           if pixel >= (200,200,200): 
               yellow_pixels.append({"color": (r,g,b), "size": (x,y)})
                
    greyscale_img = img.convert("1")
    new_img = Image.new("RGB", greyscale_img.size)
    new_img.paste(greyscale_img)
 
    for data in yellow_pixels:
        new_img.putpixel(data["size"], data["color"])
   
    new_img.save("output.jpg")
    new_img.show()

if __name__ == "__main__":
    process() # SLOW AND Not that closly!