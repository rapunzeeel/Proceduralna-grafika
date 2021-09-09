from PIL import Image


class ReadHeightMap(object):
    def __init__(self):
        self.VBO_coord_color = ()
        self.VBO_scale_color_value = []

    def read_RGB_color(self, parameter):
        if parameter == 0:
            photo = Image.open('GenerationHeight/world1.png')
        else:
            photo = Image.open('GenerationHeight/du.jpg')
        photo = photo.convert('RGB')
        for y in range(0, 60):
            for x in range(0, 60):
                RGB = photo.getpixel((x, y))
                R, G, B = RGB
                self.VBO_coord_color += ((R, G, B),)
                self.scale_RGB_interval(R)
        return self.VBO_scale_color_value

    def scale_RGB_interval(self, color_value):
        scale_color_value = color_value / 255
        self.VBO_scale_color_value.append(scale_color_value)
