import os


def syn_rename():
    # Path to the 'syn' folder
    syn_folder = 'opencv/data/syn'

    # Get list of subfolders in 'syn' folder
    subfolders = sorted(os.listdir(syn_folder))

    # Iterate over subfolders and rename them
    for i, folder_name in enumerate(subfolders, start=1):
        old_path = os.path.join(syn_folder, folder_name)
        new_name = f'{i:03d}'  # Format the new name with leading zeros
        new_path = os.path.join(syn_folder, new_name)
        os.rename(old_path, new_path)

    print("Subfolders renamed successfully!")


def real_rename():
    # Path to the 'real' folder
    root_folder = 'opencv/data/real'

    # Iterate over subfolders in the 'real' folder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            # Get list of files in the subfolder
            files = sorted(os.listdir(folder_path))

            # Rename the files in the subfolder
            for i, file_name in enumerate(files):
                old_path = os.path.join(folder_path, file_name)
                new_name = f'{i}.jpg'  # Rename files to '0.jpg', '1.jpg', etc.
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)

    print("Images renamed successfully!")


def main():
    real_rename()


if __name__ == '__main__':
    main()
