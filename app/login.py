from passlib.context import CryptContext
from fastapi import HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
import mysql.connector
from pydantic import BaseModel
from app.config import settings

SECRET_KEY = settings.SECRETKEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
pwd_context = CryptContext(schemes=["md5_crypt"])


def encryptpassword(password):
    hashpassword = pwd_context.hash(password)
    return hashpassword


def getrole():
    mydb = mysql.connector.connect(
        host=settings.HOST_NAME,
        user=settings.USER_NAME,
        password=settings.USER_PASSWORD,
        database=settings.DATABASE_NAME,
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * from roll",)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return(myresult)

def loginuser(username, plainpassword):
    mydb = mysql.connector.connect(
        host=settings.HOST_NAME,
        user=settings.USER_NAME,
        password=settings.USER_PASSWORD,
        database=settings.DATABASE_NAME,
    )
    mycursor = mydb.cursor(dictionary=True)
    # print("SELECT name,password FROM ioc where name=%s")
    val = (username,)
    mycursor.execute("SELECT name,password,map FROM ioc where name=%s", val)
    myresult = mycursor.fetchone()
    map=myresult['map']
    mycursor.close()
    mydb.close()
    # myres=dict(zip(mycursor.column_names, mycursor.fetchall()))
    if myresult:
        # print(myresult['name'])
        if pwd_context.verify(plainpassword, myresult["password"]):
            expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            data = {"username": map, "loginname":username, "exp": expire, "time": str(expire)}
            # print(data)
            encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
            return {"msg": "logged_in", "cookie": encoded_jwt,"uname":username}

        else:
            return {"msg": "invalid credentials"}
    else:
        return {"msg": "invalid credentials"}

    # valid=pwd_context.verify(plainpassword,"databasepass")
    # compare password
    # if not valid "raise HTTPException(status.HTTP_404_NOT_FOUND,details=f"invalid user")"
    # return jwttoken


def verifyuser(cookie: str):
    if not cookie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    try:
        data = jwt.decode(cookie, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = data.get("username")
        print(username)
        expiredtime = data.get("time")
        validity = datetime.fromisoformat(expiredtime) - datetime.now()
        # print("Username decrypted "+username)
        # print("Time validity "+ str(validity.total_seconds()))#vlaidity is negative means cookies expired
        # print("Time validity "+ str(datetime.now()))
        # print("Time validity "+ str(datetime.fromisoformat(expiredtime)))
        if validity.total_seconds() < 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Login Expired")

        mydb = mysql.connector.connect(
            host=settings.HOST_NAME,
            user=settings.USER_NAME,
            password=settings.USER_PASSWORD,
            database=settings.DATABASE_NAME,
        )
        mycursor = mydb.cursor(dictionary=True)
        # print("SELECT name,password FROM ioc where name=%s")
        val = (username,)
        mycursor.execute("SELECT name FROM ioc where name=%s", val)
        myresult = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        if not myresult:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    except JWTError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    return username

def verifyusermap(cookie: str):
    if not cookie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    try:
        data = jwt.decode(cookie, SECRET_KEY, algorithms=[ALGORITHM])
        mapname: str = data.get("loginname")
        expiredtime = data.get("time")
        validity = datetime.fromisoformat(expiredtime) - datetime.now()
        # print("Username decrypted "+username)
        # print("Time validity "+ str(validity.total_seconds()))#vlaidity is negative means cookies expired
        # print("Time validity "+ str(datetime.now()))
        # print("Time validity "+ str(datetime.fromisoformat(expiredtime)))
        if validity.total_seconds() < 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Login Expired")

        mydb = mysql.connector.connect(
            host=settings.HOST_NAME,
            user=settings.USER_NAME,
            password=settings.USER_PASSWORD,
            database=settings.DATABASE_NAME,
        )
        mycursor = mydb.cursor(dictionary=True)
        # print("SELECT name,password FROM ioc where name=%s")
        val = (mapname,)
        mycursor.execute("SELECT name FROM ioc where name=%s", val)
        myresult = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        if not myresult:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    except JWTError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    return mapname


def setcookie(username: str,loginname:str):
    if not username:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"invalid user")
    
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {"username": username, "loginname":loginname,"exp": expire, "time": str(expire)}
    # print(data)
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


