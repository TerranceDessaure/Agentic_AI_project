# test_key.py

from dotenv import load_dotenv
import os
import httpx2 as httpx
from anthropic import Anthropic

# This looks for a .env file in the current working directory
# and loads its contents into the environment
load_dotenv()
client = Anthropic()

custom_http_client = httpx.Client(
    headers={"Accept-Encoding": "gzip, deflate"}
)

client = Anthropic(http_client=custom_http_client)

# Confirm the key loaded — don't print the actual key, just check it exists
api_key_loaded = os.environ.get("ANTHROPIC_API_KEY") is not None
print("API key loaded:", api_key_loaded)

# If that printed True, this next part confirms the client can use it
from anthropic import Anthropic

import httpx2 as httpx  # matching whatever the anthropic package is using internally
from anthropic import Anthropic

# Build a custom HTTP client that doesn't negotiate brotli compression
custom_http_client = httpx.Client(
    headers={"Accept-Encoding": "gzip, deflate"}
)

client = Anthropic(http_client=custom_http_client)
# --- new diagnostic code below ---
import traceback

try:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=20,
        messages=[{"role": "user", "content": "Say hello in exactly 3 words."}]
    )
    print(response.content[0].text)
except Exception as e:
    print("Top-level error:", e)
    print("Underlying cause:", repr(e.__cause__))
    traceback.print_exception(type(e.__cause__), e.__cause__, e.__cause__.__traceback__)


print(response.content[0].text)