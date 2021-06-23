var layer = '';//define the layer that contains the markers

map_e8ca07279e544a86bc209912bd51dab4.on('zoomend', function() {
    var currentZoom = map_e8ca07279e544a86bc209912bd51dab4.getZoom();

    console.log("CURRENT ZOOM: " + currentZoom);

    //Update X and Y based on zoom level
    /*
    var x= 50; //Update x 
    var y= 50; //Update Y         
    var LeafIcon = L.Icon.extend({
        options: {
            iconSize:     [x, y] // Change icon size according to zoom level
        }
    });
    layer.setIcon(LeafIcon);
    */
});