"""
Agentic AI Problem Solver using Microsoft AutoGen
=================================================

Overview
--------
This project is an agentic AI system designed to solve data structures and algorithms (DSA) problems automatically. It leverages Microsoft's AutoGen framework to orchestrate multiple autonomous agents that collaborate to generate, execute, and validate code solutions.

Key Features
------------
- **Agentic Architecture**: Modular agents (see `agents/`) for code generation, execution, validation, and feedback.
- **AutoGen Integration**: Utilizes Microsoft's AutoGen for agent communication and workflow automation.
- **Containerized Execution**: Secure code execution using Docker (see `confrig/docker_executor.py`).
- **Team Collaboration**: Agents can work in teams (see `teams/main_team.py`) to solve complex problems.
- **Temporary Workspace**: Solutions and intermediate code are managed in the `temp/` directory.

Project Structure
-----------------
- `app.py`: Main entry point for the application.
- `agents/`: Contains agent definitions and logic.
- `confrig/`: Configuration, Docker utilities, and settings.
- `teams/`: Team-based agent orchestration.
- `temp/`: Temporary files and generated solutions.
- `requirements.txt`: Python dependencies.

Getting Started
---------------
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the main application:**
   ```sh
   python app.py
   ```
3. **Configure agents and teams as needed in their respective folders.**

Customization
-------------
- Add or modify agents in `agents/` to extend capabilities.
- Update Docker settings in `confrig/` for secure execution.
- Organize agent teams in `teams/` for collaborative workflows.

References
----------
- [Microsoft AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Project Repository/Docs] (add your repo link here)

"""
