from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from script import generate_tiktok_report_text, create_pdf_report, course_map, SAMPLE_CSV_DATA
import os
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    course_value = data.get('course_value')

    print(f"✅ Received course_value: {course_value}")

    major = course_map.get(course_value, "Unknown")
    org_name = "Your Student Org"  # You can customize this or get it from the frontend

    report_text = generate_tiktok_report_text(org_name, major, SAMPLE_CSV_DATA)

    if report_text.startswith("Error"):
        return jsonify({'error': report_text}), 500

    filename = create_pdf_report(report_text, org_name, major, logo_path="yumeilogo.png")

    if filename.startswith("Error"):
        return jsonify({'error': filename}), 500

    return jsonify({'message': "Report generated!", 'filename': filename})


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('reports', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
