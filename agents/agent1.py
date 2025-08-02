from autogen_agentchat.agents import  CodeExecutorAgent

from confrig.docker_executor import get_executor

def get_code_executor():
    """
    Function to get the code executor agent.
    This agent is responsible for executing code.
    It will work with the problem solver agent to execute the code.
    """

    docker=get_executor()
    code_executor=CodeExecutorAgent(

        name='CodeExecutorAgent',
        code_executor= docker,
        
        
    )
    return code_executor,docker