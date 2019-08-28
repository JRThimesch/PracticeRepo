import React from "react";
import L from "leaflet";

const style = {
  width: "100%",
  height: "300px"
};

export default class Map extends React.Component {
  componentDidMount() {
    // create map

    this.littleton = L.marker([39.61, -105.02]).bindPopup(
      "This is Littleton, CO."
    );
    this.denver = L.marker([39.74, -104.99]).bindPopup("This is Denver, CO.");
    this.aurora = L.marker([39.73, -104.8]).bindPopup("This is Aurora, CO.");
    this.golden = L.marker([39.77, -105.23]).bindPopup("This is Golden, CO.");
    this.cities = L.layerGroup([this.littleton, this.denver]);
    this.others = L.layerGroup([this.aurora, this.golden]);

    this.map = L.map("map", {
      center: [39.7392, -104.9903],
      zoom: 9,
      layers: [
        this.cities,
        this.others,
        L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
          attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        })
      ]
    });

    this.groupedOverlays = {
      Landmarks: {
        Motorways: this.others,
        Cities: this.cities
      }
    };

    this.options = {
      groupCheckboxes: true
    };

    L.control
      .groupedLayers(null, this.groupedOverlays, this.options)
      .addTo(this.map);
  }
  render() {
    return <div id="map" style={style} />;
  }
}
