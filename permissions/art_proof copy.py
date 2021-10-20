from fpdf import FPDF
import os, sys
import PIL
from PIL import Image
import glob
import os
from os import path

def i_proof(isbn, media_path):
    image_directory=media_path+"/art/upload/"+isbn
    
    if path.exists(image_directory):
        images = 'resized'
        basewidth = 400
        margin = 10
        imagelist=[]
        location=''
        outfile=''
        imagePath=''

        out = 'resized'
        for dirName, subdirList, fileList in os.walk(image_directory):
            for fname in fileList:
                LowerCaseFileName = fname.lower()
                if LowerCaseFileName.endswith(".jpg") or LowerCaseFileName.endswith(".eps") or LowerCaseFileName.endswith(".gif") or LowerCaseFileName.endswith(".png") or LowerCaseFileName.endswith(".tif") or LowerCaseFileName.endswith(".tiff") or LowerCaseFileName.endswith(".jpeg"):
                    imagelist.append(dirName+"/"+fname)
            imagelist1=[]
            for infile in imagelist:
                im = Image.open(os.path.join(image_directory,infile))
                wpercent = (basewidth / float(im.size[0]))
                hsize = int((float(im.size[1]) * float(wpercent)))
                im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
                location = os.path.dirname(infile)
                if not(os.path.exists(os.path.join(location,images))):
                    os.mkdir(os.path.join(location,images))
                outfile = os.path.join(location,images,os.path.splitext(os.path.basename(infile))[0]+".png")
                imagelist1.append(outfile)
                out = im.convert("RGB")
                out.save(outfile, "PNG")

        margin = 30   
        pdf = FPDF('P','mm','A4')
        x,y,w,h = 40,40,200,250
        
        for imagePath in imagelist1:
            pdf.add_page()
            pdf.image(imagePath,10,margin)
            pdf.set_font('Arial', 'B', 12)
            caption=os.path.splitext(os.path.basename(imagePath))[0]
            pdf.cell(10,10, txt=caption)
            os.unlink(imagePath)

        pdf.output(image_directory+"/"+isbn+"_art_proof.pdf","F")

        for dirName, subdirList, fileList in os.walk(image_directory):
            if images in dirName:
                os.rmdir(dirName)
        return "Art proofs generated succesfully! Path: art/upload/{}/{}_art_proof.pdf".format(isbn,isbn)
    else:
        return "Images are not available for ISBN {} inside art/upload folder.".format(isbn)

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    return_val = i_process(arg)
