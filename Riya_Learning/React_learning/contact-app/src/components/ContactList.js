import React from "react";
import ContactCard from "./ContactCard";

const ContactList = (props) => {
    // console.log(props.mycontacts[1].email);
   
    const deleteContacthandler = (id) => {
        props.getContactId(id);
    }
   
    const renderContactList = props.mycontacts.map((contact) => {
        return (
            <ContactCard 
                mycontact={contact}
                clickHandler = {deleteContacthandler}
                key ={contact.id}/>
        );
    });
    return <div className="ui celled list">{renderContactList}</div>
}

export default ContactList;