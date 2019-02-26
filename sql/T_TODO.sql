DROP TABLE IZANAMI.T_TODO;

CREATE TABLE IZANAMI.T_TODO
  ( TODO_ID             serial NOT NULL PRIMARY KEY
  , TITLE               varchar(30)
  , DISCRIPTION         varchar(200)
  , SHOULD_ACTION       int
  , WHERE_DONT_ACTION   int
  , SINGLE_ACTON        int
  , CAN_DO_TOW_MINITE   int
  , SHOULD_MYSELF       int
  , SHOULD_DO_THAN_2MIN int
  , USER_ID             varchar(6)
  , CATEGORY            varchar(2)
  , CREATE_DATE         date
  , CREATE_PG_ID        varchar(30)
  , CREATE_USER_ID      varchar(6)
  , UPDATE_DATE         date
  , UPDATE_PG_ID        varchar(30)
  , UPDATE_USER_ID      varchar(6)
  );