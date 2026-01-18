class Tools:
    def use_tool(self, task):
        task = task.lower()

        if "search" in task:
            return "🔍 Search completed successfully."
        elif "write" in task:
            return "✍️ Content generated."
        elif "calculate" in task:
            return "🧮 Calculation done."
        else:
            return "✅ Task executed successfully."
