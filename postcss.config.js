// jshint esversion: 6
'use strict';
module.exports = ({
    env
}) => ({
    plugins: {
        'autoprefixer': env === 'production'
    }
});