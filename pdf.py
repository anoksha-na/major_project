import random
from fpdf import FPDF
from datetime import datetime

# Stored prediction from previous context
stored_prediction = "scc"  # Example stored prediction, replace as needed

# Conditions details based on stored context
conditions = {
    "normal": {
        "info": [
            "The lung tissue appears normal with no visible signs of cancer or other significant abnormalities. Regular screening and preventive measures are recommended.",
            "Maintain a healthy lifestyle with regular exercise and a balanced diet.",
            "If you smoke, consider a smoking cessation program.",
            "Be aware of any changes in respiratory health and report them to your doctor.",
            "Consider regular screening if you are in a high-risk group."
        ],
        "recommendations": [
            "Continue regular health check-ups as recommended by your healthcare provider.",
            "Maintain a healthy lifestyle with regular exercise and a balanced diet.",
            "If you smoke, consider a smoking cessation program.",
            "Be aware of any changes in respiratory health and report them to your doctor.",
            "Consider regular screening if you are in a high-risk group."
        ]
    },
    "aca": {
        "info": [
            "Adenocarcinoma is detected, which is a type of non-small cell lung cancer typically occurring in the outer parts of the lung. It's the most common type of lung cancer in non-smokers and women.",
            "Schedule an immediate consultation with an oncologist.",
            "Additional imaging tests may be needed for precise staging.",
            "Consider genetic testing for potential targeted therapy options.",
            "Discuss treatment plan options including surgery, chemotherapy, and targeted therapy.",
            "Join a support group for lung cancer patients."
        ],
        "recommendations": [
            "Schedule an immediate consultation with an oncologist.",
            "Additional imaging tests may be needed for precise staging.",
            "Consider genetic testing for potential targeted therapy options.",
            "Discuss treatment plan options including surgery, chemotherapy, and targeted therapy.",
            "Join a support group for lung cancer patients."
        ]
    },
    "scc": {
        "info": [
            "Squamous cell carcinoma is detected, a type of non-small cell lung cancer typically occurring in the central part of the lungs near the bronchi. It's strongly associated with smoking history.",
            "Immediate consultation with an oncologist is required.",
            "If you smoke, immediate smoking cessation is crucial.",
            "Complete staging workup will be needed.",
            "Discuss treatment options including surgery, radiation, and chemotherapy.",
            "Consider a pulmonary rehabilitation program."
        ],
        "recommendations": [
            "Immediate consultation with an oncologist is required.",
            "If you smoke, immediate smoking cessation is crucial.",
            "Complete staging workup will be needed.",
            "Discuss treatment options including surgery, radiation, and chemotherapy.",
            "Consider a pulmonary rehabilitation program."
        ]
    }
}

# Function to create PDF
def create_pdf(prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the condition details based on the prediction
    condition_info = conditions.get(prediction, {})
    info = condition_info.get("info", [])
    recommendations = condition_info.get("recommendations", [])

    # Ensure there's at least one info point
    if info:
        first_info = info[0]
        remaining_info = info[1:]  # All but the first point
        selected_info = random.sample(remaining_info, min(2, len(remaining_info)))  # Randomly select 2 from remaining
        selected_info.insert(0, first_info)  # Insert the first point at the beginning
    else:
        selected_info = []

    # Select 3 random recommendations
    selected_recommendations = random.sample(recommendations, min(3, len(recommendations)))

    # Add information to PDF
    pdf.cell(200, 10, txt="Lung Condition Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Prediction: {prediction.capitalize()}", ln=True)
    pdf.cell(200, 10, txt=f"Report Generated On: {current_time}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)  # Empty line

    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Info:", ln=True)
    pdf.set_font("Arial", size=12)
    for info_point in selected_info:
        pdf.multi_cell(0, 10, txt=info_point)
    pdf.cell(200, 10, txt="", ln=True)  # Empty line

    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Recommendations:", ln=True)
    pdf.set_font("Arial", size=12)
    for recommendation in selected_recommendations:
        pdf.cell(0, 10, txt=f"- {recommendation}", ln=True)

    # Save the PDF to a file
    pdf_file_path = "C:/Users/Ananya/Desktop/pdf_check/lung_condition_report.pdf"
    pdf.output(pdf_file_path)

    return pdf_file_path

# Create the PDF based on the stored prediction
pdf_file = create_pdf(stored_prediction)

pdf_file
