# main.py
from app.agent_monitor import monitored_gpt_call

if __name__ == "__main__":
    user_prompt = input("Enter a prompt for the AI agent: ")
    print("\n--- AI Response ---")
    print(monitored_gpt_call(user_prompt))

