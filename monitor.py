import time
import requests
from openpyxl import Workbook

class TokenMonitor:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.token_data = []
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(["Timestamp", "Total Tokens", "Prompt Tokens", "Completion Tokens"])

    def get_token_usage(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(f"{self.api_url}/usage", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching token usage: {e}")
            return None

    def monitor(self, interval=60):
        while True:
            usage_data = self.get_token_usage()
            if usage_data:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                self.token_data.append([
                    timestamp,
                    usage_data.get("total_tokens", 0),
                    usage_data.get("prompt_tokens", 0),
                    usage_data.get("completion_tokens", 0)
                ])
                print(f"Logged usage at {timestamp}")
            time.sleep(interval)

    def export_to_excel(self, filename="token_usage.xlsx"):
        for data in self.token_data:
            self.ws.append(data)
        self.wb.save(filename)
        print(f"Data exported to {filename}")

if __name__ == "__main__":
    # Replace with your actual API credentials
    API_KEY = "your-api-key-here"
    API_URL = "https://api.example.com/v1"
    
    monitor = TokenMonitor(API_KEY, API_URL)
    try:
        monitor.monitor()
    except KeyboardInterrupt:
        monitor.export_to_excel()
        print("Monitoring stopped. Data exported.")
