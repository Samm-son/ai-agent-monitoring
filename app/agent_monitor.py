import os
import openai
from langfuse import Langfuse
from dotenv import load_dotenv
from app.logger import logger

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host="https://us.cloud.langfuse.com"
)


def monitored_gpt_call(user_input, user_id="demo-user"):
    trace = langfuse.trace(name="AgentInteraction", user_id=user_id)
    span = trace.span(name="GPT-Call")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7
        )
        content = response.choices[0].message.content
        logger.info("GPT Response: %s", content)

        span.end(
            output=content,
            input=user_input,
            metadata=response.model_dump()
        )

        return content

    except Exception as e:
        logger.error("GPT call failed: %s", str(e))
        span.end(output=str(e), level="ERROR")
        raise

