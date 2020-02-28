import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "auth-fsnd.eu.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "castings"
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXpRekpGUlVGR1F6QTJNekpGTVRVM01EWkVOalkwUlRGQk5qSTRORGd6TWtOR05UVkZOQSJ9.eyJpc3MiOiJodHRwczovL2F1dGgtZnNuZC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU1N2U5ODc3NzgwZWIxNmI0OTA0ODk4IiwiYXVkIjoiY2FzdGluZ3MiLCJpYXQiOjE1ODI4ODMxODksImV4cCI6MTU4Mjg5MDM4OSwiYXpwIjoibEN4UjNFdG12TTBIdHJ0TUJYZmxsYXpSTmgxVjFiMEkiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.ZP69j50d-0vOuKyDbjvjdqsJ9dGGMCaX0OqcL-nIcG8dCMhnaP1eT_QPrW45gIXtARxWtAk_DB8AmLr-IBxg5vyT5p2IbUbkZOW8KCVQbWo7h2prrocQU9fQ799fWi_gmEQr_7inoI3YUN6RQlo7piDu72H22cO0gH6DdefWzHlZzXjga2LAp6rBC-3p3Ca34kgi1s3sP5UFFTT2TzCAd5uhMJ7bv5D__fV9izH_xGFYFK9G6XWVibH0eGPh0J6fcB4hBbX2lGE_iNa15X1lvqOTIStpElOedI7ebxXUK0kvFPh7ZLUSxA_dpuOJ8ZxLJX7LdkmkhsfJ42gIl-Y8cA",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXpRekpGUlVGR1F6QTJNekpGTVRVM01EWkVOalkwUlRGQk5qSTRORGd6TWtOR05UVkZOQSJ9.eyJpc3MiOiJodHRwczovL2F1dGgtZnNuZC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU1N2U5NDRlOWEwYjIxNmI1YzgwMjQzIiwiYXVkIjoiY2FzdGluZ3MiLCJpYXQiOjE1ODI4ODMyNTUsImV4cCI6MTU4Mjg5MDQ1NSwiYXpwIjoibEN4UjNFdG12TTBIdHJ0TUJYZmxsYXpSTmgxVjFiMEkiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsIm1vZGlmeTphY3RvciIsIm1vZGlmeTptb3ZpZSIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.NuO0IAqOj0WvdBwbrGj2wN9cEPzsy3xgos9CNIwqw2Hz07bBOQnN0xPDhsxEgZsjatEDxSJ5CWOK5nnYNPCrICyBswUBglBcUpDiBrRbZBcZLpFGu5fwe1MZ2O0GZRn_Rj-Cbp1mLR-KEQAjNL4E3O7n9NHQIOdQrnfBSEK79Dc6c17GtVkLw1pBm9QX0tpy58dU9MLEaDKueWVikQNhKUE-koei2Cz3iuk7g4h7FAiTyP-wImsazvGcw21MqJvHGILEy7V8hCy8v5H66YnF8nPf6815O3uASON1wwHawKp30chi4KCz6BkE7djeI2Ayl1jwksgn5pXEBIhp3_su2A",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXpRekpGUlVGR1F6QTJNekpGTVRVM01EWkVOalkwUlRGQk5qSTRORGd6TWtOR05UVkZOQSJ9.eyJpc3MiOiJodHRwczovL2F1dGgtZnNuZC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU1N2ViODgyZDcyNTMxNmIxOTZhMGRkIiwiYXVkIjoiY2FzdGluZ3MiLCJpYXQiOjE1ODI4ODMzMDUsImV4cCI6MTU4Mjg5MDUwNSwiYXpwIjoibEN4UjNFdG12TTBIdHJ0TUJYZmxsYXpSTmgxVjFiMEkiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsIm1vZGlmeTphY3RvciIsIm1vZGlmeTptb3ZpZSIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.IbxE9m9_3FntM3P_k9fbHcc-XaGHQzNGGhEwT2RgsQl4iuu9x3tES44g-lmIZvxPP0t438WgCdnDogJgGbIYUe8lyoz5cSweUK9IH-0JaTFzTJbE-hoNjk_TJexca403UGdtrG8JKtuMvykeJBo_ldtiyCMJuWw-TcsEtfxyjEQ7ZbxCoc3xu92Bmj_VcBSX_xQiY_on-fpp06OmZmREvpI2FSV6T08kRZHaNSN7dFpZO_5bWb6yVp9tZCE2mcFQ8-kWYhPb5BsIHKSCtJL-Yg6Bd1ggtr53SAjVm5nhONXwdYcY_BufTjcTDwKvgrJ5y0ZDXzG51mBEx15-TQqBXA"
}

