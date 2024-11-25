# DevOps Pro Course Scraper

Python script to extract course information and video URLs from the DevOps Pro platform. The script automatically maps all courses and their content, saving the structure to a JSON file.

## Features

- Complete course content extraction
- Automatic handling of gzipped content
- Organized JSON output with course hierarchy
- Progress logging with pretty print
- Base64 and gzip decompression handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/OtaviOuu/devops-pro-scraper
cd devopspro-scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Copy the environment example file:
```bash
cp .env.example .env
```

2. Get the authorization token:
   - Go to https://plataforma.devopspro.com.br/courses
   - Open Developer Tools (F12)
   - Go to Network tab
   - Refresh the page
   - Find "contracts" in the requests
   - In Headers > Request Headers, copy the "authorization" value
   - Paste it into the `.env` file

## Usage

Run the script:
```bash
python src/main.py
```

The script will:
1. Iterate through all course IDs
2. Extract and decompress course data
3. Generate a `devops-pro.json` file with the structure:
```json
{
    "Course Name": {
        "[ID] Module Name": {
            "[ID] Lecture Title": "Video URL",
            ...
        },
        ...
    },
    ...
}
```

## Project Structure
```
.
├── README.md
├── requirements.txt
└── src
    └── main.py
```

## Dependencies

- requests: HTTP requests handling
- python-dotenv: Environment variables management
- Other standard library modules: gzip, base64, json, pprint

## Notes

- Active subscription required on DevOps Pro platform
- Authorization token expires periodically and needs to be updated
- Script processes over 1000 potential course IDs
- Content is gzipped and base64 encoded by the platform

## Responsibility Statement

This tool is provided for educational and personal use only. Users are responsible for:

- Having a valid subscription to the DevOps Pro platform
- Using the tool in accordance with the platform's terms of service
- Not distributing or sharing any extracted content
- Using the data in compliance with DevOps Pro's policies
- Maintaining the confidentiality of their authorization tokens

The developer(s) assume no liability for any misuse of this tool or violation of terms of service. Use at your own discretion and responsibility.
