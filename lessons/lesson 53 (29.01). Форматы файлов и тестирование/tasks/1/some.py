import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, period_seconds):
        self.max_calls = max_calls
        self.period = period_seconds
        self.calls = deque()

    def allow(self):
        now = time.time()

        while self.calls and self.calls[0] <= now - self.period:
            self.calls.popleft()

        if len(self.calls) >= self.max_calls:
            return False

        self.calls.append(now)
        return True


if __name__ == "__main__":
    limiter = RateLimiter(max_calls=3, period_seconds=5)

    for i in range(6):
        print(i, limiter.allow())
        time.sleep(1)
