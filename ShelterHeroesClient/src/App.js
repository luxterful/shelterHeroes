import React from "react";
import "./App.scss";
import "bootstrap/dist/css/bootstrap.min.css";
import { UserContextProvider } from "./components/UserContext";
import Router from "./Router";

function App() {
  return (
    <UserContextProvider>
      <Router />
    </UserContextProvider>
  );
}

export default App;
