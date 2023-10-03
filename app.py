from flask import Flask, render_template, request
from transcript import VideoTranscriber

'''todo add mime'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video']
        media_type = video.content_type.split("/")
        file = 'temp.' + media_type[1]
        video.save(file)
        media = VideoTranscriber(file)

        if media_type[0] == 'video':
            media.convert_to_audio()
            
        input("Press enter to continue with transcription")
        
        transcript = media.transcribe()
        print(transcript)

        return render_template('result.html', transcript=transcript)

    return render_template('index.html')


app.run(debug=True)