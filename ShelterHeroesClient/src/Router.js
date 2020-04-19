import React, { useContext } from "react";
import { BrowserRouter as Router, Switch, Route, Link, NavLink, Redirect } from "react-router-dom";
import "./App.scss";
import "bootstrap/dist/css/bootstrap.min.css";
import { Navbar, Container, Nav } from "react-bootstrap";
import Feed from "./pages/feed";
import Animal from "./pages/animal";
import Landing from "./pages/landing";
import Post from "./pages/post";
import Shelter from "./pages/shelter";
import Explore from "./pages/explore";
import { UserContext } from "./components/UserContext";
import { fetcher } from "./utils/fetcher";

function App() {
  const { user, revalidate } = useContext(UserContext);
  return (
    <Router>
      {user?.pk ? (
        <>
          <Navbar bg="dark" variant="dark" fixed="top">
            <Container>
              <Link to="/">
                <Navbar.Brand>Shelter Heroes</Navbar.Brand>
              </Link>
              <Nav className="mr-auto">
                <NavLink exact to="/" className="nav-link" activeClassName="active">
                  Home
                </NavLink>
                <NavLink exact to="/explore" className="nav-link" activeClassName="active">
                  Explore
                </NavLink>
              </Nav>
              <Nav>
                <NavLink
                  to="#"
                  className="nav-link"
                  activeClassName="active"
                  onClick={() => {
                    fetcher("/api/auth/signout/", { method: "POST" }).then(() => {
                      revalidate();
                    });
                  }}
                >
                  {user?.full_name}
                </NavLink>
              </Nav>
            </Container>
          </Navbar>
          <Container style={{ marginTop: "72px" }}>
            <Switch>
              <Route exact path="/explore" component={Explore} />
              <Route exact path="/animals/:uid" component={Animal} />
              <Route exact path="/posts/:uid" component={Post} />
              <Route exact path="/shelters/:uid" component={Shelter} />
              <Route exact path="/" component={Feed} />
              <Router>404</Router>
            </Switch>
          </Container>
        </>
      ) : (
        <>
          <Switch>
            <Route exact path="/">
              <Landing />
            </Route>
            <Redirect to="/" />
          </Switch>
        </>
      )}
    </Router>
  );
}

export default App;
