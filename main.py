from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def carousel():
    return f'''<html>
                <head>
                    <title>Пейзажи Марса</title>
                            <link rel="stylesheet" href="{url_for('static',filename='css/bootstrap.min.css')}">
                            <link rel="stylesheet" href="{url_for('static',filename='css/all.min.css')}">
                            <link rel="stylesheet" href="{url_for('static',filename='css/style.css')}">
                    <script src="{url_for('static',filename='js/jquery.min.js')}"></script>
                    <script src="{url_for('static',filename='js/bootstrap.min.js')}"></script>
                </head>
                <body>
                    <div class="container">
                        <h1>Пейзажи Марса</h1>
                        <div id="myCarousel" class="carousel slide">
                            <ol class="carousel-indicators">
                                <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                                <li data-target="#myCarousel" data-slide-to="1"></li>
                                <li data-target="#myCarousel" data-slide-to="2"></li>
                                <li data-target="#myCarousel" data-slide-to="3"></li>
                                <li data-target="#myCarousel" data-slide-to="4"></li>
                                <li data-target="#myCarousel" data-slide-to="5"></li>
                                <li data-target="#myCarousel" data-slide-to="6"></li>
                            </ol>
                            <div class="carousel-inner">
                                <div class="item">
                                    <img src="{url_for('static',filename='img/a.jpg')}" style="width:100%;height:800px;">
                                </div>
                                <div class="item active">
                                    <img src="{url_for('static',filename='img/b.jpg')}" style="width:100%;height:800px;">
                                </div>
                                <div class="item">
                                    <img src="{url_for('static',filename='img/c.jpg')}" style="width:100%;height:800px;">
                                </div>
                                <div class="item">
                                    <img src="{url_for('static',filename='img/d.jpg')}" style="width:100%;height:800px;">
                                </div>
                                <div class="item">
                                    <img src="{url_for('static',filename='img/e.jpg')}" style="width:100%;height:800px;">
                                </div>
                                <div class="item">
                                    <img src="{url_for('static',filename='img/f.jpg')}" style="width:100%;height:800px;">
                                </div>
                            </div>
                            <a class="left carousel-control" href="#myCarousel" data-slide="prev">
                                <span class="fa fa-chevron-left fa-lg" style="margin-top:400px"></span>
                            </a>
                            <a class="right carousel-control" href="#myCarousel" data-slide="next">
                                <span class="fa fa-chevron-right fa-lg" style="margin-top:400px"></span>
                            </a>
                        </div>
                    </div>
                </body>
            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
