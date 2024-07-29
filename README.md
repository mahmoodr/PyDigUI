# PyDigUI

PyDigUI is a simple graphical user interface (GUI) for the `dig` command line tool, written in Python. It allows users to easily perform DNS lookups using a visual interface.

## Requirements
- Python 3.x
- `tkinter` module (usually included with Python)
- `dig` command line tool (part of the `bind-utils` package on most Linux distributions)

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/mahmoodr/pydigui.git
    cd pydigui
    ```

2. **Ensure `dig` is installed:**
    - On Debian/Ubuntu:
      ```bash
      sudo apt-get install dnsutils
      ```
    - On Red Hat/CentOS:
      ```bash
      sudo yum install bind-utils
      ```

3. **Run the application:**
    ```bash
    python PyDiUI.py
    ```

## Usage
1. **Domain:** Enter the domain name you want to query.
2. **Record Type:** Select the type of DNS record you want to query (e.g., A, AAAA, CNAME, MX, etc.).
3. **DNS Server (optional):** Specify a DNS server to use for the query (e.g., 8.8.8.8 for Google's DNS).
4. **Additional Options:** Add any additional options for the `dig` command (default is `+short`).
5. **Run Dig:** Click the "Run Dig" button to execute the query. The output will be displayed in the output text area.

## License
This project is licensed under the MIT License
