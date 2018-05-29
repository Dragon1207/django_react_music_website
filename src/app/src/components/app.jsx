// jshint esversion: 6
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { hot } from 'react-hot-loader';

class App extends Component {
    static propTypes = {
        name: PropTypes.string.isRequired,
    };

    render() {
        return <div className="row">
            <div className="col-sm-12 col-md-7">
                <div className="panel panel-default">
                    <div className="panel-body">
                        new content3
                    </div>
                </div>
            </div>
        </div>;
    }
}

export default hot(module)(App);
