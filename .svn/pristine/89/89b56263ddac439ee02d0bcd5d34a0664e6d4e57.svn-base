import os, sys
import PIL
from PIL import Image
from fnmatch import fnmatch
import os.path
from os import path
import shutil 

def i_process(isbn, media_path):
    images = 'resized'
    basewidth = 400
    #root=input("Enter folder name:")
    root=media_path+"/documents/"+isbn
    if path.exists(root):
        for infile in os.listdir(root):
            if infile.endswith('.png') or infile.endswith('.tif') or infile.endswith('.jpg') or infile.endswith('.eps')  or infile.endswith('.gif') or infile.endswith('.PNG') or infile.endswith('.TIF') or infile.endswith('.JPG') or infile.endswith('.EPS')  or infile.endswith('.GIF') or infile.endswith('.PDF') or infile.endswith('.pdf'):
                if infile.endswith('.pdf'):
                    #print(infile)
                    inputfile=os.path.join(root,os.path.splitext(infile)[0]+".pdf")
                    #print(inputfile)
                    if not(os.path.exists(os.path.join(root,images))):
                        os.mkdir(os.path.join(root,images))
                    outfile = os.path.join(root,images,os.path.splitext(infile)[0]+".pdf")
                    shutil.copy(inputfile,outfile)
                    
                    print(outfile)
                else:
                    im = Image.open(os.path.join(root,infile))
                    wpercent = (basewidth / float(im.size[0]))
                    hsize = int((float(im.size[1]) * float(wpercent)))
                    im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
                    if not(os.path.exists(os.path.join(root,images))):
                        os.mkdir(os.path.join(root,images))
                    outfile = os.path.join(root,images,os.path.splitext(infile)[0]+".png")
                    out = im.convert("RGB")
                    out.save(outfile, "PNG")
        return "Images processed successfully for ISBN {}".format(isbn)
    else:
        return "Images are not available for ISBN {} inside documents folder.".format(isbn)

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    return_val = i_process(arg)
