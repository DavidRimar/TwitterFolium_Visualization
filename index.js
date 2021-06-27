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


 // OWN CODE
 map_e8ca07279e544a86bc209912bd51dab4.on('zoomend', function() {
    var currentZoom = map_e8ca07279e544a86bc209912bd51dab4.getZoom();

    console.log("CURRENT ZOOM: " + currentZoom);

    var startWidth = 60;
    var startHeight = 48;

    var newWidth = (10 * currentZoom) + ((currentZoom - 6)*42)
    var newHeight = (8 * currentZoom) + ((currentZoom - 6)*42)

    // get all div elements
    var all_div_markers = document.querySelectorAll(".leaflet-marker-icon");
    
    console.log("all_div_markers: " + all_div_markers.length);
    // change width and height
    for (var i = 0; i < all_div_markers.length;  i++) {
        all_div_markers[i].style.height = `${newHeight}px`;
        all_div_markers[i].style.width = `${newWidth}px`;
    }
    
    // all_div_markers.style.height = "90px";

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