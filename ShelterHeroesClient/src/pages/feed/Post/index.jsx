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
      <Row noGutters mb={3}>
        <Col md={4}>
          <Card.Img variant="top" src={post.image} />
        </Col>
        <Col md={8}>
          <Card.Body>
            <Card.Title>
              <Link to={"/animals/" + post.posted_by.pk}>{post.posted_by.name}</Link>
            </Card.Title>
            <Card.Subtitle className="mb-2 text-muted">
              <Link to={"/shelters/" + post.posted_by.shelter.pk}>{post.posted_by.shelter.name}</Link>
            </Card.Subtitle>
            <Card.Text>{Text}</Card.Text>
            <Card.Text>{post.comments.length + " comments"}</Card.Text>
            <Card.Text>{likeCount + " likes"}</Card.Text>

            <ActionButton
              initEnabled={post.liked_by_viewer}
              disableActionPostUrl={"/api/core/posts/" + post.pk + "/unlike"}
              enableActionPostUrl={"/api/core/posts/" + post.pk + "/like"}
              enableActionCallback={() => setLikeCount(likeCount + 1)}
              disableActionCallback={() => setLikeCount(likeCount - 1)}
              contentEnabled={<FontAwesomeIcon icon={HeartSolid} />}
              contentDisabled={<FontAwesomeIcon icon={HeartBorder} />}
            />

            <Button variant="secondary">
              <FontAwesomeIcon icon={faComment} />
            </Button>
          </Card.Body>
        </Col>
      </Row>
    </Card>
  );
}
export default Post;
