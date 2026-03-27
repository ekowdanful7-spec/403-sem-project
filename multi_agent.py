import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class SensorBehaviour(OneShotBehaviour):
    async def run(self):
        print("🚨 Sensor Agent: Fire detected!")
        await asyncio.sleep(1)

class SensorAgent(Agent):
    async def setup(self):
        self.add_behaviour(SensorBehaviour())

async def main():
    jid = "agent1@127.0.0.1"
    password = "password"

    sensor = SensorAgent(jid, password, verify_security=False)

    # ✅ await must be INSIDE this function
    await sensor.start(auto_register=True)

    await asyncio.sleep(3)

    await sensor.stop()

# ✅ THIS runs the async function properly
if __name__ == "__main__":
    asyncio.run(main())
