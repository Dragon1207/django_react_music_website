// jshint esversion: 6
import React from 'react';
import ReactDOM from 'react-dom';

function HelloMessage(props) {
    return (
        <div className='message'>
            Hello, {props.name}
        </div>
    )
}

module.exports = {
    init: function () {
        const container = document.getElementById('container');
        ReactDOM.render(< HelloMessage name='PyCon LT' />, container);
    }
};

// ReactDOM.render(< div > Hello! < /div>, document.getElementById('container'));