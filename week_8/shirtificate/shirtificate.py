from fpdf import FPDF
import os

class ShirtCertificate:
    FONT_NAME = "Helvetica"
    FONT_SIZE_TITLE = 50
    FONT_SIZE_BODY = 30

    def __init__(self, name):
        self.name = name
        self.generate_certificate()

    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        return cls(name)

    def add_title(self, pdf):
        pdf.set_font(self.FONT_NAME, "B", self.FONT_SIZE_TITLE)
        pdf.cell(0, 50, txt="CS50 Shirtificate", align="C", ln=True)

    def add_image(self, pdf):
        pdf.image("shirtificate.png", x=5, y=80, w=200)

    def add_participant_info(self, pdf):
        pdf.set_font(self.FONT_NAME, "B", size=self.FONT_SIZE_BODY)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 180, align="C", txt=f"{self.name} took CS50", ln=True)

    def generate_certificate(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        self.add_title(pdf)
        self.add_image(pdf)
        self.add_participant_info(pdf)

        script_dir = os.path.dirname(__file__)
        pdf_path = os.path.join(script_dir, "shirtificate.pdf")
        pdf.output(pdf_path)


def main():
    ShirtCertificate.get()


if __name__ == "__main__":
    main()
