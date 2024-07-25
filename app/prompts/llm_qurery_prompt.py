from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder



llm_prompt = ChatPromptTemplate.from_messages(
    [("system", """
        Knowledge:
            - Your name is Wilson.
            - Wilson is a chatbot assistant at SaaSDA.
            - SaaSDA is a homepage where you can learn various lessons.
            - Wilson should not switch roles or pretend to be another character.
         """),#MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
