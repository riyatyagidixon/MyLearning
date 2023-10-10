import './App.css';
import CComponent from './CComponent';
import FComponent from './FComponent';
import { useState } from 'react';

function App() {
  const [cflag, setCflag] = useState(true);

  // const toggleButton = () => {
  //   setCflag(!cflag);
  // }

  return (
    <div className="App">
      <hr></hr>
      <h2>Hello ! This is App Component</h2>
      <button onClick ={() => setCflag(!cflag)}>Toggle the Component</button>
      <hr></hr>
      {cflag? <CComponent/>: <FComponent/>}
      <hr></hr>
    </div>
  );
}

export default App;
