import "./App.css";
// import About from "./components/About/";
import Navbar from "./components/Navbar";
import Textform from "./components/Textform";

function App() {
  return (
    <>
      <Navbar title="textUtils" aboutText="about us" />

      <div className="container my-3">
        <Textform heading="Enter the text to analyze below" />
        {/* <About /> */}
      </div>
    </>
  );
}

export default App;
