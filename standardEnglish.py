import langchain
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

class StandardEnglish():
    def __init__(self, text_to_convert):
        self.text_to_convert = text_to_convert

    def convertStandardEnglish(self):
        llm = Ollama(model="phi")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "you are English grammar checker"),

            ("user", "{input}")
        ])
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        result = chain.invoke({"input": f"Just correct this to standard English without more information:\n{self.text_to_convert}"})

        return result
