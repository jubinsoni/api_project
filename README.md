# api_project

This repo contains django rest code for backend

following routes are available

## auth
GET ​/auth​/email-verify​/
(auth_email-verify_list)

POST /auth​/login​/
(auth_login_create)

POST /auth​/logout​/
(auth_logout_create)

PATCH /auth​/password-reset-complete
(auth_password-reset-complete_partial_update)

GET ​/auth​/password-reset​/{uidb64}​/{token}​/
(auth_password-reset_read)

POST ​/auth​/register​/
(auth_register_create)

POST ​/auth​/request-reset-email​/
(auth_request-reset-email_create)

POST ​/auth​/token​/refresh​/
(auth_token_refresh_create)

## feedback
GET /feedback​/
(feedback_list)

POST /feedback​/
(feedback_create)

GET /feedback​/{id}
(feedback_read)

PUT /feedback​/{id}
(feedback_update)

PATCH ​/feedback​/{id}
(feedback_partial_update)

DELETE /feedback​/{id}
(feedback_delete)

## social_auth

Go to google-signin and start a local server by python3 -m http.server 5500
now go to http://127.0.0.1:5500/ and get token from console
This token can be now validated using this api

POST /social_auth​/google​/
(social_auth_google_create)

## user_profile

GET /user_profile​/
(user_profile_read)

PUT /user_profile​/
(user_profile_update)

PATCH ​/user_profile​/
(user_profile_partial_update)

## Running locally
1) clone this repo
2) cd to project at the manage.py level
3) source venv/bin/activate
4) pip3 install -r requirements.txt
5) go to core/settings.py and do DEBUG = False
6) python3 manage.py runserver
7) go to http://127.0.0.1:8000/ to test out the apis

## Documentation
This app is configured with swagger and to view it...
simply go to http://127.0.0.1:8000/