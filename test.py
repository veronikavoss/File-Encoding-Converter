from PIL import Image

# 이미지 파일 경로
image_path = 'path_to_your_image.jpg'

# 이미지 열기
image = Image.open(image_path)

# 이미지의 EXIF 데이터 가져오기
exif_data = image._getexif()

# EXIF 데이터가 있는지 확인
if exif_data:
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")
else:
    print("No EXIF data found.")
