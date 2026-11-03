import os
import csv

base_folder = r"D:\DataProjects\DriverBehaviourAnalytics\data_raw\Multi-Class Driver Behavior Image Dataset"

output_file = "driver_metadata.csv"

rows = []

for behaviour in os.listdir(base_folder):

    behaviour_path = os.path.join(base_folder, behaviour)

    if os.path.isdir(behaviour_path):

        for file_name in os.listdir(behaviour_path):

            if file_name.lower().endswith((".jpg", ".jpeg", ".png")):

                extension = os.path.splitext(file_name)[1]

                rows.append([
                    file_name,
                    behaviour,
                    extension
                ])

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "image_name",
        "behaviour",
        "extension"
    ])

    writer.writerows(rows)

print(f"Created {output_file}")
print(f"Rows: {len(rows)}")