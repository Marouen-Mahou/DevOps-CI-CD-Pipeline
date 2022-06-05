const bodyParser = require("body-parser");
const cors = require("cors");

// parse env variables
require("dotenv").config();

const helmet = require("helmet")

const express = require("express");
const app = express();
const port = process.env.PORT || 3001;

app.use(cors({ origin: '*' }));

app.use(helmet());

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


//Routes
const Routes = require('./routes/routes')
Routes(app)

app.listen(port, () => {
  console.log("listening port => ", port);
});