import tkinter as tk
from tkinter import ttk

# Datos del CV
cv_data = {
    "name": "Javier Ignacio Monasterio Solar",
    "email": "javiermonasterio@gmail.com",
    "work_experience": [
        {
            "position": "RPA Analyst",
            "company": "Cibernos -Conasa",
            "duration": "Currently",
            "description": "Leading functional raising for new processes, documentation, production passes, maintenance, and evolutions in RPA projects with UiPath Studio, Orchestrator, and more."
        },
        {
            "position": "RPA Developer",
            "company": "NAHITEK",
            "duration": "2022 - 2023",
            "description": "RPA development for insurance and public administration projects using UiPath Studio, Orchestrator, and other technologies."
        },
    ],
    "languages": [
        {"name": "German", "proficiency": "Basic"},
        {"name": "English", "proficiency": "Intermediate"}
    ],
    "certifications": [
        {"title": "UiPath Certified Professional Automation Developer Professional", "institution": "UiPath", "year": None},
        {"title": "UiPath Certified Professional Specialized AI Professional", "institution": "UiPath", "year": None}
    ],
    "education": [
        {"degree": "Degree in Telecommunications", "institution": "Universidad Politécnica de Madrid", "year_of_completion": 2016, "description": None},
        {"degree": "Biomedical Digital Signal Processing Course", "institution": "Polytechnic University of Madrid", "year_of_completion": 2017, "description": "Coursework included Digital Signal Processing in Finland."}
    ]
}

# Crear la ventana principal
root = tk.Tk()
root.title("Curriculum Vitae")
root.geometry("800x600")

# Contenedor principal
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Encabezado (Nombre y Email)
header = tk.Label(main_frame, text=f"{cv_data['name']}\n{cv_data['email']}", font=("Arial", 16, "bold"), pady=10)
header.pack(anchor="w")

# Crear una sección para Work Experience
def create_section(title, items, parent):
    section_title = tk.Label(parent, text=title, font=("Arial", 14, "bold"), pady=5)
    section_title.pack(anchor="w")
    
    for item in items:
        item_frame = tk.Frame(parent, padx=10, pady=5)
        item_frame.pack(anchor="w", fill="x")
        
        for key, value in item.items():
            if value:
                line = tk.Label(item_frame, text=f"{key.capitalize()}: {value}", font=("Arial", 12))
                line.pack(anchor="w")

# Work Experience
create_section("Work Experience", cv_data["work_experience"], main_frame)

# Languages
create_section("Languages", cv_data["languages"], main_frame)

# Certifications
create_section("Certifications", cv_data["certifications"], main_frame)

# Education
create_section("Education", cv_data["education"], main_frame)

# Ejecutar la aplicación
root.mainloop()
