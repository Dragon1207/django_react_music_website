// jshint esversion: 6
(function () {
    'use strict';
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    const webpack = require('webpack');
    const CleanWebpackPlugin = require('clean-webpack-plugin');

    (function (extractCss, webpack2) {
        module.exports = (env, argv) => {
            const BundleTracker = require('webpack-bundle-tracker');
            const path = require('path');
            const isDevMode = argv.mode === 'development';
            const merge = require("webpack-merge");
            const staticDir = path.resolve('./static');
            const srcDir = path.resolve('./src');
            const djangoOutDir = path.join(staticDir, 'static');
            const reactOutDir = path.join(srcDir, 'app', 'dist');

            const sharedConfig = {
                context: __dirname,
                output: {
                    publicPath: '/static/',
                    filename: '[name].[hash].js'
                },
                module: {
                    rules: [{
                            test: /\.css(\?|$)/,
                            use: extractCss.extract({
                                use: [
                                    isDevMode ? 'css-loader' : 'css-loader?minimize', 'postcss-loader'
                                ]
                            })
                        },
                        {
                            test: /\.(png|woff|woff2|eot|ttf|svg)(\?|$)/,
                            use: 'url-loader?limit=100000'
                        }
                    ]
                },
                plugins: [
                    extractCss,
                    new BundleTracker({
                        filename: path.join('static', 'manifest.json')
                    })
                ]
            };

            const djangoConfig = merge(sharedConfig, {
                entry: {
                    main: [
                        path.join(staticDir, 'css', 'main.css'),
                        path.join(staticDir, 'img', 'background.png')
                    ],
                    vendor: [
                        'jquery', // jQuery is required by taggit-selectize
                        'bootstrap',
                        'bootstrap/dist/css/bootstrap.css'
                    ],
                    selectize: path.join(staticDir, 'css', 'taggit_selectize', 'css', 'selectize.bootstrap3.css')
                },
                output: {
                    path: djangoOutDir
                },
                module: {
                    rules: [{
                        test: /jquery\.(jsx|js)$/,
                        loader: 'expose-loader?jQuery'
                    }]
                },
                plugins: [
                    new CleanWebpackPlugin([
                        djangoOutDir,
                        path.join(staticDir, 'static-only'),
                    ])
                ]
            });

            const reactConfig = merge(sharedConfig, {
                entry: {
                    react_main: path.join(srcDir, 'app', 'src', 'index.jsx'),
                    react_vendor: 'react'
                },
                output: {
                    path: reactOutDir,
                    library: 'react_app'
                },
                module: {
                    rules: [{
                        test: /.jsx?$/,
                        loader: 'babel-loader',
                        exclude: /node_modules/,
                        query: {
                            presets: ['es2015', 'react']
                        }
                    }]
                },
                plugins: [
                    new CleanWebpackPlugin(reactOutDir)
                ]
            });

            return [djangoConfig, reactConfig];
        };
    }(new ExtractTextPlugin('[name].[chunkhash].css'), webpack));
}());