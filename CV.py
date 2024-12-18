from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os

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

    if os.path.exists(icon_path):
        pdf.image(icon_path, x=x, y=y, w=icon_width, h=icon_height, link=link)
        pdf.set_x(x + icon_width + 3)
    else:
        print(f"Image {icon_path} not found!")

    pdf.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, link=link)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 8, description)
    
    pdf.ln(5)

# Contact Information
def add_contact_info(pdf):
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Smouha, Alexandria 21918 - 01064004599 - a7g2amer@gmail.com", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "GitHub: https://github.com/yousef2342K", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", link="https://github.com/yousef2342K")
    
    pdf.set_text_color(0, 51, 102) 
    pdf.cell(0, 10, "LinkedIn: https://www.linkedin.com/in/youssif-khalid-654b872a5", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", link="https://www.linkedin.com/in/youssif-khalid-654b872a5")
    
    pdf.ln(8)

skills = "Python, C++, Java, Dart, Bash, Unix/Linux, GIT/GitHub, Docker/Kubernetes, SQL/MySQL\n"
languages = "- Arabic: First Language\n- English: C1 Advanced"

projects = [
    ("Dijkstra Algorithm Implementation", 
    "Developed Dijkstra's algorithm in Java, optimized with priority queues and fibonnaci heap for efficiency. Integrated Java Swing for a GUI and tested on large datasets for reliability. The project demonstrates efficient pathfinding solutions applicable in transportation. Tools: Java, Java Swing, JGraphT, IntelliJ IDEA, Github.              ",
     "https://github.com/yousef2342K/Dijsktras-Algorithm-Implementation"),

    ("Backup Script",
     "Created a robust backup automation script using Bash. The script schedules regular backups, manages backup logs, and ensures data integrity. Implemented advanced error handling techniques to gracefully handle unexpected issues like network failures or permission errors. "
     "Additionally, the script incorporates features like incremental backups to save storage space and automated email notifications for backup statuses, making it highly reliable for critical data protection tasks. Tools: Bash, Linux.",
     "https://github.com/yousef2342K/backup-script-bash.git"),

    ("Currency Representation Project",
     "Built a currency formatting and representation tool in Rust. This tool ensures precise handling of floating-point operations to represent currency values accurately with minimal rounding errors. "
     "It includes support for multiple currencies, custom decimal place configurations, and region-specific formatting. Developed modular code to ensure scalability and ease of integration into existing systems, enabling seamless adoption in financial applications. Tools: Rust, Cargo, GitHub.",
     "https://github.com/yousef2342K/currency-representation-wtih-rust"),

    ("College Management System",
     "Designed and developed a comprehensive desktop-based college management system using JavaFX. The system provides functionality for managing student records, courses, and schedules through an intuitive and user-friendly interface. "
     "Integrated MySQL for data persistence and scalability, ensuring data security and integrity. The application supports advanced search and filtering options for administrators to easily manage information. Tools: JavaFX, MySQL.",
     "https://github.com/yousef2342K/JavaFxproject"),

    ("Tic Tac Toe with Alpha-Beta Pruning",
     "Implemented the Alpha-Beta Pruning algorithm to optimize decision-making in a Tic Tac Toe game. By pruning unnecessary branches in the decision tree, the AI opponent can make efficient and intelligent moves. "
     "The project explores artificial intelligence concepts and demonstrates the effective use of the Minimax algorithm. Additionally, added features like a graphical interface using Pygame, enabling users to interact and compete against the AI. Tools: Python, Pygame.",
     "https://github.com/yousef2342K/TIC-TAC-TOE-Using-Min-Max-and-Alpha-beta"),

    ("CV Generated Using Python",
     "This CV was programmatically generated using Python's FPDF library, demonstrating expertise in document automation and dynamic content creation. "
     "The script incorporates features like sections for experience, projects, and skills, with support for colored links and icons for better readability. This project showcases the practical application of Python for automated reporting and document generation. Tools: Python, FPDF.",
     "https://github.com/yousef2342K/MY_CV_USING_PFDF")
]

pdf = PDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)


add_contact_info(pdf)

# Summary Section
add_section_title(pdf, "Summary")
summary_text = (
    "Highly motivated and detail-oriented software engineering student with strong expertise in programming languages like C++, Java, "
    "and Rust. Adept at designing efficient algorithms and building scalable systems. Proven experience in delivering "
    "well-structured, maintainable code for real-world projects, including backup automation, pathfinding algorithms, and desktop applications. "
    "Strong team player with hands-on experience in modern tools such as Docker, Kubernetes, and Git. Passionate about problem-solving, "
    "innovation, and leveraging technology to deliver impactful solutions."
)
pdf.set_font("Helvetica", size=10)
pdf.multi_cell(0, 8, summary_text)
pdf.ln(8)

# Experience Section
add_section_title(pdf, "Experience")
pdf.set_font("Helvetica", size=10)
pdf.set_text_color(0, 51, 102)
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 7, "Semicolon\n")
pdf.set_font("Helvetica", size=10)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 8, "January 2023 to April 2023 - Machine Learning Intern\n- Developed machine learning models and algorithms for predictive analytics.\n- Conducted data pre-processing operations such as feature engineering, normalization, and imputation.")
pdf.ln(2)

pdf.set_text_color(0, 51, 102)
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, "I-Code\n")
pdf.set_font("Helvetica", size=10)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 7, "June 2022 to October 2022 - Flutter Intern\n- Proficient in Flutter framework and Dart programming language.\n- Strong understanding of mobile app development concepts and best practices.\n- Experience with RESTful APIs, Firebase, and other relevant technologies.")
pdf.ln(4)


pdf.set_text_color(0, 51, 102)
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, "ITI - PHP Laravel Track (1 Month)\n")
pdf.set_font("Helvetica", size=10)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 7, "July 2024 to August 2024 - PHP Laravel Developer Track\n- Completed a 1-month PHP Laravel track focusing on backend development.\n- Gained practical experience in building web apps with PHP, Laravel, and MySQL.")
pdf.ln(4)


# Projects Section
add_section_title(pdf, "Projects")
icon_path = "github.png"
for i, (title, description, link) in enumerate(projects):
    add_project_with_icon(pdf, title, description, link, icon_path)
    

# Skills Section
add_section_title(pdf, "Skills")
pdf.set_font("Helvetica", size=10)
pdf.multi_cell(0, 8, skills)

# Languages Section
add_section_title(pdf, "Languages")
pdf.set_font("Helvetica", size=10)
pdf.multi_cell(0, 8, languages)

output_path_final = "YoussifKhalid_CV.pdf"
pdf.output(output_path_final)

