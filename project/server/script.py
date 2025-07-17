from google import genai
import os
from dotenv import load_dotenv
from fpdf import FPDF
import uuid

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
 
course_map = {
        0: "Technology",
        1: "Medicine",
        2: "Business",
        3: "Engineering",
        4: "Journalism",
        5: "Fine Arts",
        6: "Music",
        7: "Law",
        8: "Architecture",
        9: "Surprise Me!"
    }
#PROMPT TEMPLATE
PROMPT_TEMPLATE = """
You're a seasoned social media strategist who specializes in TikTok trends for student organizations, university clubs, and academic societies.

You are provided with a dataset (.csv file) containing detailed information on the top-performing TikTok videos from various student organizations across different majors. Each entry includes org name, major/department, followers, engagement metrics, video themes, hashtags used, audio used, and post times.

Your task is to generate a concise, actionable, and professional **1-page marketing report** tailored for the following student organization:

- 📌 Org Name: {org_name}
- 🎓 Major/Department: {major}

---

Your report must include the following:
Prepared by: SWS3023_2 

### 1. **Performance Benchmarking**
- Identify and list **3–5 viral TikTok videos** from student organizations in the *same or similar major*.
- Include org name, theme, engagement rate, and one notable content or trend element (e.g., popular sound, format, or style).

### 2. **Strategic Content Recommendation**
- Write a **1-paragraph suggestion** on what TikTok strategy this org should adopt.
- Base your recommendation on:
  - Common trends used by top-performing orgs in the same field
  - Current content style of this org (assumed from context or follower count)
  - Any content gaps or opportunities (e.g., not using trending sounds, not posting at optimal times)

### 3. **Suggested Hashtags & Audios**
- Provide a short list (3–5) of **recommended hashtags and audios** they can consider using in future posts.

Keep the tone professional but engaging. The final report should be visually skimmable, clear, brief, and tailored specifically for the org's academic focus.
**IMPORTANT: Respond with ONLY the report content. Do NOT include any introductory phrases, conversational text, dates, or objectives outside of the report itself.**
"""

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
    full_prompt = PROMPT_TEMPLATE.format(
        org_name=org_name,
        major=major,
        csv_data=csv_data
    )

    print("\n--- Sending request to Gemini API ---")
    print(f"Target Org: {org_name}, Major: {major}")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=full_prompt
        )
        if response and response.text:
            return response.text
        else:
            return "Error: Gemini API did not return a valid report."
    except Exception as e:
        return f"Error: Failed to generate report. {e}"

def create_pdf_report(report_text: str, org_name: str, major: str, output_folder="reports/", logo_path="yumeilogo.png") -> str:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filename = f"TikTok_Marketing_Report_{uuid.uuid4().hex[:8]}.pdf"
    filepath = os.path.join(output_folder, filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Logo and title
    if logo_path and os.path.exists(logo_path):
        try:
            pdf.image(logo_path, x=10, y=10, w=20, h=20)
        except Exception as e:
            print(f"Warning: Couldn't add logo. {e}")

    pdf.set_font("Arial", 'B', 16)
    pdf.set_xy(35, 15)
    pdf.multi_cell(0, 10, f"TikTok Marketing Report for {org_name} ({major})", align='L')
    pdf.ln(10)
    pdf.set_font("Arial", size=10)

    for line in report_text.split('\n'):
        line = line.strip()
        stripped_line = line.strip()
        if line.startswith("### "):
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 7, line.replace("### ", ""), align='L')
            pdf.set_font("Arial", size=10)
            pdf.ln(1)
        elif line.startswith("## "):
            pdf.set_font("Arial", 'B', 14)
            pdf.multi_cell(0, 8, line.replace("## ", ""), align='L')
            pdf.set_font("Arial", size=10)
            pdf.ln(2)
        elif line.startswith("* "):
            pdf.multi_cell(0, 5, "   " + line, align='L')
        elif '**' in stripped_line: # NEW: Check if the line contains bold markdown anywhere
            processed_line_for_bold = stripped_line.replace('**', '') # Remove asterisks
            pdf.set_font("Arial", 'B', 10) # Set font to bold for this line
            pdf.multi_cell(0, 5, processed_line_for_bold, align='L')
            pdf.set_font("Arial", '', 10) # Reset font to regular
        elif line:
            pdf.multi_cell(0, 5, line, align='L')
        else:
            pdf.ln(2)
            
     # --- Add Static Section: Engagement Insights ---
    pdf.add_page()
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 8, "4. Engagement Insights", align='L')
    pdf.set_font("Arial", size=10)
    pdf.ln(2)
    insights = [
        "Based on a correlation analysis of likes, shares, and comments across TikTok videos:",
        "- Likes & Comments are strongly correlated (0.66), suggesting that engaging videos often generate conversation.",
        "- Likes & Shares have a moderate correlation (0.45), meaning popular videos are somewhat likely to be shared.",
        "- Shares & Comments show weak correlation (0.24), indicating viewers may share content without leaving feedback."
    ]
    for item in insights:
        pdf.multi_cell(0, 5, item, align='L')
    pdf.ln(5)

    # --- Add Heatmap Image ---
    heatmap_path = "heatmap.png"
    if os.path.exists(heatmap_path):
        try:
            pdf.image(heatmap_path, x=25, y=pdf.get_y(), w=160)
        except Exception as e:
            print(f"Warning: Couldn't insert heatmap. {e}")
    else:
        print("Warning: correlation_heatmap.png not found in working directory.")

    # --- Save PDF ---
    try:
        pdf.output(filepath)
        print(f"PDF saved at {filepath}")
        return filename
    except Exception as e:
        return f"Error saving PDF: {e}"