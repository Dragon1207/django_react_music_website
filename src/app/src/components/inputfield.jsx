import { ControlLabel, FormGroup, HelpBlock } from 'react-bootstrap';

import { Field } from 'formik';
import PropTypes from 'prop-types';
import React from 'react';

const InputField = ({ field, form, ...rest }) => {
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

InputField.propTypes = {
    field: PropTypes.shape({
        name: PropTypes.string.required
    }),
    form: PropTypes.shape({
        errors: PropTypes.array.required,
        touched: PropTypes.array.required
    })
};

export default InputField;