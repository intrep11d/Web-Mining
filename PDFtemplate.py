from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Beauty Brand Marketing Report", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Sample Report Sections
pdf.section_title("1. Executive Summary")
pdf.section_body(
    "This general marketing report provides an overview of key strategies, market trends, and performance "
    "recommendations for a fictional beauty brand operating in 2025. The report aims to guide future campaigns, "
    "optimize brand visibility, and improve customer engagement."
)

pdf.section_title("2. Market Overview")
pdf.section_body(
    "The beauty industry continues to grow, particularly in skincare, clean beauty, and inclusive makeup offerings. "
    "Consumer preferences are leaning toward sustainability, transparency in ingredients, and influencer-backed products. "
    "Social media remains the strongest channel for brand awareness, especially platforms like TikTok and Instagram."
)

pdf.section_title("3. Target Audience")
pdf.section_body(
    "The brand targets Gen Z and Millennial consumers aged 18-34, with a focus on urban dwellers who value self-care, "
    "authentic branding, and social responsibility. This demographic is highly responsive to social proof and peer recommendations."
)

pdf.section_title("4. Social Media Performance")
pdf.section_body(
    "TikTok and Instagram Reels have driven the highest engagement, with short-form tutorials and behind-the-scenes content "
    "performing best. Influencer collaborations yielded a 35% increase in traffic to the website. Email marketing CTR averaged 8%. "
)

pdf.section_title("5. Competitor Snapshot")
pdf.section_body(
    "Major competitors include Glossier, Fenty Beauty, and Rare Beauty. These brands dominate the online space with celebrity-driven branding, "
    "community interaction, and product innovation. Our brand should emphasize unique value propositions like sustainability and affordability."
)

pdf.section_title("6. SWOT Analysis")
pdf.section_body(
    "Strengths: Strong online presence, ethical sourcing\n"
    "Weaknesses: Limited physical store reach\n"
    "Opportunities: Expand via live shopping, diversify product line\n"
    "Threats: Rising ad costs, saturation in influencer space"
)

pdf.section_title("7. Recommendations")
pdf.section_body(
    "- Invest more in TikTok creator partnerships and UGC campaigns.\n"
    "- Launch a limited-edition product with a micro-influencer.\n"
    "- Run seasonal promotions tied to skin or makeup concerns.\n"
    "- Use email segmentation to increase repeat purchases."
)

pdf_output_path = "/mnt/data/beauty_brand_marketing_report.pdf"
pdf.output(pdf_output_path)
pdf_output_path
