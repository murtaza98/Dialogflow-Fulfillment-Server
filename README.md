# Dialogflow Fulfillment Server 

### Prerequisites
- Python 3

### Installation Step
1. Create a virtual environment with Python 3.6: 
 `python3 -m virtualenv venv`

2. Activate the environment:
- **Linux:** `source venv/bin/activate`
- **Windows:** `.\venv\Scripts\activate.bat`

3. Install the required packages from `requirements.txt` inside this virtual environment:
 `pip install -r requirements.txt`

4. Run app.py script: `python server.py`

5. Use tunnelling service like `ngrok` to get a global IP address

6. Enable `Fulfillment` on Dialogflow Dashboard and there enter the URL from step 5