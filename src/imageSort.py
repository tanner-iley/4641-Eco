import os

base_dir = 'graphs'

folders = {
    'linearRegression': 'linearRegression_images.md',
    'knn': 'knn_images.md',
    'randomForest': 'randomForest_images.md'
}

for folder, md_file in folders.items():
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        continue

    with open(md_file, 'w') as file:
        file.write(f"# {folder.capitalize()} Images\n\n")

    for image in os.listdir(folder_path):
        if image.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            encoded_image = image.replace(' ', '%20')
            img_path = f"/{folder}/{encoded_image}"
            with open(md_file, 'a') as file:
                file.write(f"![{image}]({img_path})\n\n")
            print(f"Added {image} to {md_file}")
        else:
            print(f"Skipping file (unsupported extension): {image}")
