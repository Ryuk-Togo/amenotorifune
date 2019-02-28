DROP TABLE IZANAMI.T_REMAIND;

CREATE TABLE IZANAMI.T_REMAIND
  ( REMAIND_ID          serial NOT NUL PRIMARY KEY
  , USER_ID             verchar(30) NOT NULL
  , TASK_ID             verchar(30) NOT NULL
  , REMAIND_DATE_TIME   datetime
  , MESSAGE             text
  , CREATE_DATE         date
  , CREATE_PG_ID        varchar(30)
  , CREATE_USER_ID      varchar(6)
  , UPDATE_DATE         date
  , UPDATE_PG_ID        varchar(30)
  , UPDATE_USER_ID      varchar(6)
  );