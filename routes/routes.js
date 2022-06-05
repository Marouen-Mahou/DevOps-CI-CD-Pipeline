"use strict";

module.exports = function (app) {
    //Import routes
    const postRoutes = require("./postRoutes");

    // Groupe routes
    const routes = [
        postRoutes,
    ]

    //Use
    app.use(routes)
};
