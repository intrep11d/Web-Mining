from google import genai
import os
from dotenv import load_dotenv

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

Keep the tone professional but engaging. The final report should be visually skimmable, clear, and tailored specifically for the org's academic focus.
"""


response = client.models.generate_content(
    model="gemini-1.5-flash", contents="Hi!"
)

print(response.text)