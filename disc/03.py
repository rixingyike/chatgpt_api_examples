# disc/03.py
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "Do u know yishulun？"}]
)

print(completion)

# 下面是返回示例（要开系统全局代理，才能成功调用）
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "As an AI language model, I am aware that Yishulun is a district located in Inner Mongolia, China. However, I do not have any personal experience or familiarity with the region beyond what is found in available data.",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1679750187,
#   "id": "chatcmpl-6xy2tvxpUxwArvMOJEYT7T3O7hAjz",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 46,
#     "prompt_tokens": 16,
#     "total_tokens": 62
#   }
# }