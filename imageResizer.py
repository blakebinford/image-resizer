from PIL import Image
import os
from tqdm import tqdm
import errno
import shutil


print 'Images will be resized to keep aspect ratio\n'
print """Before starting be sure this python file is in
the parent directory of the files you want to resize. Once
started it will create a directory called 'Resized_Images'
that will hold all the resized images.\n"""

width = raw_input('Image Width ')
height = raw_input('Image Height ')

# Variables to find CWD, create relative path to directory for resized files,
# size of image thumbnails.
cwd = os.path.dirname(os.path.abspath(__file__))
size = (width, height)

path = cwd + '\\Resized_Images\\'
print 'Copying file tree and creating needed folders...'
print 'This may take a few minutes...'

try:
    shutil.copytree(cwd, path, ignore=shutil.ignore_patterns('*.py'))
except OSError as e:
    # If the error was caused because the source wasn't a directory
    if e.errno == errno.ENOTDIR:
        shutil.copy(cwd, path)
    else:
        print('Directory not copied. Error: %s' % e)


print 'Starting image resizing.'

# loop over all files and add file and filename to current_files list
for root, dirs, files in os.walk(path):
    for file in tqdm(files):
        current_file = os.path.join(root, file)
        
        try:    
            if os.path.isfile(current_file):
                im = Image.open(current_file)
                filename, extension = os.path.splitext(current_file)
                im.thumbnail(size)
                im.save(current_file)
        except IOError as e:
            continue


