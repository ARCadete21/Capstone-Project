%load_ext autoreload
%autoreload 2

# Import the OpenAI library
import random
from openai import OpenAI
from util import *
from chat_bot import *

# Create an instance of the GPT_Helper class
helper = GPT_Helper(OPENAI_API_KEY="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")

# Get a completion from the model
response = helper.get_completion("Hello, world!")

# Print the response
print(response)
