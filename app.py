from flask import Flask,url_for,render_template,send_file,redirect,request
import os

app =Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = 'files'

@app.route('/',methods=['post','get'])
def home():
    if request.method =='POST':
        scale = request.form.get("scale")
        file = request.form.get("file")
        if scale == 1 and file== "gcode":
            # redirect(url_for(download_page))
            return render_template('download.html',scale=scale,file=file)
        elif scale==-1 and file=="gcode":
            # redirect(url_for(download_page))
            return render_template('download.html',scale=scale,file=file)
        elif scale==1 and file=="stl":
            # redirect(url_for(download_page))
            return render_template('download.html',scale=scale,file=file)
        else:
            return render_template('download.html',scale=scale,file=file)
    else:
        return render_template('home.html')

@app.route('/downloads/<filename>')
def download(filename):
    path1="/micheal_project/DOWNLOAD_FOLDER/"+filename
    return send_file(path1,as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)