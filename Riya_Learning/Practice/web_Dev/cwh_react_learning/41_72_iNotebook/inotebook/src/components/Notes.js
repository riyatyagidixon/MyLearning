import React, { useRef } from 'react'
import Noteitem from './Noteitem';
import AddNote from './AddNote';
import { useContext } from 'react';
import noteContext from '../context/notes/noteContext';
import { useEffect } from 'react';

const Notes = () => {
    const context = useContext(noteContext);
    const { notes, getNotes, editNote } = context;
    useEffect(() => {
        getNotes()
        // eslint-disable-next-line
    }, [])
    const ref = React.useRef(null);

    const updateNote = (note) => {
        console.log("update function calling");
        console.log("ref==>" + ref.current);
        console.log(note);
        ref.current.click();
    }

    return (
        <>
            <button ref={ref} type="button" className="btn btn-primary d-none" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Launch demo modal
            </button>
            <div className="modal fade" id="exampleModal" tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div className="modal-dialog" >
                    <div className="modal-content">
                        <div className="modal-header">
                            <h5 className="modal-title" id="exampleModalLabel">Edit Notes</h5>
                            <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close">
                            </button>
                        </div>
                        <div className="modal-body">
                            ...
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" className="btn btn-primary">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
            <div className='row my-3'>
                <h1>Your Notes</h1>
                {notes.map((note) => {
                    return <Noteitem key={note.id} updateNote={updateNote} note={note} />
                })}
            </div>

        </>
    )
}

export default Notes
