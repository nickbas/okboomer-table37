import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import geoData from '../../../data/DC_Buildings_Footprint_4326_test.js';

let mapboxToken = 'pk.eyJ1IjoidXJiYW5pbnN0aXR1dGUyMDE5IiwiYSI6ImNrM293b2VzaTI1c3IzbmtvZ2thcGE5ZjQifQ.srvBDFJzO8pNOz62SNz7wA'

declare let mapboxgl

let apiUrl = 'https://3rz79gbmdl.execute-api.us-east-2.amazonaws.com/dev/geodata'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'hackathon2019';
	constructor(private http: HttpClient) {}

	ngOnInit() {
		mapboxgl.accessToken = mapboxToken

		var map = new mapboxgl.Map({
	  container: 'map',
	    style: 'mapbox://styles/mapbox/satellite-v9',
	    center: [-77.037770018042963, 38.987408245748732],
	    zoom: 17
	  });
	  map.on('load', function () {
	    map.addSource('bb', { type: 'geojson', data: geoData.default });
	    map.addLayer({
	      'id': 'polygons',
	      'type': 'fill',
	      'source': 'bb',
	      'paint': {
	        'fill-color': [
						'interpolate',
		        ['linear'],
		        ['number', ['get', 'ALTITUDE_M']],
						0, '#0000ff',
						50, '#00ff00',
						100, '#ffff00',
		        150, '#ff0000',
					]
	      }
	    });
	  });

		map.on('click', 'polygons', function (e) {
			console.log("e:", e.features)
			let center = [e.lngLat.lng, e.lngLat.lat]
			console.log("center:", center)
			map.flyTo({center: [e.lngLat.lng, e.lngLat.lat]});
		});

		this.getData()
	}

	getData(): void {
		console.log("runnign ")
		this.http.post(apiUrl, {}).subscribe((response) => {
			console.log("response:", response)
		});
	}
}
