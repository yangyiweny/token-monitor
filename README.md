# Token Monitor System

## Overview
A real-time token usage monitoring system for large language models. Tracks API calls, monitors token consumption, and provides alerts when usage exceeds thresholds.

## Features
- Real-time token usage tracking
- Threshold-based alerts
- API gateway integration
- Usage statistics and visualization
- Multi-model support

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yangyiweny/token-monitor.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the API server:
   ```bash
   python main.py
   ```
2. Configure monitoring threshold:
   ```bash
   curl -X POST http://localhost:8000/threshold -d '{"threshold": 10000}'
   ```
3. Check current usage:
   ```bash
   curl http://localhost:8000/usage
   ```

## Documentation
For detailed API documentation, visit [API Docs](http://localhost:8000/docs)
