DROP TABLE IZANAMI.M_USER;

CREATE TABLE IZANAMI.M_USER
  ( USER_ID             verchar(30) NOT NULL PRIMARY KEY
  , USER_NAME           verchar(30) NOT NULL
  , PASSWORD            verchar(30)
  , CREATE_DATE         date
  , CREATE_PG_ID        varchar(30)
  , CREATE_USER_ID      varchar(6)
  , UPDATE_DATE         date
  , UPDATE_PG_ID        varchar(30)
  , UPDATE_USER_ID      varchar(6)
  );