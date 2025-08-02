import streamlit as st
from teams.main_team import create_team
from confrig.docker_utils import start_docker,stop_docker
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio

st.title("🧑‍💻DSA Problem Solver")
st.write("Enter the problem statement and let the agent solve it for you")

task=st.text_area("Enter you Problem Statement")
st.write("Click on Solve to start solving the problem")

async def main(team,docker,task):
    try:
        await start_docker(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):

               print(msg:=f"{message.source}: {message.content}")
               yield msg
            elif isinstance(message,TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                yield msg
        print("Task Completed")
    except Exception as e:
        print(f"Error: {e}")
        yield f"Error: {e}"
    finally:
        await stop_docker(docker)

if st.button("Solve"):
    st.write("Solving...")
    team,docker=create_team()

    async def collect_messages():
        async for msg in main(team,docker,task):
            if isinstance(msg,str):
                if msg.startswith("User :"):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith('ProblemSolverAgent'):
                    with st.chat_message('assistant',avatar='🧑‍💻'):
                        st.markdown(msg)
                elif msg.startswith(''):
                    with st.chat_message('assistant',avatar='🤖'):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                with st.chat_message('stopper',avatar='🚫'):
                    st.markdown(f"Task Completed: {msg.result}")

    asyncio.run(collect_messages())


                
               
            
            

    
    

