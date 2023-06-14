from pydub import AudioSegment
import speech_recognition as sr
import tempfile
import os
from datetime import datetime

# define the input directory path
input_dir_path = r"D:\RECORDER\FOLDER_A"

# create a recognizer instance
recognizer = sr.Recognizer()

for root, dirs, files in os.walk(input_dir_path):
    for file in files:
        # check if the file is an audio file
        if file.lower().endswith(('.mp3', '.wav')):
            # define the audio file path
            audio_file_path = os.path.join(root, file)

            # read the audio file using pydub
            audio_data = AudioSegment.from_file(audio_file_path, format="mp3")

            # convert the audio to PCM WAV format
            pcm_audio_data = audio_data.set_frame_rate(16000).set_sample_width(2).set_channels(1)

            # transcribe the audio to text using the recognizer
            with tempfile.NamedTemporaryFile(delete=False) as f:
                temp_file = f.name
                pcm_audio_data.export(temp_file, format='wav')
                with sr.AudioFile(temp_file) as source:
                    audio_text = recognizer.record(source)

            # get the transcribed text
            text = recognizer.recognize_google(audio_text)

            # get the creation time of the input audio file
            file_creation_time = os.path.getctime(audio_file_path)
            creation_date = datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d')

            # define the output file path
            output_file_name = "{}.txt".format(creation_date)
            output_file_path = os.path.join(os.getcwd(), output_file_name)


            # write the transcribed text to a text file
            with open(output_file_path, "w") as f:
                f.write(text)

            # print a message to indicate the file has been saved
            print("Transcription saved to {}".format(output_file_path))

