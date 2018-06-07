// jshint esversion: 6

import { Button, Col, ControlLabel, FormGroup, HelpBlock, Panel, Row } from 'react-bootstrap';
import { Field, Form, Formik } from 'formik';
import React, { Component } from 'react';
import { object, string } from 'yup';

import DjangoCSRFToken from 'django-react-csrftoken';
import PropTypes from 'prop-types';
import { hot } from 'react-hot-loader';
import uniqueId from 'react-html-id';

const InputElement = ({ field, form, ...rest }) => {
    const name = field.name;
    const error = form.errors[name];
    const label = `${name.charAt(0).toUpperCase()}${name.slice(1).toLowerCase()}${rest.required ? '*' : ''}`;
    let rest_without_required = { ...rest };
    delete rest_without_required.required;
    return <FormGroup>
        <ControlLabel htmlFor={rest.id}>{label}</ControlLabel>
        <Field className="form-control" {...field} {...rest_without_required} />
        {form.touched[name] && error && <HelpBlock style={{ color: 'red' }}>{error}</HelpBlock>}
    </FormGroup>;
};

InputElement.propTypes = {
    field: PropTypes.shape({
        name: PropTypes.string.required
    }),
    form: PropTypes.shape({
        errors: PropTypes.array.required,
        touched: PropTypes.array.required
    })
};

class FormikForm extends Component {
    constructor() {
        super();
        uniqueId.enableUniqueIds(this);
    }

    render() {
        return <Formik
            initialValues={{
                artist: '',
                title: '',
                genre: ''
            }}
            validationSchema={object().shape({
                artist: string().required().max(250),
                title: string().required().max(500),
                genre: string().required().max(100)
            })}
            onSubmit={
                values => {
                    event.preventDefault();
                    alert('An album was submitted: ' + JSON.stringify(values));
                }
            }
            render={({ isSubmitting }) => (
                <Row>
                    <Col sm={12} md={7}>
                        <Panel>
                            <Panel.Body>
                                <Form>
                                    <DjangoCSRFToken />
                                    <Field component={InputElement} name="artist" id={this.nextUniqueId()} required />
                                    <Field component={InputElement} name="title" id={this.nextUniqueId()} required />
                                    <Field component={InputElement} name="genre" id={this.nextUniqueId()} required />

                                    <FormGroup>
                                        <Button type="submit" disabled={isSubmitting} bsStyle="primary">Add Album</Button>
                                    </FormGroup>
                                </Form>
                            </Panel.Body>
                        </Panel>
                    </Col>
                </Row>
            )
            }
        />;
    }
}

export default hot(module)(FormikForm);
