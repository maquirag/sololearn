from PIL import Image

ASCII = r'█▓▒░'

with Image.open('fairy-tales.jpg', 'r') as image:
    w, h = image.size
    width = 24
    height = int(width * h / w)
    grayscale = image.convert('L').resize((width, height)).getdata()
    # normalize between 0-3
    low, high = min(grayscale), max(grayscale)
    normalized = (int(3.99 * (x-low) / (high-low)) for x in grayscale)
    # convert to ASCII characters
    pixels = '\n'.join(''.join(ASCII[next(normalized)] for _ in range(width)) 
                       for _ in range(height))
    print(pixels)
    