import os,certifi
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from dotenv import load_dotenv,find_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
import requests
import streamlit as st


load_dotenv()


search_tool=TavilySearch(max_results=2)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("groq_api_key"),
    temperature=0
)

search_tool=TavilySearch(max_results=2)


@tool
def get_wether(city:str)->str:
    """
    Fetch current weather information for a city.
    """

    url=(
        f"https://api.weatherstack.com/current?"
        f"access_key={os.getenv("weather_api_key")}&query={city}"
    )

    res=requests.get(url)
    

    if res.status_code != 200:
        return f"could not fetch wether of {city}"

    data=res.json()

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%"
    )


@tool
def get_conversion_rate(f:str,t:str,q:int):

    """
    fetch currency conversion rate
    """
    url=f"https://v6.exchangerate-api.com/v6/{os.getenv('currency_api_key')}/latest/USD"

    res=requests.get(url).json()['conversion_rates']

    rate=res[t]/ res[f]

    out= rate*q

    return f"the value of {q}{f} in {t} is {out}"



tools=[search_tool,get_conversion_rate,get_wether]

prompt="""

You are an helpful AI assistant.
Use the avaliable tools to answer the question if nedded.
answer directly if you do not need the tools.

"""


agent=create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt

)



st.set_page_config(
    page_title="Agentic AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic AI Assistant")
st.markdown("Search + Weather +Currency conversion AI Agent using LangChain")


user_query=st.text_input("Enter your query?")


if st.button("Run Agent"):

    if user_query:

        with st.spinner("Agent is thinking..."):

            try:
                response = agent.invoke({
                        "messages": [
        {"role": "user", "content": user_query}
    ]
                })

                st.success("Response Generated")

                st.markdown("## Final Response")
                st.write(response["messages"][-1].content)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a query")