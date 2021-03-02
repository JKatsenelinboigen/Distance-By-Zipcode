import flask
from flask import request, jsonify
from ZipCodeDatasetParser import ZipCodeDatasetParser

app = flask.Flask(__name__)
app.config["DEBUG"] = True

 #routes all requests in home directory to this method
@app.route('/', methods=['GET'])
def home():

    
    if ("zip1" in request.args and "zip2" in request.args): ##some input checking
        zip1 = str(request.args["zip1"])
        zip2 = str(request.args["zip2"])

        DBZ = ZipCodeDatasetParser() #initialize zip code class
        
        distanceKm = DBZ.distanceBetweenZipsKm(zip1, zip2)
        distanceMi = DBZ.distanceBetweenZipsMi(zip1, zip2)

        #creates dictionary with out of results for display
        distances = {
                    "distance_Km":distanceKm,
                    "distance_Mi":distanceMi,
                    "zip1":zip1, "zip2":zip2
                    }
                    

        #converts to json and returns 
        return jsonify(distances)
    else:
        return "Request must be of the form: /?zip1=12345&zip2=12345"


app.run()