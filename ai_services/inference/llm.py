from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os
from dotenv import load_dotenv

load_dotenv()

class LLMAgent:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("⚠️ OPENAI_API_KEY missing. Agent disabled.")
            self.llm = None
            return

        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=api_key)
        
        # Define the structure we want the LLM to return
        response_schemas = [
            ResponseSchema(name="entity", description="The main company or financial entity"),
            ResponseSchema(name="sentiment", description="positive, negative, or neutral"),
            ResponseSchema(name="reasoning", description="Short financial explanation for the sentiment")
        ]
        self.output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = self.output_parser.get_format_instructions()

        template = """
        You are a financial analyst. Analyze the headline below.
        Headline: {headline}
        
        {format_instructions}
        """
        self.prompt = PromptTemplate(
            template=template,
            input_variables=["headline"],
            partial_variables={"format_instructions": format_instructions}
        )

    def analyze(self, text):
        if not self.llm:
            return {"entity": "Error", "sentiment": "neutral", "reasoning": "No API Key"}

        try:
            _input = self.prompt.format(headline=text)
            response = self.llm.invoke(_input)
            return self.output_parser.parse(response.content)
        except Exception as e:
            return {"entity": "Error", "sentiment": "neutral", "reasoning": str(e)}