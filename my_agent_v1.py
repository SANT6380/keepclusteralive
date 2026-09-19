from agent_interface import BaseAgent

class MyAgent(BaseAgent):

    def reset(self):
        pass

    def calculate_health(self, node):
        score = 100

        if not node["heartbeat_ok"]:
            score -= 50

        latency = node.get("latency_ms")
        if latency is None:
            latency = 1000

        error_rate = node.get("error_rate")
        if error_rate is None:
            error_rate = 1.0

        queue_len = node.get("queue_len")
        if queue_len is None:
            queue_len = 10

        score -= latency / 10
        score -= error_rate * 100
        score -= queue_len * 2

        return score

    def act(self, obs):
        actions = {}

        health_scores = {}

        for node in obs["nodes"]:
            health_scores[node["node_id"]] = self.calculate_health(node)

        best_node = max(health_scores, key=health_scores.get)

        for task in obs["tasks"]:
            if task["node"] is None:
                actions[task["task_id"]] = best_node

        return actions

    def update(self, obs, reward, done, info):
        pass