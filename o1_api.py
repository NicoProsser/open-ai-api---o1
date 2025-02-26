import openai
import time
import base64

# Set your API key, best would be via environmental variable
api_key = 'xxx'
openai.api_key = api_key

def load_screenshot():
    """ Loads file 'screenshot.png' from the current folder and returns it as base64 string """
    screenshot_path = "screenshot.png"
    
    try:
        with open(screenshot_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        return base64_image
    except FileNotFoundError:
        print("Error: File 'screenshot.png' not found.")
        return None

def send_request_to_api(base64_image):
    """ Sends a request to the open ai api with the model 'o1' """
    
    response = openai.chat.completions.create(
        model="o1",  # gpt-4o should also work
        messages=[
            {
                "role": "developer",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Answer me the question from the screenshot as easy as possible"
                        )
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"}  # Screenshot
                    }
                ]
            }
        ],
        response_format={"type": "text"}
    )
    
    return response.choices[0].message.content.strip()

def main():
    """ Main function to load the screenshot and send it to the OpenAI API """
    
    base64_image = load_screenshot()
    if base64_image:
        response = send_request_to_api(base64_image)
        print("API response:", response)

if __name__ == "__main__":
    main()