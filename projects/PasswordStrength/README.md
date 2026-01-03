# PasswordStrength.py

# About the project
The goal of this program is for users to interact with a menu in order to enter a password that is between (8-10) characters requiring 1 upper, 1 lower case letters and 1 number. The next option users will have is to pick between a dictionary attack and a brute force attack (estimate) done by john the ripper

# Built with
1) Github cli and Github pages (To code and host)
2) Streamlit (to host the project on -> app)
3) Python (main coding language)
4) hashlib(Python library for password hashing)
5) Streamlit (hosting platform for project)
6) RockYou.txt (Dictionary wordlist)
7) linux/ubuntu (OS)

### Prerequisites

* Python 3.8 or higher
* Linux/Ubuntu environment (or WSL on Windows)
* Git for cloning the repository

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/twizzymeowth/CybersecurityCodingPortfolio.git
   ```

2. Navigate to the project directory
   ```sh
   cd CybersecurityCodingPortfolio/projects/PasswordStrength
   ```

3. Install Python dependencies
   ```sh
   pip install streamlit
   ```

4. Install John the Ripper (Ubuntu/Debian)
   John the Ripper folder is in projects/PasswordStrength

5. Download RockYou wordlist (if not already present)
   ```sh
   wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
   ```
   Or use the included rockyou.txt file in the project directory.

6. Verify John the Ripper installation
   ```sh
   john --version
   ```
## Project Structure

```
PasswordStrength/
├── PasswordStrength.py    # Main application file
├── README.md              # Project documentation
├── hashfile.txt          # Temporary hash storage
├── rockyou.txt           # Dictionary wordlist
├── requirements.txt      # Python dependencies
└── john/                 # John the Ripper directory
```

## How It Works

1. **Password Validation**: Checks password against security requirements
2. **Hashing**: Converts password to SHA-256 hash
3. **Attack Simulation**: 
   - Dictionary: Compares against known passwords
   - Brute Force: Calculates time based on character space
4. **Results**: Displays estimated crack time and security rating

## Methodology
1) 