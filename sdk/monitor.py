import time
from typing import Dict, Optional

class TokenMonitor:
    def __init__(self):
        self.token_usage: Dict[str, int] = {}
        self.threshold: Optional[int] = None

    def track_usage(self, model: str, tokens: int) -> None:
        """Track token usage for a specific model"""
        if model not in self.token_usage:
            self.token_usage[model] = 0
        self.token_usage[model] += tokens

    def set_threshold(self, threshold: int) -> None:
        """Set token usage threshold"""
        self.threshold = threshold

    def check_threshold(self) -> bool:
        """Check if total token usage exceeds threshold"""
        if self.threshold is None:
            return False
        return sum(self.token_usage.values()) >= self.threshold

    def get_usage(self) -> Dict[str, int]:
        """Get current token usage statistics"""
        return self.token_usage

    def reset(self) -> None:
        """Reset token usage statistics"""
        self.token_usage = {}
