import React, { useState } from "react";

export default function Textform(props) {
  const handleUpClick = () => {
    // console.log("uppercase was clicked" + text);
    let newText = text.toUpperCase();
    setText(newText);
  };

  const handleLowClick = () => {
    let newText = text.toLowerCase();
    setText(newText);
  };

  const handleClearClick = () => {
    let newText = "";
    setText(newText);
  };

  const handleOnChange = (event) => {
    setText(event.target.value);
  };

  const handleCopy = () => {
    let text = document.getElementById("myBox");
    text.select();
    navigator.clipboard.writeText(text.value);
  };

  const handleExtraSpaces = () => {
    let newText = text.split(/[ ]+/);
    setText(newText.join("."));
  };

  const [text, setText] = useState("");
  //   text = "new text " // wrong way to change the state
  //   setText("new text"); // correct way

  return (
    <div>
      <h1>{props.heading}</h1>
      <div className="mb=3">
        <textarea
          className="form-control"
          value={text}
          onChange={handleOnChange}
          id="myBox"
          rows="8"
        ></textarea>
      </div>
      <button className="btn btn-primary mx-1" onClick={handleUpClick}>
        Convert to Uppercase
      </button>
      <button className="btn btn-primary mx-1" onClick={handleLowClick}>
        Convert to Lowercase
      </button>
      <button className="btn btn-primary mx-1" onClick={handleClearClick}>
        Clear Text
      </button>
      <button className="btn btn-primary mx-1" onClick={handleCopy}>
        Copy Text
      </button>
      <button className="btn btn-primary mx-1" onClick={handleExtraSpaces}>
        Remove Extra Spaces
      </button>
      <div className="container my-3">
        <h1>Your text Summary</h1>
        <p>
          {text.split(" ").length}words and {text.length}characters
        </p>
        <p>{0.008 * text.split(" ").length}Minutes read</p>
        <h3>Preview</h3>
        <p>{text}</p>
      </div>
    </div>
  );
}
