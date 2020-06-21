import React from "react";
import Post from "./Post";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { Row, Col } from "react-bootstrap";

const Feed = () => {
  const { data, error } = useSWR("/api/core/feed", swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  if (error) return <div>error :( </div>;

  if (!data) return <div>loading...</div>;

  if (data.length === 0) {
    return (
      <p style={{ textAlign: "center", fontSize: "22pt" }}>
        Looks like you are not following any animal!
        <br /> Click on Explore to find some.
      </p>
    );
  }
  return (
    <Row>
      {data.map((post, k) => (
        <Col md={6}>
          <Post post={post} />
        </Col>
      ))}
    </Row>
  );
};
export default Feed;
