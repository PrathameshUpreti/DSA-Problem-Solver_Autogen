from agents.agent1 import get_code_executor
from agents.agent2 import problem_solving_agent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from confrig.storedvar import TEXT_MENTION, MAX_TURNS

def create_team():
    """
    Function to create the team.
    This team will be used to solve the problem.
    """
    ProblemSolvingAgent = problem_solving_agent()
    CodeExecutorAgent,docker = get_code_executor()
    termination_condition = TextMentionTermination(TEXT_MENTION)
    team = RoundRobinGroupChat(
        participants=[ProblemSolvingAgent,
                      CodeExecutorAgent
                      ],
        termination_condition=termination_condition,
        max_turns=MAX_TURNS,
        
        
    )
    return team,docker