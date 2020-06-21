import React, { useState } from "react";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart as HeartBorder } from "@fortawesome/free-regular-svg-icons";
import { faHeart as HeartSolid } from "@fortawesome/free-solid-svg-icons";
import ActionButton from "../../components/ActionButton";
import TimeAgo from "javascript-time-ago";
import en from "javascript-time-ago/locale/en";
import { InputGroup, FormControl, Button } from "react-bootstrap";
import { fetcher } from "../../utils/fetcher";

function Post(props) {
  const [likeCount, setLikeCount] = useState(undefined);
  const { data, error, revalidate } = useSWR(`/api/core/posts/${props.match.params.uid}`, swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  const [comment, setComment] = useState("");
  const sendComment = () => {
    fetcher(`/api/core/posts/${props.match.params.uid}/comments`, {
      method: "POST",
      body: {
        text: comment,
      },
    }).then(() => {
      revalidate();
    });
  };

  TimeAgo.addLocale(en);
  const timeAgo = new TimeAgo("ru-RU");

  if (error) return <div>error :( </div>;
  if (!data) return <div>loading...</div>;

  if (likeCount === undefined) {
    setLikeCount(data.likes_count);
  }
  return (
    <div>
      <h1>{data.posted_by.name}</h1>
      <h3>{data.posted_by.shelter.name}</h3>
      <img alt={data.text} src={data.image.image_file} width="50%" />
      <p>{data.text}</p>

      <ActionButton
        initEnabled={data.liked_by_viewer}
        disableActionPostUrl={"/api/core/posts/" + data.pk + "/unlike"}
        enableActionPostUrl={"/api/core/posts/" + data.pk + "/like"}
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
      <h4 style={{ paddingTop: "10px" }}>
        <p>Comments</p>
      </h4>
      {data.comments.map((c) => (
        <p>
          <b>{c.user.full_name}</b> {c.text} - <i>{timeAgo.format(new Date(c.creation_date))}</i>
        </p>
      ))}
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
          <Button variant="primary" onClick={sendComment}>
            SEND
          </Button>
        </InputGroup.Append>
      </InputGroup>
    </div>
  );
}
export default Post;
