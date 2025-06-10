import time
from typing import Dict
import threading

class RateLimiter:
    def __init__(self, max_requests_per_minute: int = 3):
        self.max_requests_per_minute = max_requests_per_minute
        self.requests: Dict[str, list] = {}
        self.lock = threading.Lock()

    def wait_if_needed(self, key: str):
        with self.lock:
            current_time = time.time()
            if key not in self.requests:
                self.requests[key] = []
            
            # Remove requests older than 1 minute
            self.requests[key] = [t for t in self.requests[key] if current_time - t < 60]
            
            if len(self.requests[key]) >= self.max_requests_per_minute:
                # Wait until we can make another request
                sleep_time = 60 - (current_time - self.requests[key][0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                self.requests[key] = self.requests[key][1:]
            
            self.requests[key].append(current_time)