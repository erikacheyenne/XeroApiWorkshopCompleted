from flask import Flask,jsonify,request,abort,make_response
from app import app
from app import storage

locations = [
    {
        "name": "SofiasCustomAutomotive",
        "details": [
            {
                "address" : "P. 60 Sherman Wallaby Way, Sydney",
                "hours" : "9 A.M. to 5 P.M.",
                "phone number": "000-000-0000",
                "services":[

                          {
                            "servicetype":"regularmaintenance",
                            "details":[
                                {
                                    "price":5,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"bodyrepair",
                            "details":[
                                {
                                    "price":30,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"paintrepair",
                            "details":[
                                {
                                    "price":20,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"custompaint",
                            "details":[
                                {
                                    "price":20,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"framerepair",
                            "details":[
                                {
                                    "price":20,
                                    "explanation":"none"
                                },
                            ]
                        },
                        {
                            "servicetype":"customemachining",
                            "details":[
                                {
                                    "price":0,
                                    "explanation":"unavailable at this time."
                                },
                            ]
                        }
                ]
            }
        ]
    }
]

services = [
   {
       "servicetype": "custommachining",
       "details":[
           {
               "price":"",
               "explanation of service":""
           }
       ]

   },
      {
       "servicetype": "framerepair",
       "details":[
           {
               "price":"",
               "explanation of service":""
           }
       ]

   }
]


jobs = [
    {
        "Order Number": ""
    }
]


# all my GET methods

@app.route('/')
def home():
    return "Hello World!"


@app.route('/locations', methods=['Get'], strict_slashes=False)
def get_locations():
    data = locations
    response = jsonify(data)
    response.status_code=200
    return response


@app.route('/service', methods=['Get'], strict_slashes=False)
@app.route('/services', methods =['Get'], strict_slashes=False)
def get_services():
    data = services
    response = jsonify(data)
    response.status_code=200
    return response


@app.route('/locations/<string:name>', methods=['Get'], strict_slashes=False)
def get_location(name):
    for location in locations:
        if location['name'] == name:
            data = location
            response = jsonify(data)
            response.status_code=200
            return response
    abort(404, "message: Location {} does not exist.".format(name))


@app.route('/locations/<string:name>/services', methods=['Get'], strict_slashes=False)
def get_services_for_location(name):
    for location in locations:
        if location['name'] == name:
            data = location['details'][0]['services']
            response = jsonify(data)
            response.status_code=200
            return response
    abort(404, "message: Location {} does not exist.".format(name))


@app.route('/locations/<string:name>/<string:service>', methods=['Get'], strict_slashes=False)
def get_service_for_location(name,service):
    for location in locations:
        if location['name'] == name:
            for s in location['details'][0]['services']:
                if s["servicetype"] == service:
                    data = s
                    response = jsonify(data)
                    response.status_code=200
                    return response
            abort(404, "message: Service {} does not exist.".format(service))
    abort(404, "message: Location {} does not exist.".format(name))


@app.route('/service/<string:name>', methods=['Get'], strict_slashes=False)
@app.route('/services/<string:name>', methods =['Get'], strict_slashes=False)
def get_service(name):

    for service in services:
        if service['servicetype'] == name:
            data = service['details']
            response = jsonify(data)
            response.status_code=200
            return response
    abort(404, "message: Service {} does not exist.".format(name))


@app.route('/Jobs', methods=['Get'], strict_slashes=False)
def get_jobs():
    return ""


# all my POST methods
@app.route('/locations/<string:name>/<string:service>', methods=['POST'], strict_slashes=False)
#The service needs to be added to a specific location, because this example assumes locations have different offerings. 
#Although there is a master list of all services that can be updated, this should be updated separately, 
# as locations can pick from master list.
def create_service(name,service):
    #request_data = request.args
    request_data=request.get_json(force=True)
    for location in locations:
        if location['name'] == name:
            service_list = location['details'][0]['services']
            for s in location['details'][0]['services']:
                if s["servicetype"] == service:
                    return jsonify({'message':'Thanks for trying to update a service. This service type already exists. Try using the PUT endpoint to edit this instead.'})
                
                new_service = {
                        "servicetype":request_data['servicetype'],
                        "details": [
                            {
                                "price":request_data['details'][0]['price'],
                                "explanation of service":request_data['details'][0]['explanation']
                            }
                        ]
                }
                location['details'][0]['services'].append(new_service)
                data = new_service
                response = jsonify(data)
                response.status_code=201
                return response
    return jsonify({'message':"This service could not be created."})


# all my PUT methods
# PUT requests either create a new resource or modify an existing resource
@app.route('/services/<string:service_name>', methods=['PUT'], strict_slashes=False)
def put_service(service_name):

    request_data = request.get_json(force=True)

    for service in services:
        if service["servicetype"] == service_name:
            service["details"] = request_data["details"]
            data = { "message" : "Service {} updated.".format(service_name) }
            response = jsonify(data)
            response.status_code=202
            return response
    
    services.append(request_data)
    data = { "message" : "Service {} created.".format(service_name) }
    response = jsonify(data)
    response.status_code=201
    return response


# all my DELETE methods

@app.route('/services/<string:service_name>', methods=['DELETE'], strict_slashes=False)
def delete_service(service_name):

    for service in services:
        if service["servicetype"] == service_name:
            services.remove(service)
            data = { "message" : "Service {} deleted.".format(service_name) }
            response = jsonify(data)
            response.status_code = 200
            return response

    abort(404, "message: Service {} does not exist.".format(service_name))

#app.run(port=5000,debug=True)
