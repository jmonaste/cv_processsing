from pydantic import BaseModel
from typing import List, Optional

class Curriculum(BaseModel):
    class WorkExperience(BaseModel):  # Clase anidada para experiencia laboral
        position: str
        company: str
        duration: str
        description: Optional[str] = None  # Breve descripción opcional de las responsabilidades o logros

    class Language(BaseModel):  # Clase anidada para idiomas
        name: str
        proficiency: str  # Nivel de competencia (por ejemplo, Básico, Intermedio, Avanzado, Nativo)

    class Certification(BaseModel):  # Clase anidada para certificaciones y cursos
        title: str
        institution: str
        year: Optional[int] = None  # Año en que se obtuvo la certificación (opcional)

    class Education(BaseModel):  # Clase anidada para estudios
        degree: str
        institution: str
        year_of_completion: Optional[int] = None  # Año de finalización (opcional)
        description: Optional[str] = None  # Breve descripción del enfoque o logros

    name: str
    email: str
    work_experience: List[WorkExperience]  # Lista de experiencia laboral
    languages: List[Language]  # Lista de idiomas
    certifications: List[Certification]  # Lista de certificaciones y cursos
    education: List[Education]  # Lista de estudios
