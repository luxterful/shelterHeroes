import React, { useState } from "react";
import { InputGroup, FormControl, Button } from "react-bootstrap";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { Link } from "react-router-dom";

const CommentInput = () => {
  const [comment, setComment] = useState("");
  const sendComment = () => {
    fetcher("/api/auth/signin/", {
      method: "POST",
      body: {
        email: email,
        password: password,
      },
    }).then(() => {
      revalidate();
    });
  };

  return (
    <div>
      <InputGroup className="mb-3">
        <FormControl
          onKeyUp={(e) => {
            setComment(e.target.value);
          }}
          placeholder="comment..."
          aria-label="comment..."
          aria-describedby="basic-addon"
        />
        <InputGroup.Append>
          <Button variant="primary">SEND</Button>
        </InputGroup.Append>
      </InputGroup>
    </div>
  );
};
export default CommentInput;
