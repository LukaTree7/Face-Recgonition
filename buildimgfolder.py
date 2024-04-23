import os
import shutil


# Function to rename and move images
def rename_and_move_images(root_folder, output_folder, prefix):
    # Iterate over subfolders in the root folder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            # Get the root folder name ('real' or 'syn')
            root_folder_name = os.path.basename(root_folder)

            # Get list of files in the subfolder
            files = sorted(os.listdir(folder_path))

            # Rename and move the images
            for i, file_name in enumerate(files):
                old_path = os.path.join(folder_path, file_name)
                new_name = f"{i + 1}.{folder_name}{root_folder_name}.jpg"
                new_path = os.path.join(output_folder, new_name)
                shutil.copyfile(old_path, new_path)


# Path to the root folders
real_root_folder = 'opencv/data/real'
syn_root_folder = 'opencv/data/syn'

# Path to the output folder
output_folder = 'opencv/data/fr_2'
os.makedirs(output_folder, exist_ok=True)

# Rename and move images from 'data/real'
rename_and_move_images(real_root_folder, output_folder, 'real')

# Rename and move images from 'data/syn'
rename_and_move_images(syn_root_folder, output_folder, 'syn')

print("Images renamed and moved successfully!")
