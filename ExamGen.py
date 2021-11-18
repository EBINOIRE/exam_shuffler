from PyPDF2 import PdfFileReader, PdfFileWriter
from fpdf import FPDF
import random

def examGen(index, output):

    # find ??? rand number between 1:4 
    # choose file accordingly
    # merge chosen files

    r1 = random.randrange(1, 5, 1)
    r2 = random.randrange(1, 5, 1)
    r3 = random.randrange(1, 5, 1)
    r4 = random.randrange(1, 5, 1)
    r5 = random.randrange(1, 5, 1)

    # # according to random numbers already generated choose set of questions
    # q1 = paths[r1]
    # q2 = paths[r2]
    # q3 = paths[r3]
    # q4 = paths[r4]
    # q5 = paths[r5]

    # open chosen sets
    reader1 = PdfFileReader('Question1.pdf')
    reader2 = PdfFileReader('Question2.pdf')
    reader3 = PdfFileReader('Question3.pdf')
    reader4 = PdfFileReader('Question4.pdf')
    reader5 = PdfFileReader('Question5.pdf')
    
    # generate suitable code 
    code = f'Q1({r1}) | Q2({r2}) | Q3({r3}) | Q4({r4}) | Q5({r5})'

    # map coding
    coding.write(f'{index}  =->  {code} \n')

    # create code_page.pdf
    code_page = FPDF()
    code_page.add_page()
    # set style and size of font 
    # that you want in the pdf
    code_page.set_font("Arial", size = 100)
    
    # create a cell
    code_page.cell(200, 10, txt = f'{index}', 
            ln = 1, align = 'C')

    # save the code_page with name .code_page
    code_page.output('code.pdf') 

    # write object
    writerObj = PdfFileWriter()

    # read pages
    front_page = PdfFileReader('front_page.pdf')
    cd_page = PdfFileReader('code.pdf')

    # add code page
    writerObj.addPage(cd_page.getPage(0))
    
    # add cover page
    writerObj.addPage(front_page.getPage(0))

    # read from each set
    writerObj.addPage(reader1.getPage(r1 - 1))
    writerObj.addPage(reader2.getPage(r2 - 1))
    writerObj.addPage(reader3.getPage(r3 - 1))
    writerObj.addPage(reader4.getPage(r4 - 1))
    writerObj.addPage(reader5.getPage(r5 - 1))

    # write to output file
    with open (output, 'wb') as out:
        writerObj.write(out)



if __name__ == '__main__':
    
    coding = open("mapping.txt", "w")
    
    for i in range(50):
        examGen(i, output = f'{i}.pdf')

    coding.close()