import getCookie from "./cookies";

const fetcher = (url, { body = undefined, method, headers = {} }) => {
  const requestHeaders = headers;
  let requestBody = body;
  if (typeof body !== "string" && body) {
    requestBody = JSON.stringify(body);
    requestHeaders["Content-Type"] = "application/json";
  }
  requestHeaders["X-CSRFToken"] = getCookie("csrftoken");
  requestHeaders["Cache-Control"] = "no-cache";

  return fetch(url, {
    method,
    body: requestBody,
    headers: requestHeaders,
    credentials: "include",
  });
};

const swrFetcher = (url) =>
  fetch(url, {
    cache: "no-cache",
    method: "GET",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Cache-Control": "no-cache",
      Pragma: "no-cache",
    },
    credentials: "include",
  }).then((r) => {
    if (r.status === 200) {
      return r.json();
    } else {
      throw new Error("Error");
    }
  });

export { fetcher, swrFetcher };
