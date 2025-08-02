async def start_docker(docker):
    """
    Function to start the docker container.
    """
    await docker.start()

async def stop_docker(docker):
    """
    Function to stop the docker container.
    """
    await docker.stop()
    