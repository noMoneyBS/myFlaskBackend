import requests

# 服务器的URL地址
url = 'http://127.0.0.1:5000/upload'  

# 要上传的图片文件路径
image_path = 'image.jpg'

try:
    # 准备图片文件
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}

        # http
        response = requests.post(url, files=files, verify=False)

        if response.status_code == 200:
            print("Upload successful")
            print("Server Response:", response.json())
        else:
            print(f"Failed to upload image. Status code: {response.status_code}")
            print("Error:", response.text)
except FileNotFoundError:
    print(f"File {image_path} not found. Please check the file path.")
