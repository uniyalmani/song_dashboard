# song_dashboard

# docker-compose up -> for running app locally
# token based authentication
user can add multiple audio audio duration should be less then 10 min .
for adding multiple audio select audio and click add button then select other audio and click add button .....
if user has selected protected mode then user need to add emails of other user who can excess audio.
user can select multiple emails..
at last click upload button.


* http://0.0.0.0:8000/auth/login -> login 
* http://0.0.0.0:8000/auth/signup -> signup
* http://0.0.0.0:8000/user/home _> home 
* http://0.0.0.0:8000/user/upload_song -> for uploading songs (protected)
* http://0.0.0.0:8000/user/songs -> liat all the song uploaded by user (protected )
