from typing import Any
from tex_table_and_img import create_table, create_img
from pdflatex import PDFLaTeX


def generate_latex(table: list[list[Any]], img: str) -> str:
    return """
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{}
{}
\\end{{document}}
    """.format(
        "" if len(table) == 0 else create_table(table),
        "" if img == "" else create_img(img)
    )


def generate_latex_file(pathTex: str, table: list[list[Any]] = [], img: str = ""):
    file = open(pathTex, 'w+')
    file.write(generate_latex(table, img))
    file.close()

def generate_pdf(pathTex: str, pathPdf:str):
    pdfl = PDFLaTeX.from_texfile(pathTex)
    pdf, log, completed_process = pdfl.create_pdf()
    file = open(pathPdf, 'wb')
    file.write(pdf)
    file.close()


if __name__ == "__main__":
    pathTex = "../artifacts/test_tex_2_2_1.tex"
    pathPdf = "../artifacts/test_tex_2_2_2.pdf"
    table = [[1, 2, 3], ['4', '5', '6'], ['one', 'two', None]]
    img = "../res/cat.png"
    generate_latex_file(pathTex, table=table, img=img)
    generate_pdf(pathTex, pathPdf)

