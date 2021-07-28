#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

outint = Blueprint('outint', __name__,)

@outint.route('/outint.md')
def getDescriptorInterpolation():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/outint.md",
			"entrypoint": "http://51.77.148.187:5001/resource/outint",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "55"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues", "tabTimestamp"],
				"returns": ["tabValues"],
				"functionality": "OVI", 
				"image": "ovi.png",
				"Qf": [{"Cost" : "15"},{"Usage": "11"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/predheatengcons",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/predheateng",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/predheat",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outvalinterpolation",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "OVI"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outvalint",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "OVI"
				}
				]
 		}
 		"""
 	return myjson
	
