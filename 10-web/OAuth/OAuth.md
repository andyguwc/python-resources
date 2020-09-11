# OAuth 2.0 (for Authorization)
https://www.youtube.com/watch?v=996OiexHze0

## History 
Simple Login
SAML
Mobile app login
Delegated authorization
- how can I let a website access my data without giving them password

## OAuth 2.0 Terminology
Resource owner - the user who owns their data 
Client - application who wants to access the data 
Authorization server - system to authorize that (google)
Resource server - the system that pulls the data (like user contacts)
Authorization grant - proves the user clicks yes and consents the permission
Redirect URI - authorization server directs the user to 
Access token - the key client really needs

## OAuth Dance for Authorization
https://medium.com/typeforms-engineering-blog/the-beginners-guide-to-oauth-dancing-4b8f3666de10


Steps
- Have a button on the app (client) 
- Once user clicks on the button, it directs to google domain
- google prompts login form, after login, google tells you what scope the app wants to access
- After user clicks yes, google sends the code to app/callback
- With the code, and client secret, app talks to google to ask of an OAuth token 
- App can talk to google with the OAuth token on behalf of the user

Why 2 step here
- back channel going from my backend server to my api
- front channel browser - all stuff is passed through the browser
- code is passed as query params
- but authtoken need to be more secure (server to authserver)
- that client secret plus authorization code makes sure even if someone steals the authorization code, they don't have the secret to ask for auth token from the authorizaiton server

The App developer needs to create a client at Google 
- to get a client id and a client secret


# OpenID Connect (for Authentication)

OAuth should not be used for authentication
- hack for OAuth 
- no standard way to get user info

OpenID Connect is for authentication
- add ID token (JWT)
- UserInfo endpoint for getting more user information 
- Standard set of scopes
- Standardized implementation 

Differences
- scope includes openid to identify as an openid connect request
- asks for id token and more information for the user /userinfo
- able to know who the user is 




