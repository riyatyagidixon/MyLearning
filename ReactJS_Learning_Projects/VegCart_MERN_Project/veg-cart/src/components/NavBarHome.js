import { React } from "react";
import { Link, useLocation } from "react-router-dom";

export default function NavBarHome() {
    let location = useLocation();

    return (
        <div>
            {!localStorage.getItem("auth-token") && (
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div className="container-fluid">
                        <Link className="navbar-brand" to="/">
                            vCart
                        </Link>
                        <button
                            className="navbar-toggler"
                            type="button"
                            data-bs-toggle="collapse"
                            data-bs-target="#navbarSupportedContent"
                            aria-controls="navbarSupportedContent"
                            aria-expanded="false"
                            aria-label="Toggle navigation"
                        >
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                                <li className="nav-item">
                                    <Link className={`nav-link ${location.pathname === "/home" ? "active" : ""}`} to="/home">
                                        Home
                                    </Link>
                                </li>
                            </ul>
                            {
                                <form className="d-flex">
                                    <Link className="btn btn-primary mx-2" to="/login" role="button">
                                        Login
                                    </Link>
                                    <Link className="btn btn-primary mx-2" to="/signup" role="button">
                                        Signup
                                    </Link>
                                </form>
                            }
                        </div>
                    </div>
                </nav>
            )}
        </div>
    );
}
