# Word API

The Word API project provides a RESTful API for accessing word-related information, including definitions, synonyms, antonyms, and examples. It serves as a convenient tool for developers to integrate word-related functionalities into their applications.

## Features

- **Word Definitions**: Retrieve definitions of words.
- **Synonyms and Antonyms**: Get synonyms and antonyms for words.
- **Example Usage**: Access example sentences using words.
- **RESTful API**: Expose endpoints to interact with the word-related functionalities programmatically.
- **Simple Integration**: Easily integrate the Word API into your applications using HTTP requests.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rky5231/word-api.git
    ```

2. Navigate into the project directory:

    ```bash
    cd word-api
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Access the API endpoints using a tool like cURL, Postman, or by making HTTP requests from your application.

## Usage

1. Send HTTP GET requests to the API endpoints to retrieve word-related information.
2. Use the provided endpoints `/definitions`, `/synonyms`, `/antonyms`, and `/examples` to access different types of word-related data.
3. Customize and extend the API as needed to suit your application's requirements.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to suggest improvements, report bugs, or add new features.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rky5231/word-api/blob/main/LICENSE) file for details.
