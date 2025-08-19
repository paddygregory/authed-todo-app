# DESCRIPTION OF AUTH

## requirements for auth

1. create a users table: store id, email(unique), password_hash, status(done=False)
2. hash passwords on write: when a user signs up, hash their password and save the hash, not the password (done=False)
3. add auth/register: endpoint that validates email/password, hashes it, inserts a users row, and returns a success response- no tokens yet (done=False)
4. add /auth/login -> issue tokens: look user up by email, verify pw against hash_pw. If valid, mint a 15 min access JWT. Also mint a refresh token. (done=False)
5. return tokens to client: respond with JSON like {"access_token": jwt", "token_type": "bearer", "refresh_token": "opaque"} (done=False)
6. teach client to send the header (done=False)
7. add auth middleware dependency: for every protected route, read auth header, ensure its bearer token, verify JWT sig, extract sub, load user (done=False)
8. inside todo handlers, never trust client-sent user ids, always use user_id from context (done=False)
9. add /auth/refresh: accept a refresh token, if it matches a hashed row and isnt expired/revoked (done=False)
10. add /auth/logout: accepts a refresh token and marks its db row (done=False)
11. choose a signing strategy and keep keys safe (done=False)
12. validate right claims (done=False)


valid shape:

- tables: users, refresh_tokens (hashed), todos with owner_id
- endpoints: public, /auth/register, /auth/login, /auth/refresh, /health
- middleware: verifies jwt, attaches user_id
- handlers: use user_id from context, never from the request body