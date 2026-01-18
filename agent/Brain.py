class AgentBrain:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal

    def think(self, task):
        print(f"\n🤖 {self.name} is thinking...")
        return f"Plan created to complete: {task}"
