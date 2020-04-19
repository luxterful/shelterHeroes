import React, { useState } from "react";
import { Button } from "react-bootstrap";
import { fetcher } from "../utils/fetcher";

const ActionButton = ({
  initEnabled = false,
  enableActionPostUrl,
  disableActionPostUrl,
  enableActionCallback = () => null,
  disableActionCallback = () => null,
  contentEnabled,
  contentDisabled,
}) => {
  const [enabled, setEnabled] = useState(initEnabled);

  const clickHandle = () => {
    if (enabled) {
      fetcher(disableActionPostUrl, { method: "POST" }).then(() => {
        setEnabled(false);
        disableActionCallback();
      });
    } else {
      fetcher(enableActionPostUrl, { method: "POST" }).then(() => {
        setEnabled(true);
        enableActionCallback();
      });
    }
  };
  return <Button onClick={clickHandle}>{enabled ? contentEnabled : contentDisabled}</Button>;
};
export default ActionButton;
