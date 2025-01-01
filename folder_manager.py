import os
import shutil
FOLDER_NAME = "CS"
SOURCE_DIR = "C:/Users/Gilchrist/Desktop"
TARGET_DIR = os.path.join(SOURCE_DIR,FOLDER_NAME)

def move_files():

    folder_name = []
    paths = os.listdir(SOURCE_DIR)
    # List all directories in the source folder
    folder_name = [item for item in paths if os.path.isdir(os.path.join(SOURCE_DIR,item)) and item != FOLDER_NAME]
    print(folder_name)

    # Ensure the target directory exists
    if not os.path.exists(TARGET_DIR):
        print("Folder Does Not Exist\n Creating new Folder...")
        os.makedirs(TARGET_DIR)
        print("Folder Created Successfully... ")
    else:
        # Move each directory to the target folder
        for name in folder_name:
            source_file_path = os.path.join(SOURCE_DIR,name)
            try:
                shutil.move(source_file_path,TARGET_DIR)
                print(f"Moved {name} to {TARGET_DIR}")
            except Exception as e:
                print(f"Failed to move {name}: {e}")




def main():
    move_files()

if __name__ == "__main__":
    main()