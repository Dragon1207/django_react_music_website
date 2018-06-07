// jshint esversion: 6

import React, { Component } from 'react';
import { bool, object, string } from 'yup';

import DjangoCSRFToken from 'django-react-csrftoken';
import { Formik } from 'formik';
import { hot } from 'react-hot-loader';
import uniqueId from 'react-html-id';

class FormikForm extends Component {
    constructor() {
        super();

        uniqueId.enableUniqueIds(this);
    }

    render() {
        return (
            <Formik
                initialValues={{
                    name: '',
                    email: '',
                    isActive: false
                }}
                validationSchema={object().shape({
                    name: string().required('Name is required.'),
                    email: string().email().required('Email is required.'),
                    isActive: bool()
                })}
                onSubmit={
                    values => {
                        event.preventDefault();
                        alert('An user was submitted: ' + JSON.stringify(values));
                    }
                }
                render={({ values, errors, touched, handleChange, handleSubmit, isSubmitting }) => (
                    <div className="row">
                        <div className="col-sm-12 col-md-7">
                            <div className="panel panel-default">
                                <div className="panel-body">
                                    <form method="post" onSubmit={handleSubmit}>
                                        <DjangoCSRFToken />
                                        <div className="form-group">
                                            <label htmlFor={this.nextUniqueId()}>Name:</label>
                                            <input
                                                id={this.lastUniqueId()}
                                                name="name"
                                                type="text"
                                                value={values.name}
                                                onChange={handleChange}
                                                className="form-control"
                                            />
                                            {touched.name && errors.name && <div>{errors.name}</div>}
                                        </div>

                                        <div className="form-group">
                                            <label htmlFor={this.nextUniqueId()}>Email:</label>
                                            <input
                                                id={this.lastUniqueId()}
                                                name="email"
                                                type="email"
                                                value={values.email}
                                                onChange={handleChange}
                                                className="form-control"
                                            />
                                            {touched.email && errors.email && <div>{errors.email}</div>}
                                        </div>

                                        <div className="form-group">
                                            <label htmlFor={this.nextUniqueId()}>Is active:</label>
                                            <input
                                                id={this.lastUniqueId()}
                                                name="isActive"
                                                type="checkbox"
                                                checked={values.isActive}
                                                onChange={handleChange}
                                            />
                                            {touched.isActive && errors.isActive && <div>{errors.isActive}</div>}
                                        </div>

                                        <div className="form-group">
                                            <button type="submit" disabled={isSubmitting} className="btn btn-primary">Add User
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                )
                }
            />
        );
    }
}

export default hot(module)(FormikForm);
