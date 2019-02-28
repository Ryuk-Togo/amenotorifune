DROP TABLE IZANAMI.T_TASK;

CREATE TABLE IZANAMI.T_TASK
  ( TASK_ID             serial NOT NUL PRIMARY KEY
  , USER_ID             verchar(30) NOT NULL
  , TODO_ID             verchar(30) NOT NULL
  , TASK_DATE_TIME      datetime
  , TASK_DESCRIPTION    text
  , CREATE_DATE         date
  , CREATE_PG_ID        varchar(30)
  , CREATE_USER_ID      varchar(6)
  , UPDATE_DATE         date
  , UPDATE_PG_ID        varchar(30)
  , UPDATE_USER_ID      varchar(6)
  );