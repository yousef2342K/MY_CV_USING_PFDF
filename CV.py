from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font("Helvetica", "B", 18)
            self.set_text_color(0, 0, 0)
            self.cell(0, 10, "Youssif Khalid - CV", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def add_section_title(pdf, title):
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(4)

def add_project_with_icon(pdf, title, description, link, icon_path):
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)

    x = pdf.get_x()
    y = pdf.get_y()
    icon_width = 5
    icon_height = 5


    try:
        pdf.image(icon_path, x=x, y=y + 1, w=icon_width, h=icon_height, link=link)
        pdf.set_x(x + icon_width + 2)
    except FileNotFoundError:
        pdf.set_x(x)

    pdf.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, link=link)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 8, description)
    pdf.ln(5)

skills = "Python, C++, Java, Dart, Bash, Unix/Linux, GIT/GitHub, Docker/Kubernetes, SQL/MySQL\n"
languages = "- Arabic: First Language\n- English: C1 Advanced"

projects = [
    ("Dijkstra Algorithm Implementation", 
     "Developed an efficient implementation of Dijkstra's shortest path algorithm in Java. Optimized for pathfinding problems, the algorithm minimizes computational complexity using priority queues and adjacency matrices. Tools: Java, IntelliJ IDEA, GitHub.",
     "https://github.com/yousef2342K/Dijsktras-Algorithm-Implementation"),

    ("Backup Script",
     "Created a robust backup automation script using Bash. The script schedules regular backups, manages backup logs, and ensures data integrity. Implemented error handling and automated email notifications for successful or failed backups. Tools: Bash, Linux.",
     "https://github.com/yousef2342K/backup-script-bash.git"),

    ("Currency Representation Project",
     "Built a currency formatting and representation tool in Rust. The tool ensures precise handling of floating-point operations to represent currency values accurately with minimal rounding errors. It also supports various currencies and decimal places. Tools: Rust, GitHub.",
     "https://github.com/yousef2342K/currency-representation-wtih-rust"),

    ("College Management System",
     "Designed and developed a desktop-based college management system using JavaFX. The system tracks student records, courses, and schedules with a user-friendly interface. It supports data persistence through MySQL and is designed for easy scalability. Tools: JavaFX, MySQL.",
     "https://github.com/yousef2342K/JavaFxproject"),

    ("Tic Tac Toe with Alpha-Beta Pruning",
     "Implemented the Alpha-Beta Pruning algorithm to optimize decision-making in a Tic Tac Toe game. The AI opponent can now make smarter choices by pruning unnecessary branches in the decision tree. Tools: Python, Pygame.",
     "https://github.com/yousef2342K/TIC-TAC-TOE-Using-Min-Max-and-Alpha-beta"),

    ("CV Generated Using Python",
     "This CV was programmatically generated using Python's FPDF library, demonstrating skills in coding and document automation. It includes dynamic sections for experience, projects, and skills. Tools: Python, FPDF.",
     "https://github.com/yousef2342K/MY_CV_USING_PFDF")
]


pdf = PDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

# Contact Information
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, "Smouha, Alexandria 21918 - 01064004599 - a7g2amer@gmail.com", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.cell(0, 10, "LinkedIn: https://www.linkedin.com/in/youssif-khalid-654b872a5", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", link="https://www.linkedin.com/in/youssif-khalid-654b872a5")
pdf.cell(0, 10, "GitHub: https://github.com/yousef2342K", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", link="https://github.com/yousef2342K")
pdf.ln(8)

# Experience Section
add_section_title(pdf, "Experience")
pdf.set_font("Helvetica", size=10)
pdf.multi_cell(0, 8, "Semicolon\nJanuary 2023 to April 2023 - Machine Learning Intern\n- Developed machine learning models and algorithms for predictive analytics.\n- Conducted data pre-processing operations such as feature engineering, normalization, and imputation.")
pdf.ln(2)
pdf.multi_cell(0, 8, "I Code\nJune 2022 to October 2022 - Flutter Intern\n- Proficient in Flutter framework and Dart programming language.\n- Strong understanding of mobile app development concepts and best practices.\n- Experience with RESTful APIs, Firebase, and other relevant technologies.")
pdf.ln(4)

# Projects Section
add_section_title(pdf, "Projects")
icon_path = "github.png"
for i, (title, description, link) in enumerate(projects):
    if i == 2:  
        pdf.add_page()
    add_project_with_icon(pdf, title, description, link, icon_path)

# Skills Section
add_section_title(pdf, "Skills")
pdf.set_font("Helvetica", size=10)
pdf.multi_cell(0, 8, skills)

# Languages Section
add_section_title(pdf, "languages")
pdf.set_font("Helvetica", size=10)
pdf.multi_cell(0, 8, languages)


output_path_final = "YoussifKhalid_CV.pdf"
pdf.output(output_path_final)
