import os
import shutil

# Path to the 'real' folder
root_folder = 'opencv/data/real'

# Iterate over subfolders in the 'real' folder
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        # Check if subfolder name is numeric (like '001', '002', etc.)
        if folder_name.isdigit():
            frontal_folder = os.path.join(folder_path, 'frontal')
            if os.path.exists(frontal_folder):
                # Get list of files in 'frontal' folder
                frontal_files = os.listdir(frontal_folder)
                frontal_files.sort()  # Sort files to ensure consistency

                # Create a new folder to save the selected images
                save_folder = os.path.join(root_folder, folder_name)
                os.makedirs(save_folder, exist_ok=True)

                # Copy the first five images to the new folder
                for i in range(min(5, len(frontal_files))):
                    file_name = frontal_files[i]
                    src_path = os.path.join(frontal_folder, file_name)
                    dest_path = os.path.join(save_folder, file_name)
                    shutil.copyfile(src_path, dest_path)
                
                # Remove original subfolders
                shutil.rmtree(os.path.join(folder_path, 'frontal'))
                shutil.rmtree(os.path.join(folder_path, 'profile'))
                shutil.rmtree(os.path.join(folder_path, 'selected_images'))

print("Images copied and original subfolders removed successfully!")
