import os
import shutil

# Change this path to your folder
folder_path = r"C:\Users\SHIRISHA\Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Organize files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():
            if extension in extensions:
                destination = os.path.join(folder_path, folder)

                if not os.path.exists(destination):
                    os.makedirs(destination)

                shutil.move(file_path, os.path.join(destination, filename))
                print(f"Moved: {filename} → {folder}")
                break

print("File organization completed!")
