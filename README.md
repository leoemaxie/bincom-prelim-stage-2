# bincom-prelim-stage-2
## Project Description

This project is a preliminary stage for the Bincom technical assessment. It involves setting up a Python environment using `venv` and installing necessary packages listed in `requirements.txt`.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).

### Setting Up the Virtual Environment

1. Clone the repository:
    ```sh
    git clone https://github.com/leoemaxie/bincom-prelim-stage-2.git
    cd bincom-prelim-stage-2
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

To run the project, ensure that your virtual environment is activated and execute the main script:
```sh
```sh
export FLASK_APP=app.py
flask run
```

## Project Structure

## Project Structure

```
bincom-prelim-stage-2/
│
├── requirements.txt        # List of required packages
├── app.py                  # Main application script
├── config.py               # Configuration settings
├── models.py               # Database models
├── templates/              # HTML templates for the web application
│   ├── index.html          # Homepage template
│   ├── polling_unit_result.html  # Template for polling unit results
│   ├── lga_result.html     # Template for local government area results
│   └── new_polling_unit.html  # Template for adding a new polling unit
├── README.md               # Project documentation
└── ...                     # Other project files
```


## Contact

For any questions or inquiries, please contact [leoemaxie@gmail.com](mailto:leoemaxie
@gmail.com.com).