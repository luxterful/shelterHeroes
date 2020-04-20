import React, { useContext } from "react";
import { fetcher } from "../../utils/fetcher";
import { UserContext } from "../../components/UserContext";
import { Form, Button, Dropdown } from "react-bootstrap";
import { useFormFields } from "../../utils/hook";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBug } from "@fortawesome/free-solid-svg-icons";

const QuickLoginBtn = ({ email, password, children, revalidate, as: Component = Button }) => {
  return (
    <Component
      variant="primary"
      type="submit"
      onClick={(e) => {
        e.preventDefault();
        fetcher("/api/auth/signin/", {
          method: "POST",
          body: {
            email: email,
            password: password,
          },
        }).then(() => {
          revalidate();
        });
      }}
    >
      {children}
    </Component>
  );
};

export const FormLogin = () => {
  const { revalidate } = useContext(UserContext);
  const [fields, handleFieldChange] = useFormFields({
    login_email: "",
    login_password: "",
  });
  return (
    <Form
      onSubmit={(e) => {
        e.preventDefault();
        fetcher("/api/auth/signin/", {
          method: "POST",
          body: {
            email: fields.login_email,
            password: fields.login_password,
          },
        }).then(() => {
          revalidate();
        });
      }}
    >
      <Form.Group controlId="login_email">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="Enter email" value={fields.login_email} onChange={handleFieldChange} />
      </Form.Group>

      <Form.Group controlId="login_password">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          placeholder="Password"
          value={fields.login_password}
          onChange={handleFieldChange}
        />
      </Form.Group>
      <Button type="submit">Login</Button>
      <Dropdown style={{ display: "inline", marginLeft: "10px" }}>
        <Dropdown.Toggle variant="success" id="dropdown-basic">
          <FontAwesomeIcon icon={faBug} />
        </Dropdown.Toggle>

        <Dropdown.Menu>
          <QuickLoginBtn as={Dropdown.Item} email="harry@labby.com" password="qwerty" revalidate={revalidate}>
            Login as Harry
          </QuickLoginBtn>
          <QuickLoginBtn as={Dropdown.Item} email="peter@bauer.net" password="qwerty" revalidate={revalidate}>
            Login as Peter
          </QuickLoginBtn>
          <QuickLoginBtn as={Dropdown.Item} email="chuck@norris.war" password="qwerty" revalidate={revalidate}>
            Login as Chuck Norris
          </QuickLoginBtn>
        </Dropdown.Menu>
      </Dropdown>
    </Form>
  );
};

export const FormRegister = () => {
  const { revalidate } = useContext(UserContext);
  const [fields, handleFieldChange] = useFormFields({
    register_email: "",
    register_full_name: "",
    register_password: "",
  });
  return (
    <Form
      onSubmit={(e) => {
        e.preventDefault();
        fetcher("/api/auth/signup/", {
          method: "POST",
          body: {
            email: fields.register_email,
            full_name: fields.register_full_name,
            password: fields.register_password,
          },
        }).then(() => {
          revalidate();
        });
      }}
    >
      <Form.Group controlId="register_email">
        <Form.Label>Email address</Form.Label>
        <Form.Control
          type="email"
          placeholder="Enter email"
          value={fields.register_email}
          onChange={handleFieldChange}
        />
      </Form.Group>
      <Form.Group controlId="register_full_name">
        <Form.Label>Full Name</Form.Label>
        <Form.Control placeholder="Name" value={fields.register_full_name} onChange={handleFieldChange} />
      </Form.Group>
      <Form.Group controlId="register_password">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          placeholder="Password"
          value={fields.register_password}
          onChange={handleFieldChange}
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Register
      </Button>
    </Form>
  );
};
