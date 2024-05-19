import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from file_manager import FileManager


class GUIFileManager:
    def __init__(self, root, file_manager):
        self.file_manager = file_manager
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("650x900")
        self.create_widgets()
        self.root.resizable(False, False)
        self.center_window()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - self.root.winfo_reqwidth()) // 3
        y = (screen_height - self.root.winfo_reqheight()) // 4

        self.root.geometry("+{}+{}".format(x, y))
        self.root.update_idletasks()

    def create_widgets(self):
        frame_border = tk.Frame(self.root, relief=tk.GROOVE, borderwidth=10)
        frame_border.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.menu_frame = tk.Frame(frame_border)
        self.menu_frame.pack(padx=10, pady=10)

        options = [
            "Создать файл", "Копировать файл", "Удалить файл", "Переместить файл",
            "Архивировать файлы", "Разархивировать файлы", "Создать резервную копию файлов",
            "Управление правами доступа к файлу", "Изменить содержимое файла",
            "Изменить базовую папку", "Переместить на другой диск", "Вывести информацию о файле",
            "Создать папку"
        ]

        button_width = 40
        button_height = 1

        for idx, option in enumerate(options, start=1):
            button = tk.Button(
                self.menu_frame,
                bg='#4B0082',
                fg='white',
                font=('Helvetica', 15, 'bold'),
                text=option,
                relief='raised',
                bd=5,
                command=lambda index=idx: self.handle_option(index),
                width=button_width,
                height=button_height
            )
            button.pack(fill='x', pady=6)

        exit_button = tk.Button(
            self.menu_frame,
            text="Выйти",
            command=self.root.quit,
            bg='#4B0082',
            fg='red',
            font=('Helvetica', 15, 'bold'),
            width=button_width,
            height=button_height,
            relief='raised',
            bd=5
        )
        exit_button.pack(fill='x', pady=6)

    def handle_option(self, option):
        if option == 1:
            new_file_name = simpledialog.askstring("Создать файл", "Введите имя файла:")
            file_content = simpledialog.askstring("Создать файл", "Введите содержимое файла:")

            self.file_manager.create_file(new_file_name, file_content)
        elif option == 2:
            source_file = filedialog.askopenfilename(title="Выберите исходный файл")
            destination_file = filedialog.asksaveasfilename(title="Выберите целевой файл")
            self.file_manager.copy_file(source_file, destination_file)
        elif option == 3:
            file_to_delete = filedialog.askopenfilename(title="Выберите файл для удаления")
            self.file_manager.delete_file(file_to_delete)
        elif option == 4:
            source_file = filedialog.askopenfilename(title="Выберите исходный файл")
            destination_folder = filedialog.askdirectory(title="Выберите целевую папку")
            self.file_manager.move_file(source_file, destination_folder)
        elif option == 5:
            files_to_archive = filedialog.askopenfilenames(title="Выберите файлы для архивации")
            archive_filename = filedialog.asksaveasfilename(title="Введите имя архива")
            self.file_manager.archive_files(files_to_archive, archive_filename)
        elif option == 6:
            archive_filename = filedialog.askopenfilename(title="Выберите архив для разархивации")
            extraction_folder = filedialog.askdirectory(title="Выберите папку для разархивации")
            self.file_manager.extract_archive(archive_filename, extraction_folder)
        elif option == 7:
            files_to_backup = filedialog.askopenfilenames(title="Выберите файлы для резервного копирования")
            backup_folder = filedialog.askdirectory(title="Выберите папку для резервного копирования")
            self.file_manager.backup_files(files_to_backup, backup_folder)
        elif option == 8:
            file_to_manage = filedialog.askopenfilename(title="Выберите файл для управления правами доступа")
            access_choice = simpledialog.askstring("Управление правами доступа", "Выберите права доступа:\n1. Только чтение (r)\n2. Чтение и запись (w)\nВведите номер права доступа:")
            self.file_manager.manage_file_permissions(file_to_manage, access_choice)
        elif option == 9:
            file_to_edit = filedialog.askopenfilename(title="Выберите файл для изменения содержимого")
            new_content = simpledialog.askstring("Изменить содержимое файла", "Введите новое содержимое файла:")
            self.file_manager.edit_file_content(file_to_edit, new_content)
        elif option == 10:
            new_base_folder = filedialog.askdirectory(title="Выберите новый путь к базовой папке")
            self.file_manager.change_base_folder(new_base_folder)
        elif option == 11:
            source_file = filedialog.askopenfilename(title="Выберите файл для перемещения")
            destination_disk = simpledialog.askstring("Переместить на другой диск", "Введите букву диска (пример: D:)")
            self.file_manager.move_to_another_disk(source_file, destination_disk)
        elif option == 12:
            file_to_inspect = filedialog.askopenfilename(title="Выберите файл для получения информации")
            file_info_result = self.file_manager.file_info(file_to_inspect)
            messagebox.showinfo("Информация о файле", file_info_result)
        elif option == 13:
            new_folder_name = simpledialog.askstring("Создать папку", "Введите имя новой папки")
            self.file_manager.create_folder(new_folder_name)


