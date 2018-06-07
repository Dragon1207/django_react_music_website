// jshint esversion: 6

import React, { Component } from 'react';
import { bool, object, string } from 'yup';

import DjangoCSRFToken from 'django-react-csrftoken';
import { Formik } from 'formik';
import { hot } from 'react-hot-loader';

class FormikForm extends Component {
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
                                        <label>Name:
                                            <input
                                                name="name"
                                                id="name"
                                                type="text"
                                                value={values.name}
                                                onChange={handleChange}
                                            />
                                        </label>
                                        {touched.name && errors.name && <div>{errors.name}</div>}

                                        <label>Email:
                                            <input
                                                name="email"
                                                type="text"
                                                value={values.email}
                                                onChange={handleChange}
                                            />
                                        </label>
                                        {touched.email && errors.email && <div>{errors.email}</div>}

                                        <label>Is active:
                                            <input
                                                name="isActive"
                                                type="checkbox"
                                                checked={values.isActive}
                                                onChange={handleChange}
                                            />
                                        </label>
                                        {touched.isActive && errors.isActive && <div>{errors.isActive}</div>}

                                        <button type="submit" disabled={isSubmitting}>Add User
                                        </button>
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
