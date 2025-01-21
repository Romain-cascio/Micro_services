from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def load_test(self):
        self.client.get("/")
