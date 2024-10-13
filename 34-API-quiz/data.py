"""Data module: It will get the quiz data from the API"""

import requests

# API doc: https://opentdb.com/api_config.php
endpoint = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
}

# consume the API
response = requests.get(url=endpoint, params=parameters)
# raise error case it occurs
response.raise_for_status()

# gets the response json
data = response.json()

# parse data
question_data = data["results"]

# example of the data:
# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
