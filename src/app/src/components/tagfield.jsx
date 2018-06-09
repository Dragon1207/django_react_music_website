import 'react-tag-input/example/reactTags.css';

import { Component } from 'react';
import { FormGroup } from 'react-bootstrap';
import PropTypes from 'prop-types';
import React from 'react';
import { WithContext as ReactTags } from 'react-tag-input';

const KeyCodes = {
    comma: 188,
    enter: 13,
};
const delimiters = [KeyCodes.comma, KeyCodes.enter];

export default class TagField extends Component {
    constructor(props) {
        super(props);
        this.state = {
            tags: [
                { id: 'Thailand', text: 'Thailand' },
                { id: 'India', text: 'India' }
            ],
            suggestions: [
                { id: 'USA', text: 'USA' },
                { id: 'Germany', text: 'Germany' },
                { id: 'Austria', text: 'Austria' },
                { id: 'Costa Rica', text: 'Costa Rica' },
                { id: 'Sri Lanka', text: 'Sri Lanka' },
                { id: 'Thailand', text: 'Thailand' }
            ]
        };
        this.name = this.props.field.name;
        this.updateProps();
    }

    updateProps = () => { this.props.onChange(this.name, this.state.tags); }

    handleAddition = (tag) => {
        this.setState(state => ({ tags: [...state.tags, tag] }),
            () => { this.updateProps(); }
        );
    }

    handleDelete = (i) => {
        const { tags } = this.state;
        this.setState({
            tags: tags.filter((tag, index) => index !== i),
        },
        () => { this.updateProps(); }
        );
    }

    handleDrag = (tag, currPos, newPos) => {
        const tags = [...this.state.tags];
        const newTags = tags.slice();

        newTags.splice(currPos, 1);
        newTags.splice(newPos, 0, tag);

        // re-render
        this.setState({ tags: newTags });
    }

    static propTypes = {
        onChange: PropTypes.func,
        field: PropTypes.shape({
            name: PropTypes.string
        })
    }

    render() {
        return < FormGroup>
            <ReactTags tags={this.state.tags} suggestions={this.state.suggestions} delimiters={delimiters}
                handleAddition={this.handleAddition} handleDelete={this.handleDelete} handleDrag={this.handleDrag}
            />
        </FormGroup>;
    }
}
