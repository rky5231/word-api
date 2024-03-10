Dictionary API
Welcome to the Dictionary API! This Flask web application provides a simple API to fetch word definitions from a CSV file.

Usage
API Endpoint
To use the API, send a GET request to the following endpoint:

ruby
Copy code
http://your-domain/api/v1/<word>
Replace <word> with the word you want to get the definition for.

Example
For example, to get the definition of the word "sun", you would send a GET request to:

bash
Copy code
http://your-domain/api/v1/sun
Response
If the word is found in the dictionary, the API will return a JSON object containing the word and its definition. If the word is not found, it will return an error message.

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/dictionary-api.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Flask application:
bash
Copy code
python app.py
The application will start running on http://127.0.0.1:5000/ by default.

Data Source
The word definitions are fetched from a CSV file named dictionary.csv. You can customize this file with your own data or modify the application logic as needed.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
