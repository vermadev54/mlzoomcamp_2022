from locust import task
from locust import between
from locust import HttpUser

sample = {
    "message": "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"
}

class SpamClassify(HttpUser):
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