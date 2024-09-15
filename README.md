# Credential Manager App

A secure and user-friendly desktop application for managing credentials using Windows Credential Manager.

## Features

- Securely store and manage credentials using Windows Credential Manager
- Add, edit, and delete credentials
- View all stored credentials in a table format
- Toggle password visibility for added security
- User-friendly graphical interface built with PySide6

## Requirements

- Windows 10 or later
- Python 3.7 or later
- PySide6
- pywin32

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/MichaelDeCortix/credential-manager-app.git
   cd credential-manager-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command from the project root directory:

```
python -m src.main
```

## Security Considerations

- This application uses Windows Credential Manager to securely store credentials.
- Passwords are not stored in plain text within the application.
- The application runs locally on your machine and does not transmit data over the network.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is provided "as is" without warranty of any kind. Use at your own risk.