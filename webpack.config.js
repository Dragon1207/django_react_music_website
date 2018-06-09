// jshint esversion: 6
(function () {
    'use strict';
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    const CleanWebpackPlugin = require('clean-webpack-plugin');

    (function (extractMainCss, extractVendorCss, webpack) {
        module.exports = (env, argv) => {
            const BundleTracker = require('webpack-bundle-tracker');
            const path = require('path');
            const isDevMode = argv.mode === 'development';
            const isHot = !!argv.hot;
            const webpackDevServerPath = 'http://localhost:3000';
            let publicPath = '/static/';
            if (isDevMode && isHot) {
                publicPath = webpackDevServerPath + publicPath;
            }
            const merge = require('webpack-merge');
            const staticDir = path.resolve('./static');
            const outDir = path.join(staticDir, 'static');

            const sharedConfig = {
                context: __dirname,
                mode: argv.mode || 'development',
                entry: isDevMode && isHot ? ['webpack-dev-server/client?' + webpackDevServerPath] : undefined,
                output: {
                    path: outDir,
                    publicPath: publicPath,
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
                        path: staticDir,
                        filename: 'manifest.json'
                    }),
                    new CleanWebpackPlugin(path.join(outDir, '*.*'))
                ],
                devServer: {
                    headers: {
                        'Access-Control-Allow-Origin': '*'
                    }
                }
            };

            const djangoSharedConfig = merge(sharedConfig, {
                plugins: [
                    new CleanWebpackPlugin([
                        path.join(staticDir, 'static-only', '*.*'),
                    ], {
                        exclude: ['django_vendor.js', 'django_vendor.css', 'selectize.js', 'selectize.css', 'admin',
                            'rest_framework', 'taggit_selectize'
                        ]
                    })
                ]
            });

            const djangoVendorConfig = merge(djangoSharedConfig, {
                entry: {
                    django_vendor: [
                        'jquery', // jQuery is required by taggit-selectize
                        'bootstrap',
                        'bootstrap/dist/css/bootstrap.css'
                    ],
                    selectize: [
                        path.join(staticDir, 'css', 'taggit_selectize', 'css', 'selectize.bootstrap3.css')
                    ]
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
                    django_main: [
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

            const reactVendorConfig = merge(sharedConfig, {
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
                    extractVendorCss,
                    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
                ]
            });

            const reactMainConfig = merge(sharedConfig, {
                entry: {
                    main: path.join(__dirname, 'src', 'app', 'src', 'index.jsx')
                },
                output: {
                    library: 'react_app'
                },
                resolve: {
                    extensions: ['.js', '.jsx', '.json', '.css']
                },
                module: {
                    rules: [{
                        test: /.jsx?$/,
                        loader: 'babel-loader',
                        exclude: /node_modules/,
                        query: {
                            'plugins': ['transform-class-properties', 'react-hot-loader/babel', 'transform-object-rest-spread'],
                            presets: ['es2015', 'react'],
                        }
                    }, {
                        test: /\.css(\?|$)/,
                        use: [
                            'style-loader', isDevMode ? 'css-loader' : 'css-loader?minimize', 'postcss-loader'
                        ],
                        exclude: /node_modules\/(?!(react-tag-input\/example\/reactTags.css))/
                    }]
                },
            });

            return [djangoVendorConfig, djangoMainConfig, reactVendorConfig, reactMainConfig];
        };
    }(new ExtractTextPlugin('[name].[chunkhash].css'), new ExtractTextPlugin('[name].css'), new require('webpack')));
}());