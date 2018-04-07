// jshint esversion: 6
import { Component } from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

class HelloMessage extends Component {
    static propTypes = {
        name: PropTypes.string.isRequired,
    };

    render() {
        return <div className='message'>
            Hello, {this.props.name}
        </div>;
    }
}
// HelloMessage.propTypes = {
//     name: PropTypes.string.isRequired,
// };

module.exports = {
    init: function () {
        const container = document.getElementById('container');
        ReactDOM.render(< HelloMessage name='PyCon LT' />, container);
    }
};