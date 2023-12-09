import os

def count_class_samples(directory_path):
    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

    class_counts = {}

    for file_name in files:
        file_path = os.path.join(directory_path, file_name)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            class_label = int(line.split()[0])

            class_counts[class_label] = class_counts.get(class_label, 0) + 1

    return class_counts

directory_path = '//home//joel//Downloads//Campus.v1i.yolov8//train//labels'
class_counts = count_class_samples(directory_path)

for class_label, count in class_counts.items():
    print(f"Class {class_label}: {count} samples")

