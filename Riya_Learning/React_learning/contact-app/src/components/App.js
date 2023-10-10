import React from "react";
import './App.css';
import { v4 as uuid } from 'uuid'; 
import Header from "./Header";
import AddContact from "./AddContact";
import ContactList from "./ContactList";
import { useState, useEffect } from 'react';

// const contactlist = [
//   {
//     id: "1",
//     name: "Riya",
//     email: "riya@g.com"
//   },
//   {
//     id: "2",
//     name: "tyagi",
//     email: "tyagi@g.com"
//   }
// ];

function App() {
  const LOCAL_STORAGE_KEY = "riya";
  const [contacts, setContacts] = useState([]);

  const addContactHandler = (c) => {
    console.log("contacts====> ", c);
    setContacts([...contacts, {id: uuid(), ...c}]);
  }

  useEffect(() => {
    const retriveContacts = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
    if (retriveContacts.length) {
      setContacts(retriveContacts);
    }
  }, []); // [] is called when page refresh

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(contacts));
  }, [contacts]); // It will call when "contacts" get updated

const removeContacthandler = (id) => {
  console.log("removeContactHandler is ==> ", id);
  const newContactList = contacts.filter((c) => {
    return c.id !==id;
  })
  setContacts(newContactList);
}

  return (
    <div className="ui container">
      <Header />
      <AddContact myAddContactHandler={addContactHandler} />
      <ContactList mycontacts={contacts} getContactId={removeContacthandler} />
    </div>

  );
}

export default App;


