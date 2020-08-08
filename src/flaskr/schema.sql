DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS markets;
DROP TABLE IF EXISTS stalls;

-- log in stuff
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

-- one market can have many stalls 

-- child table
CREATE TABLE stalls (
  stall_id INTEGER PRIMARY KEY,
  stall_name text NOT NULL,
  market_id INTEGER NOT NULL,
  FOREIGN KEY (market_id)
    REFERENCES markets (market_id)
);

-- parent table 
CREATE TABLE markets (
  market_id INTEGER PRIMARY KEY,
  market_name text NOT NULL
);