import React from "react";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";

const Shelter = (props) => {
  const { data, error } = useSWR(`/api/core/shelters/${props.match.params.uid}`, swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  if (error) return <div>error :( </div>;
  if (!data) return <div>loading...</div>;
  return (
    <div>
      <h1>{data.name}</h1>
    </div>
  );
};
export default Shelter;
