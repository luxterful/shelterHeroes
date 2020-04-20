import React, { useState } from "react";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart as HeartBorder } from "@fortawesome/free-regular-svg-icons";
import { faHeart as HeartSolid } from "@fortawesome/free-solid-svg-icons";
import ActionButton from "../../components/ActionButton";

function Animal(props) {
  const [likeCount, setLikeCount] = useState(undefined);
  const { data, error } = useSWR(`/api/core/posts/${props.match.params.uid}`, swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

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
      <p>likes: {likeCount}</p>

      <ActionButton
        initEnabled={data.liked_by_viewer}
        disableActionPostUrl={"/api/core/posts/" + data.pk + "/unlike"}
        enableActionPostUrl={"/api/core/posts/" + data.pk + "/like"}
        enableActionCallback={() => setLikeCount(likeCount + 1)}
        disableActionCallback={() => setLikeCount(likeCount - 1)}
        contentEnabled={<FontAwesomeIcon icon={HeartSolid} />}
        contentDisabled={<FontAwesomeIcon icon={HeartBorder} />}
      />
    </div>
  );
}
export default Animal;
