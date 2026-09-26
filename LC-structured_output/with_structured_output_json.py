from typing import Literal
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

#schema

json_schema = {
    "title" : "review",
    "type" : "object",
    "properties" : {
        "key_themes" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "descriptiom" : "Write down all the key themes discusssed in the review"
        },
        "summary" : {
            "type" : "string",
            "description" : "A brief summary of the review"
        },
        "sentiment" : {
            "type" : "string",
            "enum": [
                "pos",
                "neg"
            ],
            "description" : "sentiment of the review euther positive, negative or neutral"
        },
        "pros" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "description" : "Write down all the pros inside the list"
        },
        "cons" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "description" : "Write down all the cons inside the list"
        },
        "name" : {
            "type" : "string",
            "description" : "Write down name of reviewer"
        }       
    }
}
model = ChatGroq(
    model = "qwen/qwen3.8-27b",
    temperature = 0
)

structured_output = model.with_structured_output(json_schema)

result = structured_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful""")

print(result)
print(result["pros"])
print(result["cons"])
print(result["sentiment"])
print(result["name"])