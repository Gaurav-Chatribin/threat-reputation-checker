# IP and Domain Threat Reputation Checker

This Flask application is designed to provide users with a convenient way to assess the reputation of an IP address or domain name through the integration of VirusTotal, AbuseIPDB, Criminal IP, and Whoislookup APIs. By offering a user-friendly interface, the application allows users to input a single IP or domain and receive comprehensive results on a single page. This streamlined process of gathering threat-related information saves valuable time, particularly during urgent and time-critical investigations.

![image](https://github.com/user-attachments/assets/a47d208f-e962-4a90-8cb4-2dfc412b626c) 
![image](https://github.com/user-attachments/assets/51a00a73-446e-4991-904a-25c3b0205fbe)


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

    Create a file in the root directory. Name it "config.py" and paste the API_KEY file as per the format mentioned below:

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
