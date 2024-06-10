import func as f

Source_folders = Source_folders = ["А", "Б", "В", "Г"]

def main():
    for Inner_folders in Source_folders:
        new_folder = f.Create_folders(Inner_folders)
        f.Sort(Inner_folders, new_folder)
        f.Remove_and_replace_folders(Inner_folders, new_folder)
        print(f"Папка {Inner_folders} изменена")

if __name__ == "__main__":
    main()
