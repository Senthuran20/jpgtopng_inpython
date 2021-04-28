import sys
import os
from PIL import Image

#grab first and second arg which is pokedox and new folder

img_folder = sys.argv[1]
output_folder = sys.argv[2]
##print(img_folder, output_folder)
#check if new folder exists,if not create one
print(os.path.exists(output_folder))#retuns false since no new folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through pokedox, convert images to png
for filename in os.listdir(img_folder):
    img=Image.open(f'{img_folder}{filename}')# graing pokedox .since pokedox cannot always be same in various cases
    #{img_folder} is the name of folder containing images since we give slash in cmd no need to mention in code
    #{filename} is the files present in the folder individually
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

#save to new folder