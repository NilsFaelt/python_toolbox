from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report():
    """Generate a pdf report"""
    try:
        report_name = input("Enter name on report:")
        title = input("Enter title: ")
        content = input("Enter content: ")
        report_name_fixed = report_name.strip() + ".pdf".strip()   
        file_path = f"reports/{report_name_fixed}"
        
        c = canvas.Canvas(file_path, pagesize=letter)

        c.setFont("Helvetica", 16)
        c.drawCentredString(300, 750, title)

        c.setFont("Helvetica", 12)
        text_object = c.beginText(100, 730)
        text_object.setTextOrigin(100, 730)

        for line in content.split('\n'):
            text_object.textLine(line)

        c.drawText(text_object)
        c.save()
        print("Report saved inside toolbox in reports directory")

    except FileNotFoundError as file_not_found_error:
        print(f"File not found error: {file_not_found_error}")
    except PermissionError as permission_error:
        print(f"Permission error: {permission_error}")

if __name__ == "__main__":
    generate_report()
