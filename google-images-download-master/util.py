from google_images_download import google_images_download   #importing the library
import argparse
import re
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import glob
import shutil
import string

parser = argparse.ArgumentParser(description='Download Google Images')
parser.add_argument('--src_dir', default='/n/whiskey/xy/vis/qianyu/sbir/data/sketchy/sketchy_composed/photo1/tmp/png/',type=str, help= 'source folder')
parser.add_argument('--dst_dir', default='/n/whiskey/xy/vis/qianyu/sbir/data/sketchy/sketchy_composed/selected/photo/', type=str, help= 'destination folder')
parser.add_argument('--filename', default='/n/whiskey/xy/vis/qianyu/sbir/data/sketchy/sketchy_composed/selected/photo/', type=str, help='File: recording images to be processed')
parser.add_argument('--format', default="png", type=str, help='image format')
parser.add_argument('--limit', default=100, type=int, help='maximum images to download')
parser.add_argument('--size', default=">400*300", type=str, help='required size')

FN = 'check_corrupt' # check_corrupt, move

def check_corrupt(img_dir):
    subfolders = []
    for path, subdirs, files in os.walk(img_dir):
        for name in subdirs:
            subfolders.append(os.path.join(path, name))
    import pdb
    pdb.set_trace()
    for subfolder in subfolders:
        for filename in os.listdir(subfolder):
            try :
                Image.open(subfolder + "/" + filename)
                # Image.open('/n/whiskey/xy/vis/qianyu/sbir/data/sketchy/sketchy_composed/selected/photo/teddy_bear/2.7816106-single-brown-teddy-bear-isolated-on-a-white-background.jpg')
                print('ok')
            except :
                print(subfolder + "/" + filename)
                os.remove(subfolder + "/" + filename)


def move_images(args, list_or_folder):
    """Reads a file or a folder and move specific files to another folder
    """
    if ".txt" in list_or_folder:
        f = open(list_or_folder, 'r')
        lines = f.readlines()
        print("Open file: %s" % list_or_folder)
        print("Total images: %d" % len(lines))
    else:
        subfolders = []
        lines=[]
        for path, subdirs, files in os.walk(list_or_folder):
            for name in subdirs:
                subfolders.append(os.path.join(args.src_dir, name))
        for subfolder in subfolders:
            for f in listdir(subfolder):
                if isfile(os.path.join(subfolder, f)):
                    lines.append(os.path.join(subfolder, f))

        print("Total images: %d" % len(lines))

    # dst_path = '/home/qian/Projects/SimCenter/data/Google_Street_view/images/v2/buildings/binary_classifier/tmp/'
    import pdb
    pdb.set_trace()
    count = 0
    for line in lines:
        # example line: >> Converting image 31/5569 shard 0/home/qian/Projects/SimCenter/data/Google_Street_view/images/v2/buildings_v4/buildings/Soft_Story/515 BROADWAY San_Francisco.jpg
        if re.search('.png', line) is None:
            continue
        a = re.split('\/', line)
        name = a[-2] + '/' + a[-1].strip()
        src = line
        dst = args.dst_dir + name
        try:
            shutil.copy(src, dst)
        except:
            print("There's a problem when copying image %s" % src)
        print("Image %s has be moved to folder %s" % (name, dst))
        count = count + 1

    return count


def main():
    args = parser.parse_args()

    #==============================================================CHECKS==========================================================================
    #Check if there is a dataset directory entered
    if not args.filename:
        raise ValueError('filename is empty. Please state a filename argument.')

    #==============================================================END OF CHECKS===================================================================
    if FN == 'move':
        move_images(args, args.filename)
    elif FN == 'check_corrupt':
        count = check_corrupt(args.filename)
        print("%d classes have been processed" % count)
    #     src_dir = FLAGS.dataset_dir
    #     dst_dir = FLAGS.dst_dir
    #     filename = FLAGS.filename
    #     annotation = FLAGS.annotation
    #     count = split_folder_by_file(filename, annotation, src_dir, dst_dir)
    else:
        pass
    print("Done")







if __name__ == '__main__':
    main()
