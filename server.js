const express = require("express");
const app = express();
// Set the default port to connect to.
const port = process.env.PORT || 3000;

const runServer = () => {
  /*
  // Get the current working directory that the local server is being run from.
  // const cwd = process.cwd();

  // Initialise the application with Express
  // const app = express();

  // Connect the server to the root directory
  app.use(express.static(cwd));
  */

  // point to html pages and send them
  app.get('/', (req, res) => {
    res.sendFile('./maps/Map_1_fishnet_unigrams.html', { root: __dirname });
  });
  
  app.get('/map2_fishnet_bigrams', (req, res) => {
    res.sendFile('./maps/Map_2_fishnet_bigrams.html', { root: __dirname });
  });

  app.get('/map3_dbscan_fishnet_bigrams', (req, res) => {
    res.sendFile('./maps/Map_3_dbscan_fishnet_bigrams.html', { root: __dirname });
  });

  app.get('/map4_fishnet_textcat_pure_intraspace', (req, res) => {
    res.sendFile('./maps/Map_4_fishnet_pure_textcat(normalized).html', { root: __dirname });
  });

  //app.get('/map4_fishnet_textcat_pure_normalized', (req, res) => {
  //  res.sendFile('./maps/Map_4B_fishnet_textcat_pure(normalized).html', { root: __dirname });
  //});

  app.get('/map5_textcat_stdbscan_bigrams', (req, res) => {
    res.sendFile('./maps/Map_5_textcat_stdbscan_bigrams.html', { root: __dirname });
  });

  

  // Run the server at the specified port.
  app.listen(port, () => {
    console.log(`Server is up and running at port http://localhost:${port}`);
  });
};

runServer();