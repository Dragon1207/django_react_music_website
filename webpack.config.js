// jshint esversion: 6
(function () {
    "use strict";
    const ExtractTextPlugin = require("extract-text-webpack-plugin");
    const webpack = require("webpack");

    (function (extractCss, webpack2) {
        module.exports = (env, argv) => {
            const BundleTracker = require("webpack-bundle-tracker");
            const path = require("path");
            const rootAssetPath = path.join(__dirname, "static");
            const isDevMode = argv.mode === 'development';
            return {
                entry: {
                    main: [
                        path.join(rootAssetPath, "css", "main.css"),
                        path.join(rootAssetPath, "img", "background.png")
                    ],
                    vendor: [
                        "jquery", // jQuery is required by taggit-selectize
                        "bootstrap",
                        "bootstrap/dist/css/bootstrap.css"
                    ],
                    selectize: path.join(rootAssetPath, "css", "taggit_selectize", "css", "selectize.bootstrap3.css")
                },
                output: {
                    path: path.join(rootAssetPath, "static"),
                    publicPath: "/static/",
                    filename: "[name].[hash].js",
                    library: "[name]_[hash]"
                },
                module: {
                    rules: [{
                            test: /jquery\.(jsx|js)$/,
                            loader: "expose-loader?jQuery"
                        },
                        {
                            test: /\.css(\?|$)/,
                            use: extractCss.extract({
                                use: [
                                    isDevMode ? "css-loader" : "css-loader?minimize", "postcss-loader"
                                ]
                            })
                        },
                        {
                            test: /\.(png|woff|woff2|eot|ttf|svg)(\?|$)/,
                            use: "url-loader?limit=100000"
                        }
                    ]
                },
                plugins: [
                    extractCss,
                    new BundleTracker({
                        filename: path.join("static", "manifest.json")
                    })
                ]
            };
        };
    }(new ExtractTextPlugin("[name].[chunkhash].css"), webpack));
}());