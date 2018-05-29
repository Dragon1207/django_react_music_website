// jshint esversion: 6
import ReactDOM from 'react-dom';
import App from './components/app';
import React from 'react';

export function init() {
    const container = document.getElementById('container');
    ReactDOM.render(<App name='PyCon LT' />, container);
}