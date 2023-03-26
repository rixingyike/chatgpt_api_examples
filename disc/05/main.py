# disc/05/main.py
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
  prompt="A red fish bites a black dog.",
  n=2,
  size="1024x1024"
)
# ['256x256', '512x512', '1024x1024'] 
image_url = response['data']
print(image_url)

# return images
# [<OpenAIObject at 0x10ba22250> JSON: {
#   "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-P5cx5dozRuo6QOuUI69PBGjS/user-YTJ1uqnx8tzcebkd4cadXiZ8/img-aXMfLAJ7Y9olReqUMQBKAiHB.png?st=2023-03-25T12%3A43%3A38Z&se=2023-03-25T14%3A43%3A38Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-24T22%3A35%3A11Z&ske=2023-03-25T22%3A35%3A11Z&sks=b&skv=2021-08-06&sig=46iNyqwPXO7Mq3TXa40ie%2BhtgY%2BCG3DaIviLiQg/JlY%3D"
# }, <OpenAIObject at 0x1103f22a0> JSON: {
#   "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-P5cx5dozRuo6QOuUI69PBGjS/user-YTJ1uqnx8tzcebkd4cadXiZ8/img-37pFBBrQtBMaFebnaPB5CdVC.png?st=2023-03-25T12%3A43%3A38Z&se=2023-03-25T14%3A43%3A38Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-24T22%3A35%3A11Z&ske=2023-03-25T22%3A35%3A11Z&sks=b&skv=2021-08-06&sig=fYB00Kit/sY7D6VeuXsvZ48G%2BYvCuRo%2B/BRK0pht1z0%3D"
# }]