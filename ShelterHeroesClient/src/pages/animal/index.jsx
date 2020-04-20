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
      <img
        src={data.image?.image_file}
        width={100}
        height={100}
        style={{ borderRadius: "50px", float: "left", marginRight: "24px", backgroundColor: "grey" }}
      />
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
      <p>Recent Posts</p>
      <Row>
        {data.recent_posts.map((post) => (
          <Col md={4}>
            <Link to={"/posts/" + post.pk}>
              <img
                alt={post.text}
                src={post.image.image_file}
                width="100%"
                style={{ borderRadius: "5px", backgroundColor: "grey" }}
              />
            </Link>
          </Col>
        ))}
      </Row>
    </div>
  );
};
export default Animal;
