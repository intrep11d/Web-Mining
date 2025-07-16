from google import genai
import os
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#PROMPT TEMPLATE
PROMPT_TEMPLATE = """
You're a seasoned social media strategist who specializes in TikTok trends for student organizations, university clubs, and academic societies.

You are provided with a dataset (.csv file) containing detailed information on the top-performing TikTok videos from various student organizations across different majors. Each entry includes org name, major/department, followers, engagement metrics, video themes, hashtags used, audio used, and post times.

Your task is to generate a concise, actionable, and professional **1-page marketing report** tailored for the following student organization:

- 📌 Org Name: {org_name}
- 🎓 Major/Department: {major}

---

Your report must include the following:

### 1. **Performance Benchmarking**
- Identify and list **3–5 viral TikTok videos** from student organizations in the *same or similar major*.
- Include org name, theme, engagement rate, and one notable content or trend element (e.g., popular sound, format, or style).

### 2. **Visual Trend Snapshot**
- Suggest a **bar chart or pie chart** visualizing popular video themes, top-used hashtags, or peak posting times based on the CSV dataset. Describe what this chart would show.

### 3. **Strategic Content Recommendation**
- Write a **1-paragraph suggestion** on what TikTok strategy this org should adopt.
- Base your recommendation on:
  - Common trends used by top-performing orgs in the same field
  - Current content style of this org (assumed from context or follower count)
  - Any content gaps or opportunities (e.g., not using trending sounds, not posting at optimal times)

### 4. **Suggested Hashtags & Audios**
- Provide a short list (3–5) of **recommended hashtags and audios** they can consider using in future posts.

Keep the tone professional but engaging. The final report should be visually skimmable, clear, brief, and tailored specifically for the org's academic focus.
"""

# --- Sample Data for Testing ---
# In a real application, you would load this from a CSV file or a database.
# For this script, we're hardcoding it for demonstration purposes.
ORG_NAME = "University Robotics Club"
MAJOR_DEPARTMENT = "Engineering"
SAMPLE_CSV_DATA = """
org_name,major/department,followers,engagement_rate,video_theme,hashtags,audio_used,post_time
Student Coders,Computer Science,15000,0.08,Coding Challenge,['#codingchallenge','#compsci'],Upbeat Synth,Tue 3 PM
AI Innovators,Computer Science,22000,0.12,AI Explained,['#AI','#MachineLearning'],Tech Groove,Wed 4 PM
Data Science Society,Data Science,18000,0.09,Data Viz Tutorial,['#DataScience','#Tutorial'],Chill Lo-fi,Mon 2 PM
Engineering Club,Engineering,10000,00.05,Build Showcase,['#Engineering','#DIY'],Energetic Pop,Thu 5 PM
Robotics Team,Engineering,25000,0.15,Robot Dance,['#Robotics','#Dance'],Trending Pop Song,Fri 6 PM
Mechanical Marvels,Engineering,19000,0.11,Robot Competition Prep,['#Robotics','#Engineering'],Motivational Beat,Wed 2 PM
Electrical Engineers,Engineering,12000,0.07,Circuit Board Art,['#Electronics','#Art'],Chill Lo-fi,Mon 4 PM
Mathletes,Mathematics,5000,0.03,Math Hacks,['#MathTips','#StudyHacks'],Calm Ambient,Tue 1 PM
Physics Society,Physics,7000,0.04,Experiment Gone Wrong,['#Physics','#ScienceFun'],Funny Sound,Wed 11 AM
"""


def generate_tiktok_report_text(org_name: str, major: str, csv_data: str) -> str:
    """
    Generates the TikTok marketing report text using the Gemini API.

    Args:
        org_name (str): The name of the student organization.
        major (str): The major/department of the organization.
        csv_data (str): The simulated CSV dataset as a string.

    Returns:
        str: The generated report text, or an error message if generation fails.
    """
    full_prompt = PROMPT_TEMPLATE.format(
        org_name=org_name,
        major=major,
        csv_data=csv_data
    )

    print("\n--- Sending request to Gemini API ---")
    print(f"Target Org: {org_name}, Major: {major}")

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash", # Using gemini-1.5-flash as requested
            contents=full_prompt
        )
        # Check if the response contains text
        if response and response.text:
            return response.text
        else:
            print(f"Gemini API response was empty or malformed: {response}")
            return "Error: Gemini API did not return a valid report."
    except Exception as e:
        print(f"An error occurred during Gemini API call: {e}")
        return f"Error: Failed to generate report from AI. Details: {e}"

