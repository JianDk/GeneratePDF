
from fpdf import FPDF
import datetime

class PDF:
    def __init__(self):
        self.pdf = FPDF(orientation='P', unit = 'mm', format = 'A4')
        self.pdf.add_page()
        self.pdf.set_text_color(0,0,0)
        print('hello world this worked!!!!')
    
    def addFont(self, family, fontPath):
        '''The ttf file in fontPath will be added. fontPath is the string of the full path. 
        family is a string for a short name referring to the font in future'''
        self.pdf.add_font(family = family, fname = fontPath)
    
    def export(self, outputFilePath, dest):
        '''Export the pdf file using the string outputFilePath.

        dest : a string. I or D: write the document to sys.stdout. This is the default if no file name is given.
        F: save to a local file with the given name (may include a path). This is the default if a file name is given.
        S: return the document as a byte string.'''
        self.pdf.output(outputFilePath, dest)

