# Resume Parser

A web application that parses, structures, and analyzes resumes using AI. This tool helps extract key information from resumes and generates structured reports.

## Features

- Resume parsing from various document formats (PDF, DOCX)
- Extraction of key information including:
  - Personal details
  - Education
  - Work experience
  - Skills
  - Projects
  - Certifications
- Structured output generation
- Web-based user interface for easy interaction

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Processing**: Google Gemini API
- **Document Processing**: Python-docx, PyPDF2

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Setup

1. Clone the repository

   ```bash
   git clone https://github.com/Virtual4087/resume-parser.git
   cd resume-parser
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables

   - Create a `.env` file in the root directory (or copy from `.env.example`)
   - Add your Google Gemini API key and other configuration parameters:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     SECRET_KEY=your_flask_secret_key
     UPLOAD_FOLDER=uploads
     ```

5. Create required directories
   ```bash
   mkdir -p uploads
   ```

## Usage

1. Start the application

   ```bash
   python run.py
   ```

2. Open your web browser and navigate to:

   ```
   http://localhost:5000
   ```

3. Upload a resume file (PDF or DOCX)

4. View the structured analysis and download the formatted report

## Project Structure

```
resume-parser/
├── app/                    # Application package
│   ├── models/             # Data models
│   ├── routes/             # API routes
│   ├── services/           # Business logic
│   ├── static/             # Static assets (CSS, JS)
│   ├── templates/          # HTML templates
│   └── utils/              # Utility functions
├── config/                 # Configuration files
├── tests/                  # Test cases
├── uploads/                # Temporary file storage
├── .env                    # Environment variables (not in git)
├── .gitignore              # Git ignore rules
├── doc_generator.py        # Document generation module
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── structurer.py           # Data structuring module
```

## API Reference

The application exposes the following API endpoints:

- `POST /api/parse`: Upload and parse a resume
  - Request: Multipart form with 'file' field containing the resume document
  - Response: JSON with structured resume data

## Configuration

The application can be configured using environment variables:

- `GEMINI_API_KEY`: Google Gemini API key for AI processing
- `SECRET_KEY`: Flask secret key for session security
- `UPLOAD_FOLDER`: Directory where uploaded files are stored
- `DEBUG`: Enable/disable debug mode (True/False)

## Development

### Adding New Features

1. Create new routes in `app/routes/`
2. Implement business logic in `app/services/`
3. Add templates in `app/templates/`

### Running Tests

```bash
python -m pytest tests/
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions, please open an issue in the GitHub repository.
