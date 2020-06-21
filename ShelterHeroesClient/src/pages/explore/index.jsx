import React, { useState } from "react";
import { InputGroup, FormControl, Button } from "react-bootstrap";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";
import { Link } from "react-router-dom";

const Explore = (props) => {
  const [query, setQuery] = useState("");
  const { data, error } = useSWR(`/api/core/explore?q=${query}`, swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  return (
    <div>
      <InputGroup className="mb-3">
        <FormControl
          onKeyUp={(e) => {
            setQuery(e.target.value);
          }}
          placeholder="search..."
          aria-label="search..."
          aria-describedby="basic-addon"
        />
        <InputGroup.Append>
          <Button variant="primary">GO</Button>
        </InputGroup.Append>
      </InputGroup>
      {error ? (
        <div>error :( </div>
      ) : !data ? (
        <div>loading...</div>
      ) : data.length === 0 ? (
        <div>nothing found... :(</div>
      ) : (
        data.map((a, index) => (
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
        ))
      )}
    </div>
  );
};
export default Explore;
