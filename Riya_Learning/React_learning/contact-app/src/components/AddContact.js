import React from "react";

class AddContact extends React.Component {
    state = {
        name: "",
        email: ""
    };

    add = (e) => {
        e.preventDefault(); // prevent to refresh the page
        if (this.state.email=== "" || this.state.name === "") {
            alert ("These fields are mandatory");
            return;
        }
        console.log("state===>", this.state);
        this.props.myAddContactHandler(this.state);
        this.setState({name: "", email: ""});
    }

    render() {
        return (
            <div className="ui main">
                <hr></hr>
                <h2>Add Contact</h2>
                <form className="ui form" onSubmit={this.add}>
                    <div className="field">
                        <label>Name</label>
                        <input 
                            type="text" 
                            name="name" 
                            placeholder="Full name"
                            value = {this.state.name}
                            onChange={(e) => this.setState({name: e.target.value })}
                            >
                            </input>
                    </div>
                    <div className="field">
                        <label>Email</label>
                        <input 
                            type="email" 
                            name="Email" 
                            placeholder="Your email id"
                            value = {this.state.email}
                            onChange={(e) => this.setState({email: e.target.value })}
                            >
                            </input>
                    </div>
                    <button className="ui button pink">Add</button>
                </form>
            </div>

        );
    }
}


export default AddContact;