#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
import json
from openai import OpenAI

with open("personality.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    personalities = data["personalities"]

print("\n🔥Available AI Personalities🔥")
for i,personality in enumerate(personalities,1):
    print(f"{i},{personality['name']}")


while True:
    try:
        choice = int(input("\nSelect a personality (Enter the number) :"))
        selected_personality = personalities[choice-1]
        personality_name = selected_personality["name"]
        personality_prompt = selected_personality["prompt"]
        break
    except:
        print("Invalid choice. Please try again")


print(f"\n✅ You selected {personality_name}\n")

#Open AI API Logic
client = OpenAI(api_key="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")

#Chat Loop
print("💬 Start to chat (type exit to quit)")

while True:
    user_input = input("You :")
    if user_input.lower() == "exit":
        print("👋 Good Bye")
        break

    chat_completion = client.chat.completions.create(
        messages=[
            {"role":"system","content":personality_prompt},
            {"role":"user","content":user_input}
        ],
        model="gpt-4o-mini"

    )

    response_message = chat_completion.choices[0].message.content
    print("AI :",response_message)