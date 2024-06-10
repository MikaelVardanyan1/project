import os
import shutil

def Create_folders(base_folder):
    new_dir = f"{base_folder}_new"
    os.makedirs(new_dir, exist_ok=True)
    return new_dir

def Sort(source, destination):
    for subfolder in range(1, 4):
        for image_num in range(1, 4):
            current_file = os.path.join(source, str(subfolder), f"{image_num}")
            new_dir = os.path.join(destination, str(image_num))
            os.makedirs(new_dir, exist_ok=True)

            file_to_copy = current_file + '.jpg' if os.path.isfile(current_file + '.jpg') \
                else current_file + '_.jpg' if os.path.isfile(current_file + '_.jpg') \
                else None

            if file_to_copy:
                destination_file = os.path.join(new_dir, f"{subfolder}.jpg")
                shutil.copy(file_to_copy, destination_file)
                if file_to_copy.endswith('_.jpg'):
                    os.rename(destination_file, destination_file.replace('_.jpg', '.jpg'))

def Remove_and_replace_folders(original, new_structure):
    subfolders_to_remove = [os.path.join(original, str(i)) for i in range(1, 4)]
    for folder in subfolders_to_remove:
        shutil.rmtree(folder)

    for root, dirs, _ in os.walk(new_structure):
        for d in dirs:
            shutil.move(os.path.join(root, d), original)

    shutil.rmtree(new_structure)
