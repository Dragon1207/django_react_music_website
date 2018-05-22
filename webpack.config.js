// jshint esversion: 6
(function () {
    'use strict';
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    const CleanWebpackPlugin = require('clean-webpack-plugin');

    (function (extractMainCss, extractVendorCss) {
        module.exports = (env, argv) => {
            const BundleTracker = require('webpack-bundle-tracker');
            const path = require('path');
            const isDevMode = argv.mode === 'development';
            const merge = require('webpack-merge');
            const staticDir = path.resolve('./static');
            const srcDir = path.resolve('./src');
            const djangoOutDir = path.join(staticDir, 'static');
            const reactOutDir = path.join(srcDir, 'app', 'dist');
            const cleanOptions = {
                exclude: ['vendor.js', 'vendor.css', 'selectize.js', 'selectize.css', 'admin', 'rest_framework', 'taggit_selectize']
            };

            const sharedConfig = {
                context: __dirname,
                output: {
                    publicPath: '/static/',
                    filename: '[name].[hash].js'
                },
                module: {
                    rules: [{
                        test: /\.(png|woff|woff2|eot|ttf|svg)(\?|$)/,
                        use: 'url-loader?limit=100000'
                    }]
                },
                plugins: [
                    new BundleTracker({
                        filename: path.join('static', 'manifest.json')
                    })
                ]
            };

            const djangoSharedConfig = merge(sharedConfig, {
                output: {
                    path: djangoOutDir
                },
                plugins: [
                    new CleanWebpackPlugin([
                        path.join(djangoOutDir, '*.*'),
                        path.join(staticDir, 'static-only', '*.*'),
                    ], cleanOptions)
                ]
            });

            const djangoVendorConfig = merge(djangoSharedConfig, {
                entry: {
                    vendor: [
                        'jquery', // jQuery is required by taggit-selectize
                        'bootstrap',
                        'bootstrap/dist/css/bootstrap.css'
                    ],
                    selectize: path.join(staticDir, 'css', 'taggit_selectize', 'css', 'selectize.bootstrap3.css')
                },
                output: {
                    filename: '[name].js'
                },
                module: {
                    rules: [{
                        test: /jquery\.(jsx|js)$/,
                        loader: 'expose-loader?jQuery'
                    }, {
                        test: /\.css(\?|$)/,
                        use: extractVendorCss.extract({
                            use: [
                                isDevMode ? 'css-loader' : 'css-loader?minimize', 'postcss-loader'
                            ]
                        })
                    }]
                },
                plugins: [
                    extractVendorCss
                ]
            });

            const djangoMainConfig = merge(djangoSharedConfig, {
                entry: {
                    main: [
                        path.join(staticDir, 'css', 'main.css'),
                        path.join(staticDir, 'img', 'background.png')
                    ]
                },
                module: {
                    rules: [{
                        test: /\.css(\?|$)/,
                        use: extractMainCss.extract({
                            use: [
                                isDevMode ? 'css-loader' : 'css-loader?minimize', 'postcss-loader'
                            ]
                        })
                    }]
                },
                plugins: [
                    extractMainCss
                ]
            });

            const reactSharedConfig = merge(sharedConfig, {
                output: {
                    path: reactOutDir
                },
                plugins: [
                    new CleanWebpackPlugin(path.join(reactOutDir, '*.*'))
                ]
            });

            const reactVendorConfig = merge(reactSharedConfig, {
                entry: {
                    react_vendor: 'react'
                },
                output: {
                    filename: '[name].js'
                },
                module: {
                    rules: [{
                        test: /\.css(\?|$)/,
                        use: extractVendorCss.extract({
                            use: [
                                isDevMode ? 'css-loader' : 'css-loader?minimize', 'postcss-loader'
                            ]
                        })
                    }]
                },
                plugins: [
                    extractVendorCss
                ]
            });

            const reactMainConfig = merge(reactSharedConfig, {
                entry: {
                    react_main: path.join(srcDir, 'app', 'src', 'index.jsx')
                },
                output: {
                    library: 'react_app'
                },
                module: {
                    rules: [{
                        test: /.jsx?$/,
                        loader: 'babel-loader',
                        exclude: /node_modules/,
                        query: {
                            'plugins': ['transform-class-properties'],
                            presets: ['es2015', 'react']
                        }
                    }, {
                        test: /\.css(\?|$)/,
                        use: extractMainCss.extract({
                            use: [
                                isDevMode ? 'css-loader' : 'css-loader?minimize', 'postcss-loader'
                            ]
                        })
                    }]
                },
                plugins: [
                    extractMainCss
                ]
            });

            return [djangoVendorConfig, djangoMainConfig, reactVendorConfig, reactMainConfig];
        };
    }(new ExtractTextPlugin('[name].[chunkhash].css'), new ExtractTextPlugin('[name].css')));
}());