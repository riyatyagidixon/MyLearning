import { useForm } from "react-hook-form";
import './App.css';
import { useState } from "react";

function App() {
  const { register, handleSubmit, formState: {errors} } = useForm();
  const [userInfo, setUserInfo] = useState();

  const onSubmit = (data) => {
    setUserInfo(data);
    console.log("data ===> ", data);
    console.log("userInfo ==>", userInfo);
  };
  console.log(errors);

  return (
    <div className="container">
      <pre>{JSON.stringify(userInfo, undefined, 2)}</pre>
      <form onSubmit={handleSubmit(onSubmit)}>
        <h1>Registration Form</h1>
        <div className='ui divider'></div>
        <div className='ui form'>
          <div className="field">
            <label>Username</label>
            <input
              type="text"
              //  name="username"
              placeholder="Full name"
              {...register("username", {
                required: true
              })}
            />
            {errors.username && <p>This field is required</p>}
          </div>
          <div className="field">
            <label>Email id</label>
            <input
              type="email"
              // name="email" 
              placeholder="enter email"
              {...register("email", {
                required: "email is required",
                pattern: {
                  value: /^\S+@\S+\.\S+$/i,
                  message: "This is not a valid email",
                }
              }
              )
              }
            />
            {errors.email && <p>This field is required</p>}
          </div>
          <div className="field">
            <label>Password</label>
            <input
              type="password"
              // name="password" 
              placeholder="enter password"
              {...register("password", {
                required: "password is required",
                minLength: {
                  value: 4,
                  message: "password must be more than 4 characters",
                },
                maxLength: {
                  value: 10,
                  message: "password cannot exceed more than 10 characters",

                }
              }
              )
              }
            />
            {errors.password && <p>This field is required</p>}
          </div>
          <button className="fluid ui button pink">submit</button>
        </div>
      </form>
    </div>
  );
}

export default App;
