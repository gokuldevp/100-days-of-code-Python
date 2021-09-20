# import modules
from gtts import gTTS
from tkinter import filedialog, Tk
import PyPDF2

# getting file path of pdf files
Tk().withdraw()
file_path = filedialog.askopenfilename(initialdir="/", title="Choose Image File", filetypes=[('pdf file', '*.pdf')])

# getting name of pdf file and converting it to mp3 file name
save_name = file_path.split("/")[-1].replace(".pdf", ".mp3")

# opening file pdf file and reading all lines
with open(file_path, "rb") as pdf:
    file = PyPDF2.PdfFileReader(file_path)

# storing all lines of pdf in   variable text
text = ""
num_page = file.numPages
for i in range(num_page):
    text += file.getPage(i).extractText() + " "

# converting the test to speech
text_to_speech = gTTS(text=text, lang="en", slow=False)

# saving the file
text_to_speech.save(save_name)
