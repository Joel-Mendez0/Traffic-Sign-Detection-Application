import os

def update_class_labels(directory_path):
    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        updated_lines = [line.replace('0 ', '0 ').replace('1 ', '0 ').replace('2 ', '0 ')
                         .replace('3 ', '0 ').replace('4 ', '0 ').replace('5 ', '0 ')
                         .replace('6 ', '0 ').replace('7 ', '0 ') for line in lines]

        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"Updated {file_name}")

directory_path = '//home//joel//YOLOPROJECT//valid//labels'
update_class_labels(directory_path)

