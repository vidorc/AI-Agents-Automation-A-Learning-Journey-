from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel, Field


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class Review(BaseModel):
    key_themes: List[str] = Field(..., description="Write down all the key themes discussed in the review in a list")
    pros: Optional[List[str]] = Field(None, description="Write down all the pros in the list")
    summary: str = Field(..., description="A brief summary of the review")
    sentiment: str = Field(..., description="Return the sentiment of the review: negative, positive, or neutral")
    cons: Optional[List[str]] = Field(None, description="Write down all the cons in the list")
    name: str = Field(..., description="Write the name of the reviewer")

structured_model = model.with_structured_output(Review)

review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! 
The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, 
or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W 
fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. 
What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images 
even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still 
comes with bloatware—why do I need five different Samsung apps for things Google already provides? 
The $1,300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor (great for gaming and productivity)
- Stunning 200MP camera with incredible zoom capabilities
- Long battery life with fast charging
- S-Pen support is unique and useful
                                 
Review by Mayank Sharma
"""

result = structured_model.invoke(review_text)

print(result)
print(result.summary)
print(result.sentiment)
