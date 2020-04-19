import React from "react";
import useSWR from "swr";
import { swrFetcher } from "../../utils/fetcher";

const UserContext = React.createContext({
  user: {},
  revalidate: () => null,
});

const UserContextProvider = ({ children }) => {
  const { data, revalidate } = useSWR("/api/auth/info/", swrFetcher, {
    refreshInterval: 0,
    revalidateOnFocus: false,
  });

  if (!data) {
    return <p>... Loading</p>;
  }

  return (
    <UserContext.Provider value={{ user: data, revalidate }}>
      {children}
    </UserContext.Provider>
  );
};

export { UserContext, UserContextProvider };
