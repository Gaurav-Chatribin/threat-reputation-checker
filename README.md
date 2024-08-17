# IP and Domain Threat Reputation Checker

This Flask application allows users to check the reputation of IP addresses and domain names using the VirusTotal and AbuseIPDB APIs. The application provides a user-friendly interface to input single or multiple IPs or domains and displays the results in a structured format.

![image](https://github.com/user-attachments/assets/63e21b74-ab58-4453-a72e-2a1eee3121d1)

## Features

- **Toggle between IP and Domain checks:** Users can choose to check either IP addresses or domain names.
- **Input validation:** The application handles errors for empty inputs or incorrect formats, providing informative messages.
- **Dynamic result display:** The reputation results are displayed in a well-structured and styled format.
- **Modular code:** API calls and other functionalities are separated into different modules for better maintainability.

## Requirements

- Python 3.8 or higher
- Flask
- Requests

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Gaurav-Chatribin/threat-reputation-checker.git
   cd ip-domain-reputation-checker

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API keys:**

    Replace the API_KEY in config.py file in the root directory with the following content:

    ```python
    VIRUSTOTAL_API_KEY = 'your_virustotal_api_key'
    ABUSEIPDB_API_KEY = 'your_abuseipdb_api_key'
    ```

5. **Run the application:**
    Change the directory to the root directory of the cloned project and run the following command:
    
    ```bash
    python app.py
    ```

6. **Access the application:**
    Open a browser and navigate to http://127.0.0.1:5000/.

## Usage

   - Enter an IP address or domain name in the search box.
   - Choose the appropriate option (IP or Domain).
   - Click on the "Check Reputation" button.
   - View the results in the dynamically generated result boxes.

## Error Handling

   - If the input is empty, an error message will prompt you to enter an IP or domain.
   - If you select "IP" but enter a domain, or vice versa, an error message will inform you of the mismatch and guide you to correct it.

## License

   This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

   If you have suggestions or want to contribute, please create an issue or submit a pull request.

## Contact

- **Author**: Gaurav Chatribin
- **Email**: gauravchatribin58@gmail.com
- **GitHub**: [Gaurav-Chatribin](https://github.com/Gaurav-Chatribin)
