import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from streamlit_pdf_viewer import pdf_viewer

def getContents2 (file):

  with magChapters:
    f = 'c:/users/malpr/perlstuf/smartsig/oldmags/Cont' + str(file)
    pdf_viewer(input=f,
                   width=700)

#########################################

header = st.container()

magtitles = st.container()
magcontents = st.container()
magsample = st.container()

with header:
  st.title('SmartSig Magazines')

with open('c:/users/malpr/perlstuf/smartsig/oldmags/oldmagnames.txt') as file:
    magnames = [line.rstrip() for line in file]
magnames.sort()
with magcontents:
  magMonths, magChapters = st.columns([0.2,0.8])
  with magMonths:
    mag = st.radio('Choose a Mag',magnames)
  magChapters.write('£4 per mag or 10 for £35 Contact details at smartersig.com')
  chapters = getContents2(mag)
