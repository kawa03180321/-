import os
import json

IMAGE_FOLDER = "images"

# 対応する画像形式
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif")

images = []

if os.path.exists(IMAGE_FOLDER):
    for file in sorted(os.listdir(IMAGE_FOLDER)):
        if file.lower().endswith(EXTENSIONS):
            images.append(file)

with open("images.json", "w", encoding="utf-8") as f:
    json.dump(images, f, ensure_ascii=False, indent=2)

print(f"{len(images)}枚の画像を登録しました。")
