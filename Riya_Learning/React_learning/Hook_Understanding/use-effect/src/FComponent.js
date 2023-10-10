import React, { useState, useEffect } from "react";

function FComponent() {
    const [message, setMessage] = useState("Function Component");
    const [time, setTime] = useState(new Date().toString());

    function showDate() {
        setTime(new Date().toString());
    }

    useEffect(() => {
        // Initialization
        const interval = setInterval(showDate, 1000);

        //cleanup
        return () => {
            console.log("cleanup of interval");
            clearInterval(interval);
        }
    }, [time, message]); // Dependencies

    function changeMessage() {
        setMessage("I am Riya " + Math.floor((Math.random() * 100) + 1)); // 1 to 100 range 
    }

    return (
        <div>
            <h2>I am in Function Component</h2>
            <button onClick={changeMessage}>Change Message</button>
            <button onClick={showDate}>Show Date</button>
            <h2>{message}</h2>
            <div>{time}</div>
        </div>
    );
}

export default FComponent;