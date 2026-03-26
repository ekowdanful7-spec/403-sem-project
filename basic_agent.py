import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class HelloBehaviour(OneShotBehaviour):
    async def run(self):
        print("Hello! Agent is running.")
        await self.agent.stop()

class HelloAgent(Agent):
    async def setup(self):
        print("Agent starting...")
        self.add_behaviour(HelloBehaviour())

async def main():
    agent = HelloAgent("agent1@localhost", "password", verify_security=False)
    await agent.start(auto_register=True)
    await asyncio.sleep(3)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())