import './App.css';
import { React, useState } from 'react';

function App() {
  // let name = "Riya";
  const [name, setName] = useState("Riya");
  const [flag, setFlag] = useState(false);
  const [steps, setSteps] = useState(0);
  const [names, setNames] = useState([]);

  function changeName() {
    console.log("i clicked");
    setName("tyagi");
    setFlag(!flag);
  }

  function increment() {
    setSteps((e) => e + 1);
    setSteps((e) => e + 1);
  }

  function decrement() {
    setSteps(steps - 1);
  }

  function addNames(e) {
    e.preventDefault(); // to stop the page refresh
    setNames([...names, { id: names.length, name }]);
    console.log("names===> ", names);
  }

  return (
    <div className="App">
      <h2>Hello {flag ? "" : name} </h2>
      <button onClick={changeName}>click me</button>
      <hr></hr>
      <button onClick={increment}>+</button>
      <h2>{steps}</h2>
      <button onClick={decrement}>-</button>
      <hr></hr>
      <form onSubmit={addNames}>
        <input
          type='text'
          name='name'
          placeholder='your name'
          onChange={(e) => setName(e.target.value)}>
        </input>
        <div>
          <button>Submit</button>
        </div>
      </form>
      <hr></hr>
      <ul>
        {names.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
