import React from "react";
import { FormLogin, FormRegister } from "./forms";
import styles from "./index.module.scss";
import headerImage from "../../Assets/landing_header.jpg";
import logo from "../../Assets/shelterhero_logo.png";
import { Navbar, Container, Button, Modal } from "react-bootstrap";

const Landing = () => {
  const [loginModalShow, setLoginModalShow] = React.useState(false);
  const [registerModalShow, setRegisterModalShow] = React.useState(false);

  return (
    <>
      <div className={styles.customHeader} style={{ backgroundImage: `url(${headerImage})` }}>
        <Navbar bg="transparent" variant="dark" fixed="top" className={styles.customNavbar}>
          <Container>
            <Navbar.Brand>
              <img src={logo} height="42px" /> Shelter Heroes
            </Navbar.Brand>
          </Container>
        </Navbar>
        <Container>
          <p className={styles.customPreHeadline}>There are thousands of animals living in shelters right now.</p>
          <p className={styles.customHeadline}>
            Make a <br />
            difference!
          </p>
          <p className={styles.customSubtitle}>
            <Button onClick={() => setRegisterModalShow(true)} className={styles.customLoginButton} variant="warning">
              Register
            </Button>
            <Button
              onClick={() => setLoginModalShow(true)}
              className={styles.customLoginButton}
              variant="outline-warning"
            >
              Login
            </Button>
          </p>
        </Container>
      </div>
      <Container>
        <Modal
          onHide={() => setLoginModalShow(false)}
          show={loginModalShow}
          aria-labelledby="contained-modal-title-vcenter"
          centered
        >
          <Modal.Header>
            <Modal.Title>Login</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <FormLogin />
          </Modal.Body>
        </Modal>

        <Modal
          onHide={() => setRegisterModalShow(false)}
          show={registerModalShow}
          aria-labelledby="contained-modal-title-vcenter"
          centered
        >
          <Modal.Header>
            <Modal.Title>Registration</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <FormRegister />
          </Modal.Body>
        </Modal>
      </Container>
    </>
  );
};
export default Landing;
