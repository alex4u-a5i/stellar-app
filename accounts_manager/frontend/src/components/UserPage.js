import React, {Component} from 'react';

export default class UserPage extends Component {
    constructor(props) {
        
        super(props);
        this.state = {
            name: "",
        };

        this.public_key = this.props.match.params.public_key;
        this.getUserDetails();
    }

    getUserDetails() {
        fetch('/api/get-user' + '?public_key=' + this.public_key).then((response) => response.json()
        ).then((data) => {
            this.setState({
                name: data.name,
            })
        });
    }
    
    render() {
        return <div>
            <h3> Name: {this.state.name} </h3>
            <p> Public key: {this.public_key} </p>
        </div>
    }
}