def main_menu():
    file_manager = FileManager(base_folder="C:\\Users\\User\\OneDrive\\Рабочий стол\\82\\PPOIS_python\\lab1")

    choice = input("Выберите интерфейс (1 - cli; 2- gui): ").strip().lower()

    if choice == '1':
        while True:
            print("\nМеню:")
            print("1. Создать файл")
            print("2. Копировать файл")
            print("3. Удалить файл")
            print("4. Переместить файл")
            print("5. Архивировать файлы")
            print("6. Разархивировать файлы")
            print("7. Создать резервную копию файлов")
            print("8. Управление правами доступа к файлу")
            print("9. Изменить содержимое файла")
            print("10. Изменить базовую папку")
            print("11. Переместить на другой диск")
            print("12. Вывести информацию о файле")
            print("13. Создать папку")
            print("0. Выйти")

            user_choice = input("Выберите операцию (введите номер): ")

            if user_choice == '1':
                new_file_name = input("Введите имя файла: ")
                file_content = input("Введите содержимое файла: ")
                file_manager.create_file(new_file_name, file_content)
            elif user_choice == '2':
                source_file = input("Введите имя исходного файла: ")
                destination_file = input("Введите имя целевого файла: ")
                file_manager.copy_file(source_file, destination_file)
            elif user_choice == '3':
                file_to_delete = input("Введите имя файла для удаления: ")
                file_manager.delete_file(file_to_delete)
            elif user_choice == '4':
                source_file = input("Введите имя исходного файла: ")
                destination_folder = input("Введите имя целевой папки: ")
                file_manager.move_file(source_file, destination_folder)
            elif user_choice == '5':
                files_to_archive = input("Введите имена файлов для архивации (через запятую): ").split(', ')
                archive_filename = input("Введите имя архива: ")
                file_manager.archive_files(files_to_archive, archive_filename)
            elif user_choice == '6':
                archive_filename = input("Введите имя архива для разархивации: ")
                extraction_folder = input("Введите имя папки для разархивации: ")
                file_manager.extract_archive(archive_filename, extraction_folder)
            elif user_choice == '7':
                files_to_backup = input("Введите имена файлов для резервного копирования (через запятую): ").split(', ')
                backup_folder = input("Введите имя папки для резервного копирования: ")
                file_manager.backup_files(files_to_backup, backup_folder)
            elif user_choice == '8':
                file_to_manage = input("Введите имя файла для управления правами доступа: ")
                access_choice = input(
                    "Выберите права доступа:\n1. Только чтение (r)\n2. Чтение и запись (w)\nВведите номер права доступа: ")
                file_manager.manage_file_permissions(file_to_manage, access_choice)
            elif user_choice == '9':
                file_to_edit = input("Введите имя файла для изменения содержимого: ")
                new_content = input("Введите новое содержимое файла: ")
                file_manager.edit_file_content(file_to_edit, new_content)
            elif user_choice == '10':
                new_base_folder = input("Введите новый путь к базовой папке: ")
                file_manager.change_base_folder(new_base_folder)
            elif user_choice == '11':
                source_file = input("Введите имя файла для перемещения: ")
                destination_disk = input("Введите букву диска (пример: D:): ")
                file_manager.move_to_another_disk(source_file, destination_disk)
            elif user_choice == '12':
                file_to_inspect = input("Введите имя файла для получения информации: ")
                file_info_result = file_manager.file_info(file_to_inspect)
                print(file_info_result)
            elif user_choice == '13':
                new_folder_name = input("Введите имя новой папки: ")
                file_manager.create_folder(new_folder_name)
            elif user_choice == '0':
                break
            else:
                print("Некорректный выбор. Пожалуйста, введите корректный номер операции.")
    elif choice == '2':
        root = tk.Tk()
        gui = GUIFileManager(root, file_manager)
        root.mainloop()
    else:
        print("Некорректный выбор. Пожалуйста, введите 'cli' или 'gui'.")


if __name__ == "__main__":
    main_menu()
