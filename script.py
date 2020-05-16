from PIL import Image
import os
from os import listdir
from os.path import isfile, join


directory_path = os.path.dirname(os.path.realpath(__file__))


def remove_extension(image_with_extenxion):
    ans , extension = image_with_extenxion.split('.')
    return ans

def get_files():
    path = '{}/images_to_pixelate'.format(os.path.dirname(os.path.realpath(__file__)))
    # get all images name with their extensions ex(.png , .jpeg , .JPG)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    files_to_pixelate = {}
    for filename in onlyfiles:
        ans = '{}/{}'.format(path, filename)
        files_to_pixelate[filename]=ans
    return files_to_pixelate


# main function
if __name__ == '__main__':
    for image_file,path_to_file in get_files().items():
        print(image_file)
        img = Image.open(path_to_file)
        height, width = img.size

        # Resize smoothly down to h/6,w/g pixels
        imgSmall = img.resize((height//6,width//6), resample=Image.BILINEAR)

        # Scale back up using NEAREST to original size
        result = imgSmall.resize(img.size, Image.NEAREST)

        filename = '{}/result/pixelated_{}.png'.format(directory_path, remove_extension(image_file))
        result.save(filename)
        print('File {} pixelated successfully into {}'.format(remove_extension(image_file), filename))