


import os
import shutil

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code" : [".html", ".css", ".js", ".json"]
}


def get_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"


def org_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: the folder '{folder_path}' does not exits")
        return
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isdir(file_path):
            continue

        category = get_category(os.path.splitext(file_name)[1])
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(category_folder,file_name))
        print(f"Moved '{file_name}' to '{category}/'. ")
    
def main():
    folder_to_org = input("Enter the folder path to organize: ").strip()
    org_folder(folder_to_org)
    print("Folder Organization Compoleted!!")


if __name__ == "__main__":
    main()


