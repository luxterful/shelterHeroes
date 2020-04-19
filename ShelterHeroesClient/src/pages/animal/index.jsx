import React from "react";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import ActionButton from "../../components/ActionButton";

const Animal = (props) => {
  const { data, error } = useSWR(`/api/core/animals/${props.match.params.uid}`, swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  if (error) return <div>error :( </div>;
  if (!data) return <div>loading...</div>;
  return (
    <div>
      <h1>{data.name}</h1>
      <h3>{data.shelter.name}</h3>
      <p>
        <ActionButton
          initEnabled={data.followed_by_viewer}
          disableActionPostUrl={"/api/core/animals/" + data.pk + "/unfollow"}
          enableActionPostUrl={"/api/core/animals/" + data.pk + "/follow"}
          contentEnabled="Following"
          contentDisabled="Follow"
        />
      </p>
      Recent Posts
      <Row>
        {data.recent_posts.map((post) => (
          <Col md={4}>
            <Link to={"/posts/" + post.pk}>
              <img alt={post.text} src={post.image} width="100%" />
            </Link>
          </Col>
        ))}
      </Row>
    </div>
  );
};
export default Animal;
