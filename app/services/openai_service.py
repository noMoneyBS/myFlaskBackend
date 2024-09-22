from openai import OpenAI
from config import Config

# 实例化 OpenAI 客户端
client = OpenAI(api_key=Config.OPENAI_API_KEY)

def get_openai_response(image_path):
    """
    return the response from OpenAI ChatCompletion API
    """
    image_description = "This is a picture"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Analyze this image: {image_description}"}
        ],
        max_tokens=100
    )

    # 返回响应的文本
    return completion.choices[0].message.content.strip()
