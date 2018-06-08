// jshint esversion: 6

import { Button, Col, ControlLabel, FormGroup, HelpBlock, Panel, Row } from 'react-bootstrap';
import { Field, Form, Formik } from 'formik';
import React, { Component } from 'react';
import { object, string } from 'yup';

import DjangoCSRFToken from 'django-react-csrftoken';
import InputField from './inputfield';
import TagField from './tagfield';
import { hot } from 'react-hot-loader';
import uniqueId from 'react-html-id';

class FormikForm extends Component {
    constructor(props) {
        super(props);
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
                (values, { setSubmitting }) => {
                    event.preventDefault();
                    setTimeout(() => {
                        alert('An album was submitted: ' + JSON.stringify(values));
                        setSubmitting(false);
                    }, 1000);
                }
            }
            render={({ errors, touched, isSubmitting, setFieldValue }) => (
                <Row>
                    <Col sm={12} md={7}>
                        <Panel>
                            <Panel.Body>
                                <Form>
                                    <DjangoCSRFToken />
                                    <Field component={InputField} name="artist" id={this.nextUniqueId()} required />
                                    <Field component={InputField} name="title" id={this.nextUniqueId()} required />
                                    <Field component={InputField} name="genre" id={this.nextUniqueId()} required />

                                    <FormGroup>
                                        <ControlLabel htmlFor={this.nextUniqueId()}>Album logo</ControlLabel>
                                        <Field name="logo" id={this.lastUniqueId()} type="file"
                                            className="form-control-file" onChange={(event) => {
                                                setFieldValue('file', event.currentTarget.files[0]);
                                            }} />
                                        {touched.logo && errors.logo &&
                                            <HelpBlock style={{ color: 'red' }}>{errors.logo}</HelpBlock>}
                                    </FormGroup>

                                    <Field component={TagField} name="tags" onChange={setFieldValue} />

                                    <FormGroup>
                                        <Button type="submit" disabled={isSubmitting} bsStyle="primary">Add Album
                                        </Button>
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
