from agent import AgentBrain, Memory, Tools

def main():
    print("🚀 Ayaan Agentic AI Started")

    agent = AgentBrain(
        name="Ayaan-Agent",
        goal="Solve tasks autonomously using tools and memory"
    )

    memory = Memory()
    tools = Tools()

    while True:
        task = input("\n📝 Enter task (or 'exit'): ")

        if task.lower() == "exit":
            break

        plan = agent.think(task)
        print(plan)

        result = tools.use_tool(task)
        memory.save(task, result)

        print(result)

    memory.show()

if __name__ == "__main__":
    main()
