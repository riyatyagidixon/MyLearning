import React from "react";
import avatar from "../images/avatar.jpg";

const ContactCard = (props) => {
    const { id, name, email } = props.mycontact;
    const url = "https://source.unsplash.com/1600x900/?nature.water"
    return (
        <div className="item">
            <img className="ui avatar image" src={avatar} alt="NO" />
            <div className="content">
                {/* <div>{id}.</div> */}
                <div className="header">{name}</div>
                <img className="ui avatar image" src={url} alt="NO" />
                <div>{email}</div>
            </div>
            <i className="trash alternate outline icon"
                style={
                    {
                        color: "red",
                        // marginTop: "10px",
                        float: "right",
                        padding: "0px, 40px"

                    }
                }onClick = {() => props.clickHandler(id)}>   
                </i>
        </div>
    );
}

export default ContactCard;