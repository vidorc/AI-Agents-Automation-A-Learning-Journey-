from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
llm = HuggingFaceEndpoint(

repo_id = "google/gemini-2-2b-it"
task = "task generation"
)

model = ChatHuggingFace(llm=llm)

schema =[
    ResponseSchema(name='fact-1',description='Fact 1 is about the topic'),
    ResponseSchema(name='fact-2',description='Fact 2 is about the topic'),
    ResponseSchema(name='fact-3',description='Fact 3 is about the topic'),
    ResponseSchema(name='fact-4',description='Fact 4 is about the topic'),

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variable = {'format_instruction': parser.ger_format_instructions()}
)
prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)