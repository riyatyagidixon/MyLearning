import React from "react";
import noteContext from "./noteContext";
import { useState } from "react";

const NoteState = (props) => {
    const host = "http://localhost:5000";
    const notesInitial = []

    const [notes, setNotes] = useState(notesInitial)

    //Get all  notes
    const getNotes = async () => {
        //API CAll
        const response = await fetch(`${host}/api/notes/fetchallnotes`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYwM2IzZGI2OWE1ZTQ1MDAzZDQ3ZDc4In0sImlhdCI6MTcxMTY5MzA0M30.y25YwI4gKW7IzQVZh5p5LS68JibV0KPl5eSeXJpiZ90"
            }
        });
        const json = await response.json()
        console.log(json)
        setNotes(json)
    }

    //Add a note 
    const addNote = async (title, description, tag) => {
        //API CAll
        const response = await fetch(`${host}/api/notes/addnote`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYwM2IzZGI2OWE1ZTQ1MDAzZDQ3ZDc4In0sImlhdCI6MTcxMTY5MzA0M30.y25YwI4gKW7IzQVZh5p5LS68JibV0KPl5eSeXJpiZ90"
            },
            body: JSON.stringify({ title, description, tag })
        });

        const note = {
            "_id": "69060baf1b187a9256ecbcc81",
            "user": "6603b3db69a5e45003d47d78",
            "title": title,
            "description": description,
            "tag": tag,
            "date": "2024-04-02T07:09:15.934Z",
            "__v": 0
        };
        setNotes(notes.concat(note))
    }

    // delete a note
    const deleteNote = async (id) => {
        // API CAll
        console.log(id);
        const response = await fetch(`${host}/api/notes/deletenote/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYwM2IzZGI2OWE1ZTQ1MDAzZDQ3ZDc4In0sImlhdCI6MTcxMTY5MzA0M30.y25YwI4gKW7IzQVZh5p5LS68JibV0KPl5eSeXJpiZ90",
            }
        });
        console.log("checking delete fnctn ")
        const json = response.json();
        console.log(json);

        console.log("Deleting the note with id" + id);
        const newNotes = notes.filter((note) => { return note._id !== id })
        setNotes(newNotes)
    }

    // Edit a note
    const editNote = async (id, title, description, tag) => {
        // API Call
        const response = await fetch(`${host}api/notes/updatenote/${id}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYwM2IzZGI2OWE1ZTQ1MDAzZDQ3ZDc4In0sImlhdCI6MTcxMTY5MzA0M30.y25YwI4gKW7IzQVZh5p5LS68JibV0KPl5eSeXJpiZ90"
            },
            body: JSON.stringify({ title, description, tag })
        });
        const json = response.json();
        //Logic to edit in client
        for (let index = 0; index < notes.length; index++) {
            const element = notes[index];
            if (element._id === id) {
                element.title = title;
                element.description = description;
                element.tag = tag;
            }
        }
    }

    return (
        <noteContext.Provider value={{ notes, addNote, deleteNote, editNote, getNotes }}>
            {props.children}
        </noteContext.Provider>
    )

}
export default NoteState;