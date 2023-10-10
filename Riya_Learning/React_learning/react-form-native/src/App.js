import { useEffect, useState } from "react";
import './App.css';

function App() {
  const initialValue = { username: "", email: "", password: "" }
  const [formValues, setFormValues] = useState(initialValue);
  const [formErrors, setFormErrors] = useState({});
  const [isSubmit, setIsSubmit] = useState(false);
  

  // let count = 0;
  // function handleChange() {
  //   console.log("Riya ", count++);
  // }

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  }

  useEffect(() => {
    console.log(formErrors);
    if (Object.keys(formErrors).length === 0 && isSubmit) {
      console.log(formValues);
    }
  }, [formErrors])

  const handleSubmit = (e) => {
    e.preventDefault();
    // console.log("submit===> ", formValues);
    setFormErrors(validate(formValues));
    setIsSubmit(true);
  }

  function validate(values) {
    const errors = {};
    const regex_email = /^\S+@\S+\.\S+$/i;

    // Usermame Validation
    if (values.username === "") { // Emptyness
      errors.username = "Username is required";
    }

    // Email Validation
    if (values.email === "") { // Emptyness
      errors.email = "Email is required";
    }
    else if (!regex_email.test(values.email)) {
      errors.email = "Email format is incorrect";
    }

    // Password Validation
    if (values.password === "") { // Emptyness
      errors.password = "Password is required";
    }
    else if (values.password.length < 4 || values.password.length > 10) {
      errors.password = "Password length should be between 4 and 10";
    }

    return errors;
  }

  return (
    <div className="container">
      {
        Object.keys(formErrors).length === 0 && isSubmit ?
          (<div 
            className="ui message success"
            style = {
              {
                color: "green",
                background: "yellow"
              }
            }>Signed in successfully</div>) :
          (<div>
            <div
              className="ui message success"
              style={
                {
                  color: "red",
                  background: "yellow"
                }
              }>Signed in failed</div>
            <pre>{JSON.stringify(formValues, undefined, 2)}</pre>
          </div>)
      }
      <form
        onSubmit={handleSubmit}
      >
        <h1>Login Form</h1>
        <div className='ui divider'> </div>
        <div className='ui form'>
          <div className='ui field'>
            <label>Username</label>
            <input
              type="text"
              name="username"
              placeholder='Full name'
              value={formValues.username}
              onChange={handleChange}
            >
            </input>
            <p>{formErrors.username}</p>
          </div>
          <div className='ui field'>
            <label>Email</label>
            <input
              type="email"
              name="email"
              placeholder='Enter email'
              value={formValues.email}
              onChange={handleChange}
            >
            </input>
            <p>{formErrors.email}</p>
          </div>
          <div className='ui field'>
            <label>Password</label>
            <input
              type="password"
              name="password"
              placeholder='Enter password'
              value={formValues.password}
              onChange={handleChange}
            >
            </input>
          </div>
          <p>{formErrors.password}</p>
          <button className='fluid ui button pink'>Submit</button>
        </div>
      </form>

    </div>
  );
}

export default App;
