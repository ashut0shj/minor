from flask import Flask, render_template, request
from transcript import Transcriber

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        file = request.files['file']
        media_type = file.content_type.split("/")
        file_name = 'temp.' + media_type[1]
        file.save(file_name)
        print(media_type[0])
        media = Transcriber(file_name)

        if media_type[0] == 'video':
        #input("Press enter to continue with transcription")
            transcript = media.video_transcribe()
        elif media_type[0] == 'audio':
            transcript = media.audio_transcribe()
        elif media_type[0] == 'presentation':
            transcript = media.ppt_transcribe()
        elif media_type[0] == 'pdf':
            transcript = media.pdf_transcribe()
        elif media_type[0] == 'image':
            transcript = media.image_transcribe()
        
        return render_template('result.html', transcript=transcript)

    return render_template('index.html')


app.run(debug=True)