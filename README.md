# MathApp Project

Welcome to the MathApp project! This is a simple Django-based web application that allows users to perform mathematical calculations and view a history of their operations.

## Getting Started

Follow these steps to set up and run the MathApp on your local machine:

1. Clone the repository to your local machine: git clone https://github.com/Shantanu505/MathApp.git

2. Navigate to the project directory: cd math-server

3. Install the required Python packages: pip install -r requirements.txt

4. Run the Django development server:  python manage.py runserver
5. 
6. Open your web browser and go to http://localhost:8000/ to access the Math Server.

## Features

- The main page provides a list of available endpoints that you can use to perform mathematical operations and view history.

- To perform calculations, use the URLs like `/5/plus/3`, `/3/minus/5/plus/8`, etc.

- The `/history` endpoint lists the last 20 operations performed on the server along with their answers.

- The server remembers the history even after a restart, as it saves the history to a `history.json` file.

## Project Structure

- `mathapp`: Django application directory containing settings, URLs, and configuration.
- `views.py`: Contains the core functionality, including views, calculations, and history management.
- `templates`: HTML templates used to render pages.
- `manage.py`: Django command-line utility.
- `requirements.txt`: List of required Python packages.

## Contribution

Feel free to contribute to this project by creating issues or submitting pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License.

---

For any questions or assistance, please contact shantanujha505@gmail.com.



