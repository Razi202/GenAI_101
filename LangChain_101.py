from langchain.llms import OpenAI
from langchain.llms.retrieval import MemoryRetrieval

openai_agent = OpenAI(api_key="YOUR_OPENAI_API_KEY")

memory_agent = MemoryRetrieval(max_length=10)

chatbot_chain = memory_agent >> openai_agent

def chat(message):
  memory_agent.update(message)
  response = chatbot_chain.run(message)
  return response

while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break
  bot_response = chat(user_input)
  print("Chatbot:", bot_response)
