#!/usr/bin/env python

import Image
import logging

class dither:

    def __init__ (self):

        # Dithering in C because it is faster
        # https://github.com/migurski/atkinson

        try :
            import atk
            self.has_atk = True
        except Exception, e:
            self.has_atk = False

    def dither_image(self, src_path, dest_path, mime_type):

        if self.has_atk:
            return self.dither_image_atk(src_path, dest_path, mime_type)
            
        return self.dither_image_python(src_path, dest_path, mime_type)

    def dither_image_atk(self, src_path, dest_path, mime_type):

        import atk
        img = Image.open(src_path)
        img = img.convert('L')
        sz = img.size
        
        tmp = atk.atk(sz[0], sz[1], img.tostring())
        new = Image.fromstring('L', sz, tmp)

        new = img.convert('1')
        new.save(dest_path, mime_type)
        return True

    def dither_image_python(self, src_path, dest_path, mime_type):

        img = Image.open(src_path)
        img = img.convert('L')

        threshold = 128*[0] + 128*[255]

        for y in range(img.size[1]):
            for x in range(img.size[0]):

                old = img.getpixel((x, y))
                new = threshold[old]
                err = (old - new) >> 3 # divide by 8
            
                img.putpixel((x, y), new)
        
                for nxy in [(x+1, y), (x+2, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x, y+2)]:
                    try:
                        img.putpixel(nxy, img.getpixel(nxy) + err)
                    except IndexError:
                        pass

        img = img.convert('1')

        img.save(dest_path, mime_type)
        return True

if __name__ == '__main__':

    import sys

    source = sys.argv[1]
    dest = sys.argv[2]

    d = dither()
    d.dither_image(source, dest)

    sys.exit()
