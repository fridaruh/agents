from pathlib import Path
import markdown
import pdfkit
from datetime import datetime
from typing import List

class ReportGenerator:
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_pdf(self, content: str, prefix: str = "aml_report") -> str:
        """Convert markdown content to PDF with styling"""
        # Convertir markdown a HTML
        html_content = markdown.markdown(content)
        
        # Agregar estilos básicos
        styled_html = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1 {{ color: #2c3e50; }}
                    h2 {{ color: #34495e; }}
                </style>
            </head>
            <body>{html_content}</body>
        </html>
        """
        
        # Generar nombre único para el reporte
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.pdf"
        pdf_path = self.output_dir / filename
        
        # Guardar como PDF
        pdfkit.from_string(styled_html, str(pdf_path))
        
        return str(pdf_path) 