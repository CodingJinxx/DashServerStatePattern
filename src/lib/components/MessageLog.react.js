import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { prop } from 'ramda';

class MessageLog extends Component {
    constructor(props) {
        super(props);
    }

    componentDidMount(){
        setInterval(() => {
            this.props.setProps({trigServLogUpdate : !this.props.trigServLogUpdate})
            console.log("Triggering Server Update")
        }, 1000);
    }
    
    render() {
        let messages = [];
        for(let line of this.props.log){
            messages.push(<li>{line}</li>);
        }

        return (
            <ul>
                {messages}
            </ul>
        );
    }
}

export default MessageLog;

MessageLog.propTypes = {
    id : PropTypes.string,
    log : PropTypes.arrayOf(PropTypes.string).isRequired,
    trigServLogUpdate : PropTypes.bool,
    setProps : PropTypes.func
}

MessageLog.defaultProps = {
    trigServLogUpdate : false
}