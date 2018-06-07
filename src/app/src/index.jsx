// jshint esversion: 6

import FormikForm from './components/form';
import React from 'react';
import ReactDOM from 'react-dom';

export function init() {
    const container = document.getElementById('container');
    ReactDOM.render(<FormikForm name='PyCon LT' />, container);
}