def create_pdf_report(report_text: str, org_name: str, major: str, filename: str = "TikTok_Marketing_Report.pdf", logo_path: str = None):
    """
    Creates a PDF file from the generated report text, with the yumei logo
    Args:
        report_text (str): The text content of the report.
        org_name (str): The name of the organization (for PDF title).
        major (str): The major (for PDF title).
        filename (str): The name of the output PDF file.
        logo_path (str, optional): Path to the logo image file (e.g., 'logo.png').
                                    If provided, the logo will be added to the top-left.
                                    Requires 'Pillow' library to be installed.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Set standard font for all content
    pdf.set_font("Arial", size=12)

    # Coordinates for logo and title
    logo_x = 10
    logo_y = 10
    logo_width = 20 # Adjust as needed
    logo_height = 20 # Adjust as needed

    title_x_offset = logo_x + logo_width + 5 # 5 units spacing between logo and title
    title_y = logo_y + (logo_height / 2) - 5 # Center title vertically with logo, adjust -5 as needed

    # Add logo if path is provided
    if logo_path and os.path.exists(logo_path):
        try:
            pdf.image(logo_path, x=logo_x, y=logo_y, w=logo_width, h=logo_height)
        except Exception as e:
            print(f"Warning: Could not add logo from '{logo_path}'. Error: {e}")
    elif logo_path: # Only warn if path was provided but file not found
        print(f"Warning: Logo file not found at '{logo_path}'. Skipping logo.")

    # TITLE BESIDE THE LOGO
    pdf.set_font("Arial", 'B', 16) # Set font for main title
    pdf.set_xy(title_x_offset, title_y)
    pdf.multi_cell(0, 10, f"TikTok Marketing Report for {org_name} ({major})", align='L') # Align left
    pdf.ln(5) # Reduced space after the title

    pdf.set_font("Arial", size=10) 
    
    lines = report_text.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('### '):
            heading_text = stripped_line.replace('### ', '')
            pdf.set_font("Arial", 'B', 12) # Set bold font for headings
            pdf.multi_cell(0, 7, heading_text, align='L') # No emoji, reduced line height
            pdf.set_font("Arial", size=10) # Reset font to regular for next lines
            pdf.ln(1) # Reduced line break after heading
        elif stripped_line.startswith('## '):
            pdf.set_font("Arial", 'B', 14) # Set bold font for H2 headings
            pdf.multi_cell(0, 8, stripped_line.replace('## ', ''), align='L') # Reduced line height
            pdf.set_font("Arial", size=10) # Reset font to regular for next lines
            pdf.ln(2) # Reduced line break after heading
        elif stripped_line.startswith('* '): # For bullet points
            pdf.multi_cell(0, 5, "   " + stripped_line, align='L') # Reduced line height, indent bullet points
        elif stripped_line: # Only process non-empty lines that aren't headings or bullets
            pdf.multi_cell(0, 5, stripped_line, align='L') # Reduced line height for regular text
        else: # Handle empty lines for spacing
            pdf.ln(2) # Reduced line break for empty lines

    try:
        pdf.output(filename)
        print(f"\nPDF report '{filename}' generated successfully!")
    except Exception as e:
        print(f"Error generating PDF: {e}")

# --- Main execution ---
if __name__ == "__main__":

    LOGO_FILE = "yumeilogo.png" 

    generated_report_text = generate_tiktok_report_text(ORG_NAME, MAJOR_DEPARTMENT, SAMPLE_CSV_DATA)

    if "Error:" not in generated_report_text:
        print("\n--- Generated Report Text (for verification) ---")
        print(generated_report_text)

        create_pdf_report(generated_report_text, ORG_NAME, MAJOR_DEPARTMENT, logo_path=LOGO_FILE)
    else:
        print(generated_report_text)