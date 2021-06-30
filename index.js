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


 // OWN CODE: HEIGHT AND WIDTH
 map_087ac7dee80446fd8e8ca732f7c7caa8.on('zoomend', function() {
    var currentZoom = map_087ac7dee80446fd8e8ca732f7c7caa8.getZoom();

    console.log("CURRENT ZOOM: " + currentZoom);

    var startWidth = 60;
    var startHeight = 48;

    var newWidth = (10 * currentZoom) + ((currentZoom - 6)*42)
    var newHeight = (8 * currentZoom) + ((currentZoom - 6)*42)

    // get all div elements
    //var all_div_ttips = document.querySelectorAll(".leaflet-marker-icon");
    var all_div_ttips = document.querySelectorAll(".leaflet-tooltip");
    
    console.log("all_div_ttips: " + all_div_ttips.length);
    // change width and height
    for (var i = 0; i < all_div_ttips.length;  i++) {
        all_div_ttips[i].style.height = `${newHeight}px`;
        all_div_ttips[i].style.width = `${newWidth}px`;
    }
    
});

// OWN CODE: FONT-SIZE
map_087ac7dee80446fd8e8ca732f7c7caa8.on('zoomend', function() {
    var currentZoom = map_087ac7dee80446fd8e8ca732f7c7caa8.getZoom();

    console.log("CURRENT ZOOM: " + currentZoom);

    var startFontSize = 4.5;

    // part1 = startFontSize, part2 = 0 at zoom = 6 
    var newFontSize = (0.75 * currentZoom) + ((currentZoom - 6) * 2)

    // get all div elements
    //var all_div_ttips = document.querySelectorAll(".leaflet-marker-icon");
    var all_div_ttips = document.querySelectorAll(".leaflet-tooltip");
    
    console.log("all_div_ttips: " + all_div_ttips.length);
    // change width and height
    for (var i = 0; i < all_div_ttips.length;  i++) {
        all_div_ttips[i].style.fontSize = `${newFontSize}px`;
    }
    
});