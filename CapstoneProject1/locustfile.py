from locust import task
from locust import between
from locust import HttpUser

sample = {
  "text": "Sooo SAD I will miss you here in San Diego!!!"
}

class TweetsClassify(HttpUser):
    """
    Usage:
        Start locust load testing client with:
            locust -H pip3 install locust
        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)