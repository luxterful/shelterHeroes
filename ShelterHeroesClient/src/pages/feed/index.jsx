import React from "react";
import Post from "./Post";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";

const Feed = () => {
  const { data, error } = useSWR("/api/core/feed", swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  if (error) return <div>error :( </div>;

  if (!data) return <div>loading...</div>;

  if (data.length === 0) {
    return <p>Looks like you are not following any animal you douche bag</p>;
  }
  return data.map((post, k) => <Post post={post} />);
};
export default Feed;
