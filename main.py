
import os
import shutil

# define parent and target folder
parent_folder = r'/Users/jag_diya/Photos/Dees google photos'
target_folder = r'/Users/jag_diya/Photos/google_photos'
total_files = 0
file_types_available = set()
# To iterate through the root and file name
for root, dirs, files in os.walk(parent_folder, topdown=True):
    # to get the unique file types available in your root folder
    for name in files:
        if "." in name:
            x = [a for a in name.split('.')]
            user = ''.join(x[-1:])
            file_types_available.add(user)
        # To copy all file types
        # total_files += 1
        # sourceFolder = os.path.join(root, name)
        # shutil.copy(sourceFolder, target_folder)
# Copy the files except the once listed below
        avoid = ('.json')
        if not name.endswith(avoid):
            total_files += 1
            sourceFolder = os.path.join(root, name)
            shutil.copy(sourceFolder, target_folder)
# print the file types available
print(file_types_available)
# print the length of the total file types
print(len(file_types_available))
# print total files available
print(f"total files copies are {total_files}")
