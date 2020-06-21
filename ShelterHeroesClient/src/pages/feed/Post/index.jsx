import React, { useState } from "react";
import { Card, Button, Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faComment, faHeart as HeartBorder } from "@fortawesome/free-regular-svg-icons";
import { faHeart as HeartSolid } from "@fortawesome/free-solid-svg-icons";
import ActionButton from "../../../components/ActionButton";

function Post({ post }) {
  const [likeCount, setLikeCount] = useState(post.likes_count);
  return (
    <Card style={{ marginBottom: "20px" }}>
      <Link to={"/posts/" + post.pk}>
        <Card.Img variant="top" src={post.image.image_file} />
      </Link>

      <Card.Body>
        <Card.Title>
          <Link to={"/animals/" + post.posted_by.pk} style={{ fontSize: "20pt", color: "black" }}>
            {post.posted_by.name}
          </Link>
        </Card.Title>
        <Card.Subtitle className="mb-2 text-muted">
          <Link to={"/shelters/" + post.posted_by.shelter.pk} style={{ fontSize: "16pt", color: "black" }}>
            {post.posted_by.shelter.name}
          </Link>
        </Card.Subtitle>
        <Card.Text>{post.text}</Card.Text>

        <ActionButton
          initEnabled={post.liked_by_viewer}
          disableActionPostUrl={"/api/core/posts/" + post.pk + "/unlike"}
          enableActionPostUrl={"/api/core/posts/" + post.pk + "/like"}
          enableActionCallback={() => setLikeCount(likeCount + 1)}
          disableActionCallback={() => setLikeCount(likeCount - 1)}
          contentEnabled={
            <>
              <FontAwesomeIcon icon={HeartSolid} />
              {" " + likeCount}
            </>
          }
          contentDisabled={
            <>
              <FontAwesomeIcon icon={HeartBorder} />
              {" " + likeCount}
            </>
          }
        />
        <Link to={"/posts/" + post.pk} style={{ color: "black" }}>
          <span style={{ cursor: "pointer", fontSize: "16pt", marginLeft: "10px" }}>
            <FontAwesomeIcon icon={faComment} /> {post.comments.length}
          </span>
        </Link>
      </Card.Body>
    </Card>
  );
}
export default Post;
