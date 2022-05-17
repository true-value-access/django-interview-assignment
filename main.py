from ast import Return
from typing import List, Optional
from fastapi import FastAPI,HTTPException,status,UploadFile,Response,Request,Cookie
from fastapi.params import Body, File
from jose.jws import verify
from pydantic import BaseModel,BaseSettings
import mysql.connector
from sqlalchemy import JSON
from app import login
import requests
import json
from starlette.requests import cookie_parser
import time
import os
from app.config import settings
from datetime import date, datetime
from starlette.requests import cookie_parser
from starlette.responses import Response
from starlette.responses import FileResponse
import pathlib
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import random

import math
# import fpdf

script_dir = os.path.dirname(__file__)
staticpath = os.path.join(script_dir, "static/")

app=FastAPI()

origins=settings.ORIGINS

# Get role
@app.get("/getrole")
def getrole():
    return(login.getrole())


@app.post("/signup")
def signup():
    return({"message":"hello"})



#login------------------------------------------------------------------
# @app.post("/login")
# def loginpage(request:Request,response:Response,userdetails:user): #
    
#     token=login.loginuser(userdetails.username,userdetails.password)
#     if(token['msg']=="invalid credentials"):
#         return({"msg":"invalid credentials"})
    
#     response.set_cookie(key="Manish",value=token['cookie'], httponly=True,secure=settings.SECURITYHHTPS, samesite=settings.SAMESITE)
    
#     return ({"msg":"login Successfull","uname":token['uname']})#,"Manish":token['cookie']})

@app.post("/logout")
def logout(response:Response):
    response.delete_cookie("Manish")
    response.set_cookie(key="Manish",value="a", httponly=True,secure=settings.SECURITYHHTPS, samesite=settings.SAMESITE)
    return({"msg":"logout successfull"})





# @app.post("/changepassword")
# def changepassword(password:Password,Manish:Optional[str] = Cookie(None)):
#     return(login.changepassword(password.old_passowrd,password.new_passowrd,Manish))

# @app.post("/adminresetpassword")
# def changepassword(name:login.resetpass,Manish:Optional[str] = Cookie(None)):
#     return(login.resetpassword(name.ioc,name.password,Manish))

# @app.post("/admincreateuser")
# def createuser(user:login.Createuser,Manish:Optional[str] = Cookie(None)):
#     return(login.createuser(user,Manish))



#login------------------------------------------------------------------
