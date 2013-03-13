from bottle import Bottle, run, template, get, post, request, error, SimpleTemplate
import os
import CLSearch

app = Bottle()

@app.route('/')
@app.route('/search')
@app.route('/search/')
def search_form():
    return template('search_form.tpl')


@app.route('/search', method='POST')
def search_submit():
    location = request.forms.get('location')
    bed = request.forms.get('bed')
    rentmin = request.forms.get('rentmin')
    rentmax = request.forms.get('rentmax')
    
    results = CLSearch.get_list(location,rentmin,rentmax,bed)
    return template('search_results.tpl',
                    location=location,
                    bed=bed,
                    rentmin=rentmin,
                    rentmax=rentmax,
                    results=results)


@app.error(404)
def error404(error):
    return "sorry, doesn't exist"   

##if __name__ == '__main__':
##    port = os.environ.get('PORT',8080)
##    run(app, host='0.0.0.0', port=port)

port = os.environ.get('PORT',8080)
run(app, host='0.0.0.0', port=port)
