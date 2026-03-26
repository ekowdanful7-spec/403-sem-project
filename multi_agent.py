import asyncio

# ---------------- SENSOR ----------------
async def sensor():
    print("🚨 Sensor Agent: Fire detected!")
    print("📡 Sending alert to Coordinator...\n")
    await asyncio.sleep(1)
    return "fire_alert"

# ---------------- COORDINATOR ----------------
async def coordinator(message):
    if message == "fire_alert":
        print("🧠 Coordinator Agent: Alert received!")
        print("📋 Assigning Rescue Agent...\n")
        await asyncio.sleep(1)
        return "dispatch_rescue"

# ---------------- RESCUE ----------------
async def rescue(task):
    if task == "dispatch_rescue":
        await asyncio.sleep(2)
        print("🚑 Rescue Agent: Responding to emergency!")
        print("✅ Victims rescued successfully.\n")

# ---------------- MAIN ----------------
async def main():
    alert = await sensor()
    task = await coordinator(alert)
    await rescue(task)

if __name__ == "__main__":
    asyncio.run(main())