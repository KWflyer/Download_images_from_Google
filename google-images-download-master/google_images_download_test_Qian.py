from google_images_download import google_images_download   #importing the library
import argparse
import re

parser = argparse.ArgumentParser(description='Download Google Images')
parser.add_argument('--output_directory', default='./downloads',type=str, help= 'root directory')
# parser.add_argument('--image_directory', default='', type=str, help= 'sub-directory')
parser.add_argument('--filename', default='./sketch1_list.txt', type=str, help='File: recording images to be processed')
parser.add_argument('--format', default="png", type=str, help='image format. Note: download images are different when set png or jpg')
parser.add_argument('--limit', default=100, type=int, help='maximum images to download')
parser.add_argument('--size', default=">400*300", type=str, help='required size')

FN = 'download'

def download_images(args, filename):
    f = open(filename, 'r')
    lines = f.readlines()
    print("Open file: %s" % filename)
    print("Total images: %d" % len(lines))
    count = 0
    response = google_images_download.googleimagesdownload()   #class instantiation
    import pdb
    pdb.set_trace()

    for line in lines:
        line = line.strip()
        if re.search('\/', line):
            line = re.sub('\/', '', line)
        # prepare keywords, e.g., replace '_' with ' '
        if re.search('_', line):
            keyword = re.sub('_', ' ', line)
        else:
            keyword = line
        print("Keyword: %s" % keyword)
        # prepare folder names, e.g., replace ' ' with '_'
        if re.search(' ', line):
            folder = re.sub(' ', '_', line)
        else:
            folder = line
        print(folder)
        # args.image_directory = folder
        keywords = keyword + ' white background'
        arguments = {"keywords":keywords,"limit":args.limit,"print_urls":False,"size":args.size,"output_directory":args.output_directory,'image_directory':folder,"format":args.format}   #creating list of arguments
        try:
            paths = response.download(arguments)   #passing the arguments to the function
            count = count + 1
            print("Class %s finished!" % folder)
        except:
            print("Class %s meets a problem!" % folder)
            continue
        # print(paths)   #printing absolute paths of the downloaded images

    return count


def main():
    args = parser.parse_args()

    #==============================================================CHECKS==========================================================================
    #Check if there is a dataset directory entered
    if not args.filename:
        raise ValueError('filename is empty. Please state a filename argument.')

    #==============================================================END OF CHECKS===================================================================
    if FN == 'download':
        count = download_images(args, args.filename)
    else:
        pass

    print("%d classes have been processed" % count)





if __name__ == '__main__':
    main()
