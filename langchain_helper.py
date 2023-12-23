from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
os.environ['OPENAI_API_KEY']="enter your key"
llm=OpenAI(temperature=0.6)

def generate_shop_name_and_services(country_name):
    # prompt for shop name 
    prompt_template_name=PromptTemplate(
        # country is input variable, we can define multiple variables here.
        input_variables=['country'],
        template = "I want to open a computer hardware repairing shop in {country} . Suggest a fency name for this."
        )
    #' output_key ' - it will also shows as an output 
    chain= LLMChain(llm=llm,prompt=prompt_template_name,output_key="shop_name")
    
    prompt_template_items=PromptTemplate(
        # country is input variable, we can define multiple variables here.
        input_variables=['shop_name'],
        template = "Suggest top 5 services menu for my shop {shop_name}. Return it as comma seprated list. "
        )
    chain_items= LLMChain(llm=llm,prompt=prompt_template_items,output_key="services")

    chain=SequentialChain(
        chains=[chain,chain_items],
        # initial input as an country name
        input_variables=['country'],
        # output will display on the output cell
        output_variables=['shop_name','services']
        )

    # note:- india is the input value for 'country' input variable
    response=chain({'country':'india'})
    return response


if __name__=="__main__":
    print(generate_shop_name_and_services("indian"))