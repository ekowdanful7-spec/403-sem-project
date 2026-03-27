import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class SensorBehaviour(OneShotBehaviour):
    async def run(self):
        print("🚨 Sensor Agent: Fire detected!")
        print("📡 Sending alert to Coordinator...\n")
        await asyncio.sleep(1)

class SensorAgent(Agent):
    async def setup(self):
        print("🔍 Sensor Agent starting...")
        self.add_behaviour(SensorBehaviour())

class CoordinatorBehaviour(OneShotBehaviour):
    async def run(self):
        await asyncio.sleep(1)
        print("🧠 Coordinator Agent: Alert received!")
        print("📋 Assigning Rescue Agent...\n")

class CoordinatorAgent(Agent):
    async def setup(self):
        print("🧠 Coordinator Agent starting...")
        self.add_behaviour(CoordinatorBehaviour())

class RescueBehaviour(OneShotBehaviour):
    async def run(self):
        await asyncio.sleep(2)
        print("🚑 Rescue Agent: Responding to emergency!")
        print("✅ Victims rescued successfully.\n")
        await self.agent.stop()

class RescueAgent(Agent):
    async def setup(self):
        print("🚑 Rescue Agent starting...")
        self.add_behaviour(RescueBehaviour())

async def main():
    jid = "agent1@localhost"
    password = "password"

    sensor = SensorAgent(jid, password, verify_security=False)
    coordinator = CoordinatorAgent(jid, password, verify_security=False)
    rescue = RescueAgent(jid, password, verify_security=False)

    await sensor.start(auto_register=True)
    await coordinator.start(auto_register=True)
    await rescue.start(auto_register=True)

    await asyncio.sleep(5)

    await sensor.stop()
    await coordinator.stop()
    await rescue.stop()

if __name__ == "__main__":
    asyncio.run(main())
