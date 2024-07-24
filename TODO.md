Basic Functionality:
- [ ] Configure a list of supported message types

Admin Menu in Group Chat:

- [ ] Introduce a convenient admin menu accessible within the group chat itself.f
- [ ] Implement a `/ban` command allowing admins to ban users by replying to their messages.
    - [ ] In-memory storage for temporary bans
    - [ ] Databases PostgreSQL for a permanent solution
- [ ] Enable admins to reply directly to users in private chats using a `/reply` command from within the group chat.

User Validation:

- [ ] Incorporate a mechanism to verify that new users are human.

Code Housekeeping:

- [ ] remove unnecessary libraries from requirements.txt (presently it's produced via `pip freeze`)