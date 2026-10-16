import streamlit as st
from streamlit_advanced_audio import audix, WaveSurferOptions
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader, PdfWriter
import os
import webbrowser
import time
import piper
import wave

voices_path = "voices/"
installed_models = os.listdir(voices_path)
installed_voices = []
startpage = True

#Plain text reader
def Read():
    if lingo == "English":
        voice = piper.PiperVoice.load("voices/en_US-danny-low.onnx")
    elif lingo == "French":
        voice = piper.PiperVoice.load("voices/fr_FR-gilles-low.onnx")
    elif lingo == "Russian":
        voice = piper.PiperVoice.load("voices/ru_RU-dmitri-medium.onnx")
    elif lingo == "Korean":
        voice = piper.PiperVoice.load("voices/ko_KR-kss-medium.onnx.onnx")
    elif lingo == "Arabic":
        voice = piper.PiperVoice.load("voices/ar_JO-kareem-medium.onnx")
    
    with wave.open(f"{filename}.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
#Checks language on refresh
def check_languages():
    if "en_US-danny-low.onnx.json" not in installed_models:
        st.error("English Not installed")
    elif "en_US-danny-low.onnx" not in installed_models:
        st.error("English Not installed")
    else:
        if startpage == True:
            st.success("English Installed")
        installed_voices.append("English")
    #Chekc FR
    if "fr_FR-gilles-low.onnx.json" not in installed_models:
        st.error("French Not installed")
    elif "fr_FR-gilles-low.onnx" not in installed_models:
        st.error("French Not installed")
    else:
        if startpage == True:
            st.success("French Installed")
        installed_voices.append("French")
    #Check RU
    if "ru_RU-dmitri-medium.onnx.json" not in installed_models:
        st.error("Russian Not installed")
    elif "ru_RU-dmitri-medium.onnx" not in installed_models:
        st.error("Russian Not installed")
    else:
        if startpage == True:
            st.success("Russian Installed")
        installed_voices.append("Russian")
    #Check KO
    if "ko_KR-kss-medium.onnx.json" not in installed_models:
        st.error("Korean Not installed")
    elif "ko_KR-kss-medium.onnx" not in installed_models:
        st.error("Korean Not installed")
    else:
        if startpage == True:    
            st.success("Korean Installed")
        installed_voices.append("Korean")
    #Check AR
    if "ar_JO-kareem-medium.onnx.json" not in installed_models:
        st.error("Arabic Not installed")
    elif "ar_JO-kareem-medium.onnx" not in installed_models:
        st.error("Arabic Not installed")
    else:
        if startpage == True:
            st.success("Arabic Installed")
        installed_voices.append("Arabic")
#PDF reader
def Read_PDF(startpage, endpage, pdf_reader, lingo, filename):
    target_pages = list(range(startpage, endpage + 1))
    fulltext = ""
    
    for page_num in target_pages:
        pages = pdf_reader.pages[page_num]
        text = pages.extract_text()
        fulltext += text

    if lingo == "English":
        voice = piper.PiperVoice.load("voices/en_US-danny-low.onnx")
    elif lingo == "French":
        voice = piper.PiperVoice.load("voices/fr_FR-gilles-low.onnx")
    elif lingo == "Russian":
        voice = piper.PiperVoice.load("voices/ru_RU-dmitri-medium.onnx")
    elif lingo == "Korean":
        voice = piper.PiperVoice.load("voices/ko_KR-kss-medium.onnx.onnx")
    elif lingo == "Arabic":
        voice = piper.PiperVoice.load("voices/ar_JO-kareem-medium.onnx")

    with wave.open(f"{filename}.wav", "wb") as wav_file:
        voice.synthesize_wav(fulltext, wav_file)

    @st.dialog("Conversion Sucessfull")
    def balls2():

        surferoptions = WaveSurferOptions(
        wave_color="#2B88D9",
        progress_color="#b91d47",
        height=100
        )

        result = audix(f"{filename}.wav", wavesurfer_options=surferoptions)

    balls2()


#Web UI
st.title("📚🐛 Bookworm")
st.set_page_config(page_title = "Bookworm", page_icon = "🐛")

selected2 = option_menu(None, ["Home", "Read PDF", "Read Plain Text"], 
    icons=['house', 'file-earmark', "card-text"], 
    menu_icon="cast", default_index=0, orientation="horizontal")

#Home Page
if selected2 == "Home":
    st.header("Welcome to Bookworm Reader")
    st.text("In order to start using this application, you must download at least one of these piper voice model, and put it in the voices folder.")
    st.header("Piper Model Installation Instructions")
    st.text("1. Select a Language \n2. Click the open Huggingface button \n3. Download the .onnx and .json files \n4. Put them into the voices folder \n5. Hit the refresh button")
    
    language_to_download = st.selectbox(
    "Select a Lanuage",
    ("English", "French", "Russian", "Korean", "Arabic"),
    )
    
    col1, col2 = st.columns(2)
    
    with col2:
        if st.button("Refresh", width="stretch"):
            st.toast("Refreshed")
            time.sleep(0.5)
            st.rerun()
    #Download links to the models
    with col1:    
        if st.button("Open Huggingface", type="primary", width="stretch"):
            if language_to_download == "Select a Model":
                webbrowser.open("https://www.youtube.com/watch?v=Aq5WXmQQooo")
            elif language_to_download == "English":
                webbrowser.open("https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/danny/low")
            elif language_to_download == "French":
                webbrowser.open("https://huggingface.co/rhasspy/piper-voices/tree/main/fr/fr_FR/gilles/low")
            elif language_to_download == "Russian":
                webbrowser.open("https://huggingface.co/rhasspy/piper-voices/tree/main/ru/ru_RU/dmitri/medium")
            elif language_to_download == "Korean":
                webbrowser.open("https://huggingface.co/rhasspy/piper-voices/tree/main/ko/ko_KR/kss/medium")
            elif language_to_download == "Arabic":
                webbrowser.open("https://huggingface.co/rhasspy/piper-voices/tree/main/ar/ar_JO/kareem/medium")

    st.subheader("Installed Models")
    check_languages()

#Web UI for plain text tab
if selected2 == "Read Plain Text":
    startpage = False
    check_languages()
    st.header("Plain Text")
    text = st.text_area("Enter the text to be read")
    lingo = st.selectbox("Select a Language", installed_voices, placeholder="No Voices Installed")
    filename = st.text_input("Filename")
    
    if st.button("Read", width="stretch", type="primary"):
        checks_to_pass = 3
        check_passed = 0
        if text == "":
            st.error("Write something")
        else: 
            check_passed += 1
        if lingo == "No Voices Installed":
            st.error("Please install a voice first")
        else: 
            check_passed += 1
        if filename == "":
            st.error("Please name the file")
        else: 
            check_passed += 1
        
        if check_passed == checks_to_pass:
            with st.spinner("Synthesizing text...", show_time=True):
                Read()

            @st.dialog("Conversion Sucessfull")
            def balls():

                surferoptions = WaveSurferOptions(
                wave_color="#2B88D9",
                progress_color="#b91d47",
                height=100
                )
                
                result = audix(f"{filename}.wav", wavesurfer_options=surferoptions)

            balls()
        else:
            st.toast("One or more checks faild.")
#Web UI for Read PDF tab
if selected2 == "Read PDF":
    startpage = False
    uploaded_file = st.file_uploader("Choose a PDF file", accept_multiple_files=False)
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            PDF_file = uploaded_file.getvalue()
            check_languages()

            st.text("Preview:")
            pdf_viewer(
                PDF_file,
                width=700,
                height=900,
                zoom_level=1.2,                    
                viewer_align="center",             
                show_page_separator=True           
            )

            with open("temp.pdf", "wb") as f:
                f.write(PDF_file)
            
            pdf_reader = PdfReader("temp.pdf")
            lingo = st.selectbox("Select a Language", installed_voices, placeholder="No Voices Installed")
            filename = st.text_input("Filename")
            coli1, coli2 = st.columns(2)
            min_start = 1
            max_end = len(pdf_reader.pages)
            max_end_int = int(float(max_end))

            with coli1:
                startpage = st.text_input("Start Page", "1")
            with coli2:
                endpage = st.text_input("End Page", max_end)

            if st.button("Read", width="stretch", type="primary"):
                checks_to_pass = 9
                check_passed = 0
                
                if lingo == "No Voices Installed":          
                    st.toast("Please install a voice first")
                else:
                    check_passed += 1
                if filename == "":
                    st.toast("Please name the file")
                else:
                    check_passed += 1
                if startpage == "":
                    st.toast("Enter page to start at")
                else:
                    check_passed += 1
                if endpage == "":
                    st.toast("Enter page to end at")
                else:
                    check_passed += 1

                try:
                    int(startpage)
                except ValueError:
                    st.toast("Enter a Whole Number")
                startpage = int(startpage)
                check_passed += 1

                try:
                    int(endpage)
                except ValueError:
                    st.toast("Enter a Whole Number")
                endpage = int(endpage)
                check_passed += 1
                
                if startpage > endpage:
                    st.error("Start page is bigger then end page")
                else:
                    check_passed += 1
                
                if endpage > max_end_int:
                    st.error("Page does not exist")
                else:
                    check_passed += 1

                if startpage < 1:
                    st.error("Page can not be nothing or negative")
                else:
                    check_passed += 1

                if check_passed == checks_to_pass:
                    print("All Checks Passed")
                    with st.spinner("Synthesizing text...", show_time=True):
                        Read_PDF(startpage, endpage, pdf_reader, lingo, filename)
                else:
                    print("Not all passed")

        else:
            st.error("This is not a PDF file")
