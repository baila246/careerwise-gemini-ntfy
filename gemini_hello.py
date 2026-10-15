import os

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv(override=True)
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise SystemExit(
            "Missing GOOGLE_API_KEY. Set it as an environment variable (or in a .env file)."
        )

    gemini = OpenAI(
        api_key=google_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    resp = gemini.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hi and give me one productivity tip."},
        ],
    )

    print(resp.choices[0].message.content)


if __name__ == "__main__":
    main()
