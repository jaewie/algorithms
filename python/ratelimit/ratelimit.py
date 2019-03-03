import time


class RateLimiter:
    def __init__(self, num_requests, num_secs):
        self.num_requests = num_requests
        self.num_secs = float(num_secs)
        self.pool = num_requests
        self.last_ts = time.time()

    def ratelimit(self):
        # Replenish pool
        now = time.time()
        elapsed = now - self.last_ts
        self.last_ts = now
        self.pool = min(self.num_requests, self.pool + elapsed * (self.num_requests / self.num_secs))

        # Determine whether enough in pool to make request
        if self.pool > 1:
            self.pool -= 1
            return True
        return False
