{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","@app.route(\"/\")","","def hello():","    return \"Helllo World ...again\"","    ","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","        port=int(os.environ.get('PORT')),","        debug=True)",""],"id":1}],[{"start":{"row":10,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","        port=int(os.environ.get('PORT')),","        debug=True)",""],"id":2},{"start":{"row":10,"column":0},"end":{"row":13,"column":59},"action":"insert","lines":["","if __name__ == '__main__':","    app.debug = True","    app.run(host=os.environ['IP'], port=os.environ['PORT'])"]}],[{"start":{"row":10,"column":0},"end":{"row":13,"column":59},"action":"remove","lines":["","if __name__ == '__main__':","    app.debug = True","    app.run(host=os.environ['IP'], port=os.environ['PORT'])"],"id":3},{"start":{"row":10,"column":0},"end":{"row":13,"column":23},"action":"insert","lines":["if __name__=='__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":23},"end":{"row":13,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1560791112787,"hash":"6162d911af771a14f3b50dfcf0f3c48f44309e45"}