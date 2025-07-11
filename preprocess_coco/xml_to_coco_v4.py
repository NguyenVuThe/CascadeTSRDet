import os
import xml.etree.ElementTree as ET
import json
from tqdm import tqdm

'''
This script reads a folder of XMLs and convert it into COCO format file
'''

voc_folder = r"D:\MyWorking\dataset\FinTabNet.c\FinTabNet.c-Structure\test"
output_json = "dataset/ftbc_full_6classes_test.json"

categories_list = [
    "table",
    "table column",
    "table row",
    "table spanning cell",
    "table projected row header",
    "table column header"
]

category_id_map = {name: i + 1 for i, name in enumerate(categories_list)}

images = []
annotations = []
image_id = 0
annotation_id = 0

for file in tqdm(sorted(os.listdir(voc_folder))):
    if not file.endswith(".xml"):
        continue
    if image_id > 9288:
        break       
    xml_path = os.path.join(voc_folder, file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    filename = root.find("filename").text.strip()
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)

    images.append({
        "id": image_id,
        "file_name": filename,
        "width": width,
        "height": height
    })

    for obj in root.findall("object"):
        class_name = obj.find("name").text.strip()
        if class_name not in category_id_map:
            continue  # skip unknown or "no object"

        bbox = obj.find("bndbox")
        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)
        w = xmax - xmin
        h = ymax - ymin
        area = w * h

        # segmentation polygon: rectangular bbox
        segmentation = [
            [xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax]
        ]

        annotations.append({
            "id": annotation_id,
            "image_id": image_id,
            "category_id": category_id_map[class_name],
            "bbox": [xmin, ymin, w, h],
            "area": area,
            "iscrowd": 0,
            "segmentation": segmentation
        })

        annotation_id += 1

    image_id += 1

categories = [
    {"id": i + 1, "name": name, "supercategory": "Table"}
    for i, name in enumerate(categories_list)
]

output = {
    "info": { "author": "Bin Xiao" },
    "images": images,
    "annotations": annotations,
    "licenses": { "author": "Bin Xiao" },
    "categories": categories
}

with open(output_json, "w") as f:
    json.dump(output, f, indent=2)

print(f"COCO-style JSON saved as {output_json}")