from google import genai
from google.genai import types
import json
import re
import os

# Configure with your API key
client = genai.Client(api_key="AIzaSyDquJr4Ph35GmvfNeKihNxGVMurky_NYqU")

# Improved schema template with dynamic skill categories
SCHEMA_TEMPLATE = """{
  "contact": {
    "name": "Asish Subedi",
    "email": "subedi0530@gmail.com",
    "phone": "(571) 648-2663",
    "linkedin": "https://www.linkedin.com/in/asisub"
  },
  "title": "Test Automation Engineer",
  "summary": "Senior Test Automation Engineer with 5+ years...",
  "technical_skills": {
    // DYNAMIC CATEGORIES FROM RESUME
    "Category Name From Resume": ["skill1", "skill2"]
  },
  "work_experience": [
    {
      "company": "Company Name",
      "location": "Location",
      "role": "Job Title",
      "dates": "MMM YYYY – Present",
      "achievements": [
        "Bullet point 1",
        "Bullet point 2"
      ]
    }
  ],
  "education": {
    "institution": "University Name",
    "location": "Location",
    "degree": "Degree Earned",
    "graduation_year": "YYYY"
  }
}"""

RULES = """STRICT CONVERSION RULES:
1. TECHNICAL SKILLS FORMAT:
   - First line after "Technical Skills:" is COLUMN HEADERS (ignore it)
   - Subsequent lines alternate between CATEGORY and SKILLS
   - Example:
     Programming Languages
     Java, C#, TypeScript
     Web Automation
     Playwright, Selenium
   → Should become:
     "technical_skills": {
       "Programming Languages": ["Java", "C#", "TypeScript"],
       "Web Automation": ["Playwright", "Selenium"]
     }
2. Group skills under their original category names
3. Keep bullet points verbatim (● symbols included)
4. CRITICAL: Maintain the EXACT order of skill categories as they appear in the original resume
5. Never modify category names
6. Handle multi-line skill entries
7. Use double quotes for all JSON strings
8. Never add comments or explanations
9. Maintain consistent date formats (MMM YYYY – MMM YYYY)
10. Return ONLY valid JSON"""

def clean_json_response(text):
    """Enhanced cleaning with Unicode handling"""
    # Remove all markdown blocks and non-JSON text
    text = re.sub(r'```json|```|\+---|●', '', text)
    
    # Fix Unicode quotes and hidden characters
    text = text.encode('utf-8').decode('unicode_escape')
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', ' ', text)
    
    # Remove trailing commas
    text = re.sub(r',(\s*[]}])', r'\1', text)
    
    # Ensure single root object
    if text.count('{') - text.count('}') == 1:
        text += '}'
    
    return text.strip()

def parse_resume(resume_text):
    prompt = f"""
    Convert this resume to JSON following this structure:
    {SCHEMA_TEMPLATE}
    
    {RULES}
    
    IMPORTANT: You must preserve the EXACT ORDER of skill categories exactly as they appear in the input text.
    
    Resume Text:
    {resume_text}
    """
    
    try:
        chat = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                max_output_tokens=4000,
                temperature=0.1,
                response_mime_type="application/json",
            )
        )

        response = chat.send_message(prompt)
        
        raw_json = response.text
        cleaned_json = clean_json_response(raw_json)
        
        # Validate JSON structure
        parsed = json.loads(cleaned_json)
        
        # Basic validation checks
        required_sections = ['contact', 'summary', 'technical_skills', 
                           'work_experience', 'education']
        for section in required_sections:
            if section not in parsed:
                raise ValueError(f"Missing section: {section}")
                
        return parsed
        
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        try:
            # Attempt to fix common issues
            cleaned_json = cleaned_json.replace('\n', '\\n')
            if '"company": "' in cleaned_json and not cleaned_json.count('"') % 2 == 0:
                cleaned_json += '"'
            parsed = json.loads(cleaned_json)
            return parsed
        except:
            print("Final repair attempt failed")
            print("Raw response:", raw_json)
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Only run this code when the script is executed directly (not when imported)
if __name__ == "__main__":
    # Console interface for direct usage
    print("Please paste your resume text below and press Enter when done:")
    resume = input("Resume: ")

    # Validate if the resume text is not empty
    if not resume.strip():
        print("Error: Resume text cannot be empty.")
        exit(1)

    # Proceed with parsing the pasted resume text
    parsed_resume = parse_resume(resume)
    if parsed_resume:
        output = json.dumps(parsed_resume, indent=2)
        print(output)
    else:
        print("Failed to parse resume.")