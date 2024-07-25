from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder,PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

class Topic(BaseModel):
    output: str = Field(description="The category number representing the user's question intent")
parser = JsonOutputParser(pydantic_object=Topic)


template = """
#Role
Intelligent Intent Classifier Assistant

# Task
Categorize each user question based on the conversation history and the type of information required:

0 :Course or Content Information: Questions related to course offerings, registration periods, course duration, instructor details, and detailed course or content descriptions.
1 :Student-specific Queries: Questions regarding the courses currently being taken by the student, assignment submissions, assignment grades, exam information, exam schedules, results, course completion dates, payment information.,ompletion requirements, and certificates obtained.
2 : Gamification Features: Questions about the student's current points, badges, rankings, and levels achieved through the platform's gamification elements.
3 : Platform Functionalities: Questions about features offered by the platform, such as note-taking, inquiry submissions, personal lecture schedules, personal learning goals, progress towards goals, and daily study hours.
4 : Service FAQs — Questions related to the functionalities of a service or platform, such as "How do I sign up for a course?", "How do I make a payment?","I forgot my password", or "How can I contact customer support?" These questions involve understanding and navigating within the service or its features.
5 : Recent/External Information — Questions requiring current information that is outside the typical scope of the assistant's training data, such as recent events, weather conditions, products, and the latest market prices. Questions that require current data, such as weather forecasts, recent events, and market updates. If a question includes the need for current weather conditions or similar timely details, it should fall into this category. If a user's question contains the keywords "search for me," "search," or "~search," you should Google it.
6 : General Knowledge/Conversation Context — Questions that can be answered using broad, accessible knowledge or ongoing conversation details that do not require up-to-date external data, generally accessible knowledge or information from the ongoing conversation.
7 : Casual Conversation - This category is designated for queries that engage the chatbot in everyday casual conversations. These include questions about preferences, opinions, and hypothetical scenarios that are typical in human-like interactions. It is meant for engaging users in dialogue that builds rapport and provides a more human-like interaction experience.

# Format
The most important one. Responses should strictly categorize the input question into one of the four defined categories: 0,1,2,3,4,5,6 or 7.
You must respect the answer form. Answers should contain only numbers, not characters.
Return only the category number without additional text or explanation. This streamlined format will facilitate clear and concise decision-making.

{format_instructions}
\n{input}
Intelligent Assistant:
"""

prompt = PromptTemplate(template=template,
                        input_variables=['input'],
                        partial_variables={"format_instructions": parser.get_format_instructions()}
                        )