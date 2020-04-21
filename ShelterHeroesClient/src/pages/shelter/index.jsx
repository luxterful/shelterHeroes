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
      <div>
        {data.has_animals.map((a, index) => (
          <Link key={index} to={"/animals/" + a.pk}>
            <div style={{ marginBottom: "20px", fontSize: "20pt" }}>
              <img
                src={a.image?.image_file}
                width={100}
                height={100}
                style={{ marginRight: "20px", borderRadius: "50px", backgroundColor: "grey" }}
              />
              {a.name}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};
export default Shelter;
