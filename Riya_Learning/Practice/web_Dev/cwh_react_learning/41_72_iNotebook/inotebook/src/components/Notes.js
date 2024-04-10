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
    const ref = useRef(null)

    const updateNote = (note) => {
        console.log("update function calling");
        console.log("ref==>" + ref.current);
        console.log(note);
        ref.current.click();
    }

    return (
        <>
            < button ref={ref} type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Launch demo modal
            </button>
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">Edit Note</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            ...
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
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
