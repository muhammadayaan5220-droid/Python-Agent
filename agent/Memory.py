class Memory:
    def __init__(self):
        self.history = []

    def save(self, task, result):
        self.history.append({
            "task": task,
            "result": result
        })

    def show(self):
        print("\n🧠 Memory Log:")
        for i, item in enumerate(self.history, 1):
            print(f"{i}. {item['task']} → {item['result']}")
